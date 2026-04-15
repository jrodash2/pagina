from django.db.utils import OperationalError, ProgrammingError

from .models import ConfiguracionSitio


def sitio_context(request):
    try:
        config = ConfiguracionSitio.objects.order_by("id").first()
    except (OperationalError, ProgrammingError):
        config = None

    return {
        "sitio_config": config,
        "sitio_menu_items": [],
    }
