from django.db import migrations


def seed_data(apps, schema_editor):
    ConfiguracionSitio = apps.get_model('sitio_web', 'ConfiguracionSitio')
    Servicio = apps.get_model('sitio_web', 'Servicio')
    Proyecto = apps.get_model('sitio_web', 'Proyecto')
    Testimonio = apps.get_model('sitio_web', 'Testimonio')
    PreguntaFrecuente = apps.get_model('sitio_web', 'PreguntaFrecuente')
    BloqueContenido = apps.get_model('sitio_web', 'BloqueContenido')
    Pagina = apps.get_model('sitio_web', 'Pagina')

    if not ConfiguracionSitio.objects.exists():
        ConfiguracionSitio.objects.create(
            nombre_sitio='Tecnologías de Guatemala',
            slogan='Innovación tecnológica para modernizar empresas e instituciones',
            descripcion_corta='Infraestructura de redes, desarrollo web, software, soporte, nube y productividad.',
            descripcion_larga='Somos un equipo especializado en transformación digital, modernización tecnológica y soluciones empresariales de alto valor.',
            email='info@tecnologiasdeguatemala.com',
            telefono_1='+502 2220-1111',
            telefono_2='+502 3030-2222',
            whatsapp='https://wa.me/50230302222',
            direccion='Guatemala, Centroamérica',
            horario='Lunes a viernes 8:00 - 18:00',
            footer_text='© Tecnologías de Guatemala - Soluciones digitales empresariales.',
            enlace_mapa='https://maps.google.com/',
        )

    servicios = [
        ('Servicios de Modernización', 'servicios-modernizacion', 'Roadmap integral de modernización tecnológica y transformación digital.', 'Evaluamos infraestructura, procesos y plataformas para evolucionar operaciones con resultados medibles.', 'fa fa-rocket'),
        ('Infraestructura de Redes', 'infraestructura-redes', 'Diseño e implementación de redes seguras y escalables.', 'Instalación, segmentación, optimización y monitoreo de redes empresariales.', 'fa fa-sitemap'),
        ('Desarrollo Web y Páginas Web', 'desarrollo-web-paginas', 'Presencia digital profesional orientada a conversión comercial.', 'Sitios corporativos, landing pages y portales con arquitectura moderna.', 'fa fa-code'),
        ('Educación Virtual y E-learning', 'educacion-virtual', 'Plataformas y contenidos para formación híbrida o remota.', 'Implementación de LMS, aulas virtuales y recorridos formativos.', 'fa fa-graduation-cap'),
        ('Usuario Inteligente y Productividad', 'usuario-inteligente-productividad', 'Ecosistemas colaborativos con herramientas de productividad.', 'Automatización de tareas, colaboración y adopción digital empresarial.', 'fa fa-lightbulb-o'),
        ('Desarrollo de Software', 'desarrollo-software', 'Aplicaciones a medida para procesos críticos del negocio.', 'Soluciones web y móviles enfocadas en eficiencia y escalabilidad.', 'fa fa-laptop'),
        ('Soporte Técnico', 'soporte-tecnico', 'Soporte preventivo y correctivo para continuidad operativa.', 'Mesa de ayuda, monitoreo y mantenimiento continuo.', 'fa fa-life-ring'),
        ('Nube y Seguridad', 'nube-y-seguridad', 'Servicios cloud, productividad, respaldo y seguridad de la información.', 'Migración, respaldo, ciberseguridad y continuidad para empresas modernas.', 'fa fa-cloud'),
    ]
    for idx, (titulo, slug, resumen, descripcion, icono) in enumerate(servicios, start=1):
        Servicio.objects.get_or_create(slug=slug, defaults={
            'titulo': titulo, 'resumen': resumen, 'descripcion': descripcion, 'icono': icono,
            'orden': idx, 'activo': True, 'destacado': idx <= 6,
        })

    proyectos = [
        ('Implementación de Microsoft 365 y Teams', 'implementacion-microsoft-365-teams', 'Corporativo regional', 'Productividad', 'Adopción completa de colaboración empresarial en la nube.'),
        ('Modernización de red para campus educativo', 'modernizacion-red-campus', 'Institución educativa', 'Redes', 'Actualización integral de red cableada e inalámbrica.'),
        ('Portal web institucional de alto desempeño', 'portal-web-institucional', 'Entidad privada', 'Desarrollo web', 'Nuevo portal público orientado a posicionamiento y conversión.'),
    ]
    for idx, (titulo, slug, cliente, categoria, resumen) in enumerate(proyectos, start=1):
        Proyecto.objects.get_or_create(slug=slug, defaults={
            'titulo': titulo, 'cliente': cliente, 'categoria': categoria, 'resumen': resumen,
            'descripcion': resumen, 'orden': idx, 'activo': True, 'destacado': True,
        })

    for idx, (nombre, cargo, empresa, mensaje) in enumerate([
        ('María López', 'Gerente de Operaciones', 'Grupo Empresarial GT', 'Nos ayudaron a modernizar procesos y elevar nuestra productividad.'),
        ('Carlos Pérez', 'Director de TI', 'Corporación Andina', 'Excelente soporte técnico y soluciones cloud orientadas a resultados.'),
    ], start=1):
        Testimonio.objects.get_or_create(nombre=nombre, defaults={
            'cargo': cargo, 'empresa': empresa, 'mensaje': mensaje, 'orden': idx, 'activo': True,
        })

    for idx, (pregunta, respuesta) in enumerate([
        ('¿Pueden acompañar la transformación digital completa?', 'Sí, iniciamos con diagnóstico, plan de trabajo, implementación y soporte continuo.'),
        ('¿Atienden soporte técnico mensual?', 'Sí, contamos con planes recurrentes de soporte y mejora continua.'),
        ('¿Ofrecen servicios de seguridad y nube?', 'Sí, integramos productividad, seguridad, respaldo y continuidad empresarial.'),
    ], start=1):
        PreguntaFrecuente.objects.get_or_create(pregunta=pregunta, defaults={'respuesta': respuesta, 'orden': idx, 'activo': True})

    bloques = [
        ('fortalezas', 'Equipo especializado', 'Ingeniería, desarrollo y consultoría tecnológica integral.', 'fa fa-users'),
        ('fortalezas', 'Implementación profesional', 'Metodologías ágiles y ejecución por fases.', 'fa fa-cogs'),
        ('soluciones', 'Modernización con servicios en la nube', 'Migración cloud, continuidad y colaboración empresarial.', 'fa fa-cloud'),
        ('soluciones', 'Productividad y seguridad', 'Optimización operativa y protección de activos digitales.', 'fa fa-shield'),
        ('cta', 'Transforma tu empresa hoy', 'Solicita una consultoría y recibe una propuesta técnica.', 'fa fa-bullhorn'),
    ]
    for idx, (clave, titulo, descripcion, icono) in enumerate(bloques, start=1):
        BloqueContenido.objects.get_or_create(clave=clave, titulo=titulo, defaults={'descripcion': descripcion, 'icono': icono, 'orden': idx, 'activo': True})

    Pagina.objects.get_or_create(slug='nosotros-corporativo', defaults={
        'titulo': 'Nosotros',
        'resumen': 'Conoce nuestra experiencia y enfoque de valor empresarial.',
        'contenido': 'Tecnologías de Guatemala acompaña empresas en su evolución digital con soluciones seguras y escalables.',
        'mostrar_en_menu': False,
        'publicada': True,
        'orden': 1,
    })


def reverse_seed(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('sitio_web', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed),
    ]
