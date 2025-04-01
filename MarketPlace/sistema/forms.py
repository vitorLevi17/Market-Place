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

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(
        label="Username",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Doador Oliveira"
            }
        )
    )
    nome = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Doador"
            }
        )
    )
    sobrenome = forms.CharField(
        label="Sobrenome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Oliveira"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ex. Doador.Oliveira@gmail.com"
            }
        )
    )
    cpf = forms.CharField(
        label="Cpf",
        required=True,
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. 00011122233"
            }
        )
    )
    telefone = forms.CharField(
        label="Telefone",
        required=True,
        max_length=13,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. 5571999998888"
            }
        )
    )
    cep = forms.CharField(
        label="Cep",
        required=True,
        max_length=7,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. 0011122"
            }
        )
    )
    complemento = forms.CharField(
        label="Complemento",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Do lado do bar do zé"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ex. Insira sua senha"
            }
        )
    )
    senha1 = forms.CharField(
        label="SenhaC",
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ex. Confirme a senha"
            }
        )
    )