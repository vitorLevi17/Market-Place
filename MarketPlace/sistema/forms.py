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

class UsuarioForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Doador Oliveira"
            }
        )
    )
    nome = forms.CharField(
        label="Nome",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Doador"
            }
        )
    )
    sobrenome = forms.CharField(
        label="Sobrenome",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Oliveira"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
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
        max_length=8,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. 0011122"
            }
        )
    )
    complemento = forms.CharField(
        label="Complemento",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Do lado do bar do zé"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ex. Insira sua senha"
            }
        )
    )
    senha1 = forms.CharField(
        label="SenhaC",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ex. Confirme a senha"
            }
        )
    )