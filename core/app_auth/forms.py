from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Nom de l'Utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd=forms.CharField(label= "Mot de Passe", widget=forms.PasswordInput(attrs={'class':'form-control'}))


class RegisterForm(forms.Form):
    username=forms.CharField(label="Nom de l'Utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd=forms.CharField(label= "Mot de Passe", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    conf_pwd=forms.CharField(label= "Confirmer mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control'}))
