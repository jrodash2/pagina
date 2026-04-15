from django.db.utils import OperationalError, ProgrammingError

from .models import ConfiguracionSitio, MenuItem


def sitio_context(request):
    try:
        config = ConfiguracionSitio.objects.order_by("id").first()
        menu_items = MenuItem.objects.filter(activo=True)
    except (OperationalError, ProgrammingError):
        config = None
        menu_items = []

    return {
        "sitio_config": config,
        "sitio_menu_items": menu_items,
    }
