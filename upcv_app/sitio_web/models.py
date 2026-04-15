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
    nombre_sitio = models.CharField(max_length=150, default="Tecnologías de Guatemala")
    slogan = models.CharField(max_length=220, blank=True)
    descripcion_corta = models.CharField(max_length=260, blank=True)
    descripcion_larga = models.TextField(blank=True)
    logo = models.ImageField(upload_to="sitio_web/config/", blank=True, null=True)
    favicon = models.ImageField(upload_to="sitio_web/config/", blank=True, null=True)
    email = models.EmailField(blank=True)
    telefono_1 = models.CharField(max_length=60, blank=True)
    telefono_2 = models.CharField(max_length=60, blank=True)
    whatsapp = models.URLField(blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    horario = models.CharField(max_length=255, blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    footer_text = models.CharField(max_length=255, blank=True)
    enlace_mapa = models.URLField(blank=True)
    mapa_embed = models.TextField(blank=True)
    color_primario = models.CharField(max_length=20, default="#7366ff")
    color_secundario = models.CharField(max_length=20, default="#16c7f9")

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
    boton_texto = models.CharField(max_length=60, blank=True)
    boton_url = models.CharField(max_length=255, blank=True)
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
    publicada = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)
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
    imagen = models.ImageField(upload_to="sitio_web/servicios/", blank=True, null=True)
    icono = models.CharField(max_length=60, blank=True, help_text="Clase de icono (ejemplo: fa fa-cloud)")
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
    destacado = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

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
    titulo_opcional = models.CharField(max_length=120, blank=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden", "id"]

    def __str__(self):
        return self.titulo_opcional or f"Imagen {self.id}"


class Testimonio(BaseTimeModel):
    nombre = models.CharField(max_length=120)
    cargo = models.CharField(max_length=140, blank=True)
    empresa = models.CharField(max_length=140, blank=True)
    mensaje = models.TextField()
    foto = models.ImageField(upload_to="sitio_web/testimonios/", blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]

    def __str__(self):
        return self.nombre


class AliadoLogo(BaseTimeModel):
    nombre = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="sitio_web/aliados/")
    url = models.URLField(blank=True)
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
        ("fortalezas", "Fortalezas"),
        ("soluciones", "Soluciones"),
        ("estadisticas", "Estadísticas"),
        ("cta", "Llamado a la acción"),
    )

    clave = models.CharField(max_length=60, choices=CLAVE_CHOICES)
    titulo = models.CharField(max_length=180)
    subtitulo = models.CharField(max_length=240, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="sitio_web/bloques/", blank=True, null=True)
    icono = models.CharField(max_length=60, blank=True)
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["clave", "orden", "id"]

    def __str__(self):
        return f"{self.get_clave_display()} - {self.titulo}"


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True)
    asunto = models.CharField(max_length=180, blank=True)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"{self.nombre} - {self.email}"
