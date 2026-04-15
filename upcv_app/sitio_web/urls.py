from django.urls import path

from . import views

app_name = "sitio_web"

urlpatterns = [
    path("", views.home, name="home"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("servicios/", views.servicios, name="servicios"),
    path("servicios/<slug:slug>/", views.servicio_detalle, name="servicio_detalle"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("proyectos/<slug:slug>/", views.proyecto_detalle, name="proyecto_detalle"),
    path("contacto/", views.contacto, name="contacto"),
    path("paginas/<slug:slug>/", views.pagina_detalle, name="pagina_detalle"),
]
