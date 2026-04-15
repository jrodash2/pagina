from django import forms
from django.contrib.auth.forms import AuthenticationForm

from sitio_web.models import (
    AliadoLogo,
    BloqueContenido,
    ConfiguracionSitio,
    HeroSlide,
    MensajeContacto,
    Pagina,
    PreguntaFrecuente,
    Proyecto,
    ProyectoImagen,
    Servicio,
    Testimonio,
)


class RihoAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Usuario"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Contraseña"}))


class BaseStyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, (forms.CheckboxInput, forms.ClearableFileInput)):
                continue
            field.widget.attrs.setdefault("class", "form-control")


class ConfiguracionSitioForm(BaseStyledModelForm):
    class Meta:
        model = ConfiguracionSitio
        exclude = ("created_at", "updated_at")


class HeroSlideForm(BaseStyledModelForm):
    class Meta:
        model = HeroSlide
        exclude = ("created_at", "updated_at")


class PaginaForm(BaseStyledModelForm):
    class Meta:
        model = Pagina
        exclude = ("created_at", "updated_at")


class ServicioForm(BaseStyledModelForm):
    class Meta:
        model = Servicio
        exclude = ("created_at", "updated_at")


class ProyectoForm(BaseStyledModelForm):
    class Meta:
        model = Proyecto
        exclude = ("created_at", "updated_at")


class ProyectoImagenForm(BaseStyledModelForm):
    class Meta:
        model = ProyectoImagen
        exclude = ("created_at", "updated_at")


class TestimonioForm(BaseStyledModelForm):
    class Meta:
        model = Testimonio
        exclude = ("created_at", "updated_at")


class AliadoLogoForm(BaseStyledModelForm):
    class Meta:
        model = AliadoLogo
        exclude = ("created_at", "updated_at")


class PreguntaFrecuenteForm(BaseStyledModelForm):
    class Meta:
        model = PreguntaFrecuente
        exclude = ("created_at", "updated_at")


class BloqueContenidoForm(BaseStyledModelForm):
    class Meta:
        model = BloqueContenido
        exclude = ("created_at", "updated_at")


class MensajeContactoEstadoForm(BaseStyledModelForm):
    class Meta:
        model = MensajeContacto
        fields = ["leido"]
