from django import forms

from .models import MensajeContacto


class MensajeContactoForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "d-none", "tabindex": "-1", "autocomplete": "off"}))

    class Meta:
        model = MensajeContacto
        fields = ["nombre", "email", "telefono", "asunto", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre completo"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "correo@empresa.com"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder": "+502 ..."}),
            "asunto": forms.TextInput(attrs={"class": "form-control", "placeholder": "Asunto"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Cuéntanos tu necesidad"}),
        }

    def clean_website(self):
        website = self.cleaned_data.get("website", "")
        if website:
            raise forms.ValidationError("Solicitud inválida.")
        return website
