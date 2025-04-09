from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, EnfantForm, DonForm
from .models import Enfant , ONG, Medecin ,Don
from django.http import HttpResponse
from django.utils import timezone
from .models import Utilisateur
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import pandas as pd


# Vue pour l'inscription
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie ! Vous pouvez vous connecter.')
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})



# Vue pour la connexion
def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_type = getattr(user, 'user_type', None)
            # Redirige en fonction du type d'utilisateur
            if user_type == 'doctor':
                return redirect('doctor_dashboard')
            elif user_type == 'ong':
                return redirect('ong_dashboard')
           
            else:
                return render(request, 'erreur.html')  # Assurez-vous que ce template existe
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')




@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard/doctor_dashboard.html')



@login_required
def ong_dashboard(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'ajouter':
            return redirect('ajouter_enfant')  # URL nommée pour ajouter enfant
        elif action == 'liste':
            return redirect('liste_enfant')    # URL nommée pour liste enfant
        elif action == 'rapport':
            return redirect ('rapport')
    return render(request, 'ong_dashboard/ong_dashboard.html')


def ajouter_enfant(request):
    if request.method == 'POST':
        form = EnfantForm(request.POST)
        if form.is_valid():
            enfant = form.save(commit=False)  # Crée l'objet enfant sans l'enregistrer immédiatement
            enfant.utilisateur = request.user  # Associe l'enfant à l'utilisateur connecté
            
            # Vérifie que l'utilisateur connecté est bien une ONG avant d'assigner l'ONG
            if request.user.user_type == 'ong':
                enfant.ong = request.user  # Définit l'ONG comme l'utilisateur connecté
            else:
                return HttpResponse("Vous n'êtes pas autorisé à ajouter un enfant.")  # Gère les accès incorrects

            enfant.save()  # Enregistre l'objet enfant dans la base de données
            return redirect('ong_dashboard')  # Redirige vers le tableau de bord des ONG
    else:
        form = EnfantForm()  # Crée une nouvelle instance du formulaire pour une requête GET

    return render(request, 'ong_dashboard/ajouter_enfant.html', {'form': form})



def liste_enfant(request):
    if request.GET.get('mes_enfants') is not None:
        enfants = Enfant.objects.filter(ong=request.user)
        print("Enfants filtrés:", enfants)  # Débogage
    else:
        enfants = Enfant.objects.all()  # Récupérer tous les enfants
        
    return render(request, 'ong_dashboard/liste_enfant.html', {'enfants': enfants})


def rapport(request):
    total_enfants = Enfant.objects.count()
    total_medecins = Utilisateur.objects.filter(user_type='Medecin').count()
    total_ongs = Utilisateur.objects.filter(user_type='ong').count()
    
    context = {
        'total_enfants': total_enfants,
        'total_medecins': total_medecins,
        'total_ongs': total_ongs,
    }
    return render(request, 'ong_dashboard/rapport.html', context)

# Vue pour la déconnexion
def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté avec succès.')
    return redirect('connexion')

def index(request):
    return render(request,'index.html')


def nosactions(request):
    return render(request,'nosactions.html')
    
    
def apropos(request):
    return render(request,'apropos.html')

def contact(request):
    return render(request,'contact.html')


def merci(request):
    return render(request, 'merci.html')


def don(request):
    if request.method == 'POST':
        form = DonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('merci')  # Redirige vers une page de remerciement
    else:
        form = DonForm()
    return render(request, 'don.html', {'form': form})


# PDF Export
def export_pdf(request):
    dons = Don.objects.all()
    html = render_to_string('export_pdf.html', {'don': don})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="listedon.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

def listedon(request):
    don = Don.objects.all().order_by('date_don')
    return render(request, 'listedon.html', {'don': don})


def export_enfant(request):
    enfants = Enfant.objects.all()
    html = render_to_string('export_enfant.html', {'enfants': enfants})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="liste_enfant.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response
