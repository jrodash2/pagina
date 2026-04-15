from django.contrib.auth.decorators import user_passes_test


def can_access_cms(user):
    return bool(user and user.is_authenticated and (user.is_superuser or user.is_staff or user.groups.filter(name__in=["Administrador", "CMS"]).exists()))


cms_required = user_passes_test(can_access_cms, login_url="cms_web:login")
