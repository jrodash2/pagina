from django import forms

from .models import ContactoLead


class ContactoLeadForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "d-none", "tabindex": "-1", "autocomplete": "off"}))

    class Meta:
        model = ContactoLead
        fields = ["nombre", "empresa", "correo", "telefono", "servicio_interes", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre completo"}),
            "empresa": forms.TextInput(attrs={"class": "form-control", "placeholder": "Empresa"}),
            "correo": forms.EmailInput(attrs={"class": "form-control", "placeholder": "correo@empresa.com"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder": "+502 ..."}),
            "servicio_interes": forms.TextInput(attrs={"class": "form-control", "placeholder": "Servicio de interés"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Cuéntanos tu necesidad"}),
        }

    def clean_website(self):
        website = self.cleaned_data.get("website", "")
        if website:
            raise forms.ValidationError("Solicitud inválida.")
        return website
