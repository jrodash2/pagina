from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

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

from .forms import (
    AliadoLogoForm,
    BloqueContenidoForm,
    ConfiguracionSitioForm,
    HeroSlideForm,
    MensajeContactoEstadoForm,
    PaginaForm,
    PreguntaFrecuenteForm,
    ProyectoForm,
    ProyectoImagenForm,
    RihoAuthForm,
    ServicioForm,
    TestimonioForm,
)
from .permissions import cms_required


@login_required(login_url="cms_web:login")
@cms_required
def dashboard(request):
    context = {
        "total_servicios": Servicio.objects.count(),
        "total_proyectos": Proyecto.objects.count(),
        "total_mensajes": MensajeContacto.objects.count(),
        "no_leidos": MensajeContacto.objects.filter(leido=False).count(),
        "ultimos_mensajes": MensajeContacto.objects.all()[:8],
        "resumen_proyectos": Proyecto.objects.values("categoria").annotate(total=Count("id")).order_by("-total")[:6],
    }
    return render(request, "cms_web/dashboard.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("cms_web:dashboard")
    form = RihoAuthForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("cms_web:dashboard")
    return render(request, "cms_web/auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("cms_web:login")


class CmsListView(ListView):
    template_name = "cms_web/crud_list.html"
    context_object_name = "items"
    paginate_by = 30

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["list_title"] = getattr(self, "list_title", self.model._meta.verbose_name_plural.title())
        create_url_name = getattr(self, "create_url_name", None)
        ctx["create_url"] = reverse_lazy(create_url_name) if create_url_name else None
        ctx["is_mensaje_model"] = self.model.__name__ == "MensajeContacto"
        return ctx

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(cms_required(view), login_url="cms_web:login")


class CmsCreateView(CreateView):
    template_name = "cms_web/crud_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form_title"] = getattr(self, "form_title", self.model._meta.verbose_name.title())
        return ctx

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(cms_required(view), login_url="cms_web:login")


class CmsUpdateView(UpdateView):
    template_name = "cms_web/crud_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form_title"] = getattr(self, "form_title", self.model._meta.verbose_name.title())
        return ctx

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(cms_required(view), login_url="cms_web:login")


class CmsDeleteView(DeleteView):
    template_name = "cms_web/crud_delete.html"

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(cms_required(view), login_url="cms_web:login")


class ConfiguracionUpdateView(CmsUpdateView):
    model = ConfiguracionSitio
    form_class = ConfiguracionSitioForm
    success_url = reverse_lazy("cms_web:configuracion")

    def get_object(self, queryset=None):
        return ConfiguracionSitio.objects.order_by("id").first() or ConfiguracionSitio.objects.create(nombre_sitio="Tecnologías de Guatemala")


class HeroList(CmsListView):
    model = HeroSlide
    ordering = ["orden", "id"]
    create_url_name = "cms_web:hero_nuevo"


class HeroCreate(CmsCreateView):
    model = HeroSlide
    form_class = HeroSlideForm
    success_url = reverse_lazy("cms_web:heroes")


class HeroUpdate(CmsUpdateView):
    model = HeroSlide
    form_class = HeroSlideForm
    success_url = reverse_lazy("cms_web:heroes")


class HeroDelete(CmsDeleteView):
    model = HeroSlide
    success_url = reverse_lazy("cms_web:heroes")


class PaginaList(CmsListView):
    model = Pagina
    create_url_name = "cms_web:pagina_nueva"


class PaginaCreate(CmsCreateView):
    model = Pagina
    form_class = PaginaForm
    success_url = reverse_lazy("cms_web:paginas")


class PaginaUpdate(CmsUpdateView):
    model = Pagina
    form_class = PaginaForm
    success_url = reverse_lazy("cms_web:paginas")


class PaginaDelete(CmsDeleteView):
    model = Pagina
    success_url = reverse_lazy("cms_web:paginas")


class ServicioList(CmsListView):
    model = Servicio
    create_url_name = "cms_web:servicio_nuevo"


class ServicioCreate(CmsCreateView):
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy("cms_web:servicios")


class ServicioUpdate(CmsUpdateView):
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy("cms_web:servicios")


