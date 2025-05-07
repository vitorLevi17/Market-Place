from django import forms

class QuantidadeProdutoForms(forms.Form):
     quantidade = forms.DecimalField(
        label="quantidade",
        required=True,
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                "placeholder":"Digite a quantidade"
            }
        )
    )