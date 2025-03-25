from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Email"
            }
        )
    )
    senha = forms.CharField(
        label="senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha"
            }
        )
    )