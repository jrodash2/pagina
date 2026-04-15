from django.contrib import admin

from .models import (
    AliadoLogo,
    BloqueContenido,
    ConfiguracionSitio,
    ContactoLead,
    HeroSlide,
    MenuItem,
    Pagina,
    PreguntaFrecuente,
    Proyecto,
    ProyectoImagen,
    Servicio,
    Testimonio,
)


class ProyectoImagenInline(admin.TabularInline):
    model = ProyectoImagen
    extra = 1


@admin.register(ConfiguracionSitio)
class ConfiguracionSitioAdmin(admin.ModelAdmin):
    list_display = ("nombre_sitio", "correo", "telefonos", "mostrar_testimonios", "mostrar_faqs")


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("titulo", "orden", "activo")
    list_filter = ("activo",)
    search_fields = ("titulo", "subtitulo")
    ordering = ("orden",)


@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "mostrar_en_menu", "activa", "orden")
    search_fields = ("titulo", "slug", "resumen")
    list_filter = ("activa", "mostrar_en_menu")
    prepopulated_fields = {"slug": ("titulo",)}
    ordering = ("orden", "titulo")


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "destacado", "activo", "orden")
    search_fields = ("titulo", "descripcion", "resumen")
    list_filter = ("activo", "destacado")
    prepopulated_fields = {"slug": ("titulo",)}
    ordering = ("orden", "titulo")


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "categoria", "cliente", "destacado", "activo", "orden")
    search_fields = ("titulo", "categoria", "cliente", "descripcion")
    list_filter = ("activo", "destacado", "categoria")
    prepopulated_fields = {"slug": ("titulo",)}
    ordering = ("orden", "-created_at")
    inlines = [ProyectoImagenInline]


@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cargo", "empresa", "calificacion", "destacado", "activo", "orden")
    search_fields = ("nombre", "cargo", "empresa", "comentario")
    list_filter = ("activo", "destacado")
    ordering = ("orden",)


@admin.register(AliadoLogo)
class AliadoLogoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo", "orden")
    search_fields = ("nombre",)
    list_filter = ("activo",)
    ordering = ("orden", "nombre")


@admin.register(PreguntaFrecuente)
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    list_display = ("pregunta", "activo", "orden")
    search_fields = ("pregunta", "respuesta")
    list_filter = ("activo",)
    ordering = ("orden",)


@admin.register(BloqueContenido)
class BloqueContenidoAdmin(admin.ModelAdmin):
    list_display = ("clave", "titulo", "valor_numerico", "activo", "orden")
    list_filter = ("clave", "activo")
    search_fields = ("titulo", "subtitulo", "descripcion")
    ordering = ("clave", "orden")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "url", "activo", "orden")
    list_filter = ("activo",)
    search_fields = ("titulo", "url")
    ordering = ("orden",)


@admin.register(ContactoLead)
class ContactoLeadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "telefono", "servicio_interes", "leido", "created_at")
    list_filter = ("leido", "created_at")
    search_fields = ("nombre", "correo", "empresa", "mensaje")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at", "ip")