class ServicioDelete(CmsDeleteView):
    model = Servicio
    success_url = reverse_lazy("cms_web:servicios")


class ProyectoList(CmsListView):
    model = Proyecto
    create_url_name = "cms_web:proyecto_nuevo"


class ProyectoCreate(CmsCreateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy("cms_web:proyectos")


class ProyectoUpdate(CmsUpdateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy("cms_web:proyectos")


class ProyectoDelete(CmsDeleteView):
    model = Proyecto
    success_url = reverse_lazy("cms_web:proyectos")


class ProyectoImagenList(CmsListView):
    model = ProyectoImagen
    create_url_name = "cms_web:proyecto_imagen_nueva"


class ProyectoImagenCreate(CmsCreateView):
    model = ProyectoImagen
    form_class = ProyectoImagenForm
    success_url = reverse_lazy("cms_web:proyecto_imagenes")


class ProyectoImagenUpdate(CmsUpdateView):
    model = ProyectoImagen
    form_class = ProyectoImagenForm
    success_url = reverse_lazy("cms_web:proyecto_imagenes")


class ProyectoImagenDelete(CmsDeleteView):
    model = ProyectoImagen
    success_url = reverse_lazy("cms_web:proyecto_imagenes")


class TestimonioList(CmsListView):
    model = Testimonio
    create_url_name = "cms_web:testimonio_nuevo"


class TestimonioCreate(CmsCreateView):
    model = Testimonio
    form_class = TestimonioForm
    success_url = reverse_lazy("cms_web:testimonios")


class TestimonioUpdate(CmsUpdateView):
    model = Testimonio
    form_class = TestimonioForm
    success_url = reverse_lazy("cms_web:testimonios")


class TestimonioDelete(CmsDeleteView):
    model = Testimonio
    success_url = reverse_lazy("cms_web:testimonios")


class AliadoList(CmsListView):
    model = AliadoLogo
    create_url_name = "cms_web:aliado_nuevo"


class AliadoCreate(CmsCreateView):
    model = AliadoLogo
    form_class = AliadoLogoForm
    success_url = reverse_lazy("cms_web:aliados")


class AliadoUpdate(CmsUpdateView):
    model = AliadoLogo
    form_class = AliadoLogoForm
    success_url = reverse_lazy("cms_web:aliados")


class AliadoDelete(CmsDeleteView):
    model = AliadoLogo
    success_url = reverse_lazy("cms_web:aliados")


class FaqList(CmsListView):
    model = PreguntaFrecuente
    create_url_name = "cms_web:faq_nueva"


class FaqCreate(CmsCreateView):
    model = PreguntaFrecuente
    form_class = PreguntaFrecuenteForm
    success_url = reverse_lazy("cms_web:faqs")


class FaqUpdate(CmsUpdateView):
    model = PreguntaFrecuente
    form_class = PreguntaFrecuenteForm
    success_url = reverse_lazy("cms_web:faqs")


class FaqDelete(CmsDeleteView):
    model = PreguntaFrecuente
    success_url = reverse_lazy("cms_web:faqs")


class BloqueList(CmsListView):
    model = BloqueContenido
    create_url_name = "cms_web:bloque_nuevo"


class BloqueCreate(CmsCreateView):
    model = BloqueContenido
    form_class = BloqueContenidoForm
    success_url = reverse_lazy("cms_web:bloques")


class BloqueUpdate(CmsUpdateView):
    model = BloqueContenido
    form_class = BloqueContenidoForm
    success_url = reverse_lazy("cms_web:bloques")


class BloqueDelete(CmsDeleteView):
    model = BloqueContenido
    success_url = reverse_lazy("cms_web:bloques")


class MensajeList(CmsListView):
    model = MensajeContacto


@login_required(login_url="cms_web:login")
@cms_required
def mensaje_detalle(request, pk):
    mensaje = get_object_or_404(MensajeContacto, pk=pk)
    if not mensaje.leido:
        mensaje.leido = True
        mensaje.save(update_fields=["leido"])
    form = MensajeContactoEstadoForm(request.POST or None, instance=mensaje)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Estado de mensaje actualizado.")
        return redirect("cms_web:mensajes")
    return render(request, "cms_web/mensaje_detalle.html", {"mensaje": mensaje, "form": form})
