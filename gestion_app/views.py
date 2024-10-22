from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, EnfantForm
from .models import Enfant

# Vue pour l'inscription
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Supprimez cette ligne pour enlever le message de succès
            # messages.success(request, 'Inscription réussie ! Vous pouvez vous connecter.')
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
    return render(request,'ong_dashboard/ong_dashboard.html')


  



# Vue pour la déconnexion
def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté avec succès.')
    return redirect('connexion')


