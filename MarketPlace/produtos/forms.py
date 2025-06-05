from django import forms

class CompraForm(forms.Form):
    quantidade = forms.DecimalField(
        label="quantidade",
        required=True,
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Digite a quantidade"
            }
        )
    )

    cep = forms.CharField(
        label="cep",
        required=True,
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. 00111222"
            }
        )
    )
    complemento = forms.CharField(
        label="complemento",
        required=True,
        max_length=225,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Edificio apt 101 em frente ao Subway"
            }
        )
    )
