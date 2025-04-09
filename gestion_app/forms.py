from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur, Enfant,Don


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        label="Type d'utilisateur",
        choices=Utilisateur.USER_TYPE_CHOICES,
        widget=forms.Select(),
    )

    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = UserCreationForm.Meta.fields + ('user_type',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ➤ On supprime le help_text du champ username
        self.fields['username'].help_text = ""
        self.fields['password2'].help_text = ""

    def clean_user_type(self):
        user_type = self.cleaned_data.get('user_type')
        if not user_type:
            raise forms.ValidationError("Veuillez sélectionner un type d'utilisateur.")
        return user_type

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
        return user



class EnfantForm(forms.ModelForm):  # On renomme correctement le formulaire
    class Meta:
        model = Enfant  # On utilise le modèle Enfant
        fields = ['nom', 'prenom', 'age', 'groupe_sanguin', 'stade','sexe','pays','ville','statut']  # Ajoute tous les champs requis

    # Personnalisation des widgets avec placeholders et texte d'aide
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'placeholder': 'Entrez le nom'})
        self.fields['prenom'].widget.attrs.update({'placeholder': 'Entrez le prénom'})
        self.fields['age'].widget.attrs.update({'placeholder': 'Entrez l\'âge'})
        self.fields['groupe_sanguin'].widget.attrs.update({'class': 'form-select'})
        self.fields['sexe'].widget.attrs.update({'class': 'form-select'})
        self.fields['stade'].widget.attrs.update({'class': 'form-select'})
        self.fields['pays'].widget.attrs.update({'class': 'form-select'})
        self.fields['ville'].widget.attrs.update({'class': 'form-select'})
        self.fields['statut'].widget.attrs.update({'class': 'form-select'})

class DonForm(forms.ModelForm):
    class Meta:
        model = Don
        fields = ['nom', 'email', 'montant', 'moyen_paiement', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': "Votre nom"}),
            'email': forms.EmailInput(attrs={'placeholder': "Votre adresse email"}),
            'montant': forms.NumberInput(attrs={'placeholder': "Montant du don (en FCFA)"}),
            'moyen_paiement': forms.Select(),
            'message': forms.Textarea(attrs={'placeholder': "Message (optionnel)"}),
        }





