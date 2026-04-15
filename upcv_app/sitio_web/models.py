from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class BaseTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseSEOModel(models.Model):
    meta_title = models.CharField(max_length=160, blank=True)
    meta_description = models.CharField(max_length=320, blank=True)
    meta_image = models.ImageField(upload_to="sitio_web/seo/", blank=True, null=True)

    class Meta:
        abstract = True


class ConfiguracionSitio(BaseTimeModel, BaseSEOModel):
    nombre_sitio = models.CharField(max_length=150, default="AulaPro Tecnología")
    slogan = models.CharField(max_length=220, blank=True)
    logo = models.ImageField(upload_to="sitio_web/config/", blank=True, null=True)
    favicon = models.ImageField(upload_to="sitio_web/config/", blank=True, null=True)
    descripcion = models.TextField(blank=True)
    sobre_nosotros = models.TextField(blank=True)
    mision = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    telefonos = models.CharField(max_length=220, blank=True)
    correo = models.EmailField(blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    whatsapp_url = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    horario = models.CharField(max_length=255, blank=True)
    mapa_url = models.URLField(blank=True)
    footer_text = models.CharField(max_length=255, blank=True)
    color_primario = models.CharField(max_length=20, default="#1f3a93")
    color_secundario = models.CharField(max_length=20, default="#00b4d8")
    mostrar_testimonios = models.BooleanField(default=True)
    mostrar_faqs = models.BooleanField(default=True)
    mostrar_aliados = models.BooleanField(default=True)
    mostrar_estadisticas = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Configuración del sitio"
        verbose_name_plural = "Configuración del sitio"

    def __str__(self):
        return self.nombre_sitio


class HeroSlide(BaseTimeModel):
    titulo = models.CharField(max_length=160)
    subtitulo = models.CharField(max_length=220, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="sitio_web/hero/")
    cta_texto = models.CharField(max_length=60, blank=True)
    cta_url = models.CharField(max_length=255, blank=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]

    def __str__(self):
        return self.titulo


class Pagina(BaseTimeModel, BaseSEOModel):
    titulo = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    resumen = models.CharField(max_length=220, blank=True)
    contenido = models.TextField(blank=True)
    imagen_portada = models.ImageField(upload_to="sitio_web/paginas/", blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activa = models.BooleanField(default=True)
    mostrar_en_menu = models.BooleanField(default=False)

    class Meta:
        ordering = ["orden", "titulo"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("sitio_web:pagina_detalle", kwargs={"slug": self.slug})


class Servicio(BaseTimeModel, BaseSEOModel):
    titulo = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    resumen = models.CharField(max_length=250)
    descripcion = models.TextField()
    icono = models.CharField(max_length=60, blank=True, help_text="Clase de icono (ejemplo: fa fa-cloud)")
    imagen_portada = models.ImageField(upload_to="sitio_web/servicios/", blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)

    class Meta:
        ordering = ["orden", "titulo"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("sitio_web:servicio_detalle", kwargs={"slug": self.slug})


class Proyecto(BaseTimeModel, BaseSEOModel):
    titulo = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    cliente = models.CharField(max_length=140, blank=True)
    categoria = models.CharField(max_length=120, blank=True)
    resumen = models.CharField(max_length=250)
    descripcion = models.TextField()
    imagen_portada = models.ImageField(upload_to="sitio_web/proyectos/", blank=True, null=True)
    enlace_externo = models.URLField(blank=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)

    class Meta:
        ordering = ["orden", "-created_at"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("sitio_web:proyecto_detalle", kwargs={"slug": self.slug})


class ProyectoImagen(BaseTimeModel):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to="sitio_web/proyectos/galeria/")
    titulo = models.CharField(max_length=120, blank=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]

    def __str__(self):
        return self.titulo or f"Imagen {self.id}"


class Testimonio(BaseTimeModel):
    nombre = models.CharField(max_length=120)
    cargo = models.CharField(max_length=140, blank=True)
    empresa = models.CharField(max_length=140, blank=True)
    foto = models.ImageField(upload_to="sitio_web/testimonios/", blank=True, null=True)
    comentario = models.TextField()
    calificacion = models.PositiveSmallIntegerField(default=5)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]

    def __str__(self):
        return self.nombre


class AliadoLogo(BaseTimeModel):
    nombre = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="sitio_web/aliados/")
    sitio_web = models.URLField(blank=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "nombre"]

    def __str__(self):
        return self.nombre


class PreguntaFrecuente(BaseTimeModel):
    pregunta = models.CharField(max_length=220)
    respuesta = models.TextField()
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]

    def __str__(self):
        return self.pregunta


class BloqueContenido(BaseTimeModel):
    CLAVE_CHOICES = (
        ("beneficios", "Beneficios"),
        ("estadisticas", "Estadísticas"),
        ("cta", "Llamado a la acción"),
        ("nosotros_home", "Nosotros en inicio"),
    )

    clave = models.CharField(max_length=60, choices=CLAVE_CHOICES)
    titulo = models.CharField(max_length=180)
    subtitulo = models.CharField(max_length=240, blank=True)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=60, blank=True)
    imagen = models.ImageField(upload_to="sitio_web/bloques/", blank=True, null=True)
    valor_numerico = models.PositiveIntegerField(blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["clave", "orden", "id"]

    def __str__(self):
        return f"{self.get_clave_display()} - {self.titulo}"


class MenuItem(BaseTimeModel):
    titulo = models.CharField(max_length=120)
    url = models.CharField(max_length=255)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]

    def __str__(self):
        return self.titulo


class ContactoLead(BaseTimeModel):
    nombre = models.CharField(max_length=120)
    empresa = models.CharField(max_length=150, blank=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True)
    servicio_interes = models.CharField(max_length=180, blank=True)
    mensaje = models.TextField()
    ip = models.GenericIPAddressField(blank=True, null=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
