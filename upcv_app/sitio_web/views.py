from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import MensajeContactoForm
from .models import (
    BloqueContenido,
    ConfiguracionSitio,
    HeroSlide,
    MensajeContacto,
    Pagina,
    PreguntaFrecuente,
    Proyecto,
    Servicio,
    Testimonio,
    AliadoLogo,
)


def _common_context():
    config = ConfiguracionSitio.objects.order_by("id").first() or ConfiguracionSitio()
    return {
        "sitio_config": config,
        "servicios_menu": Servicio.objects.filter(activo=True)[:8],
        "paginas_menu": Pagina.objects.filter(publicada=True, mostrar_en_menu=True),
    }


@require_http_methods(["GET", "POST"])
def home(request):
    form = MensajeContactoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Gracias, recibimos tu solicitud. Te contactaremos pronto.")
        return redirect("sitio_web:contacto")

    context = {
        **_common_context(),
        "slides": HeroSlide.objects.filter(activo=True),
        "servicios_destacados": Servicio.objects.filter(activo=True, destacado=True)[:6],
        "proyectos_destacados": Proyecto.objects.filter(activo=True, destacado=True)[:6],
        "testimonios": Testimonio.objects.filter(activo=True)[:8],
        "faqs": PreguntaFrecuente.objects.filter(activo=True)[:8],
        "aliados": AliadoLogo.objects.filter(activo=True)[:16],
        "fortalezas": BloqueContenido.objects.filter(activo=True, clave="fortalezas"),
        "soluciones": BloqueContenido.objects.filter(activo=True, clave="soluciones"),
        "estadisticas": BloqueContenido.objects.filter(activo=True, clave="estadisticas"),
        "cta": BloqueContenido.objects.filter(activo=True, clave="cta").first(),
        "form": form,
    }
    return render(request, "sitio_web/home.html", context)


def nosotros(request):
    return render(request, "sitio_web/nosotros.html", _common_context())


def servicios(request):
    context = {
        **_common_context(),
        "servicios": Servicio.objects.filter(activo=True),
    }
    return render(request, "sitio_web/servicios.html", context)


def servicio_detalle(request, slug):
    servicio = get_object_or_404(Servicio, slug=slug, activo=True)
    return render(request, "sitio_web/servicio_detalle.html", {**_common_context(), "servicio": servicio})


def proyectos(request):
    context = {
        **_common_context(),
        "proyectos": Proyecto.objects.filter(activo=True),
    }
    return render(request, "sitio_web/proyectos.html", context)


def proyecto_detalle(request, slug):
    proyecto = get_object_or_404(Proyecto, slug=slug, activo=True)
    return render(request, "sitio_web/proyecto_detalle.html", {**_common_context(), "proyecto": proyecto})


@require_http_methods(["GET", "POST"])
def contacto(request):
    form = MensajeContactoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        mensaje: MensajeContacto = form.save()
        messages.success(request, f"Mensaje enviado correctamente, {mensaje.nombre}.")
        return redirect("sitio_web:contacto")
    return render(request, "sitio_web/contacto.html", {**_common_context(), "form": form})


def pagina_detalle(request, slug):
    pagina = get_object_or_404(Pagina, slug=slug, publicada=True)
    return render(request, "sitio_web/pagina_detalle.html", {**_common_context(), "pagina": pagina})
