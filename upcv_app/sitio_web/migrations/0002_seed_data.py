from django.db import migrations


def seed_data(apps, schema_editor):
    ConfiguracionSitio = apps.get_model('sitio_web', 'ConfiguracionSitio')
    Servicio = apps.get_model('sitio_web', 'Servicio')
    Proyecto = apps.get_model('sitio_web', 'Proyecto')
    Testimonio = apps.get_model('sitio_web', 'Testimonio')
    PreguntaFrecuente = apps.get_model('sitio_web', 'PreguntaFrecuente')
    BloqueContenido = apps.get_model('sitio_web', 'BloqueContenido')
    Pagina = apps.get_model('sitio_web', 'Pagina')
    MenuItem = apps.get_model('sitio_web', 'MenuItem')

    if not ConfiguracionSitio.objects.exists():
        ConfiguracionSitio.objects.create(
            nombre_sitio='AulaPro Tecnología',
            slogan='Modernizamos operaciones empresariales con soluciones digitales integrales',
            descripcion='Servicios de tecnología corporativa: infraestructura de red, desarrollo, cloud, ciberseguridad y educación virtual.',
            sobre_nosotros='Somos una firma tecnológica enfocada en transformación digital para empresas e instituciones.',
            mision='Diseñar e implementar soluciones tecnológicas sostenibles y escalables.',
            vision='Ser aliado estratégico líder en innovación tecnológica empresarial en Guatemala.',
            telefonos='+502 2222-3344 / +502 5555-8899',
            correo='comercial@aulaprotech.gt',
            direccion='Ciudad de Guatemala, Guatemala',
            whatsapp_url='https://wa.me/50255558899',
            horario='Lun-Vie 8:00 a 18:00',
            mapa_url='https://maps.google.com/',
            footer_text='© AulaPro Tecnología. Transformación digital para empresas.',
        )

    servicios = [
        ('Infraestructura de redes', 'infraestructura-redes', 'Diseño y despliegue de redes empresariales seguras y escalables.', 'Implementamos cableado estructurado, switching, wireless corporativo y monitoreo proactivo de redes.', 'fa fa-sitemap'),
        ('Desarrollo web corporativo', 'desarrollo-web-corporativo', 'Sitios web, portales y aplicaciones empresariales de alto desempeño.', 'Construimos plataformas modernas con enfoque comercial, seguridad y analítica para crecimiento digital.', 'fa fa-code'),
        ('Educación virtual y LMS', 'educacion-virtual-lms', 'Plataformas de aprendizaje online y capacitación híbrida.', 'Diseñamos ecosistemas educativos con gestión académica, aulas virtuales y seguimiento de desempeño.', 'fa fa-graduation-cap'),
        ('Soluciones cloud y productividad', 'soluciones-cloud-productividad', 'Migración a nube, colaboración y continuidad operativa.', 'Adoptamos soluciones cloud para mejorar productividad, respaldo de datos y trabajo remoto seguro.', 'fa fa-cloud'),
        ('Ciberseguridad y continuidad', 'ciberseguridad-continuidad', 'Estrategias de seguridad, respaldo y recuperación.', 'Fortalecemos políticas de ciberseguridad, backups automatizados y continuidad del negocio.', 'fa fa-shield'),
    ]
    for idx, (titulo, slug, resumen, descripcion, icono) in enumerate(servicios, start=1):
        Servicio.objects.get_or_create(
            slug=slug,
            defaults={
                'titulo': titulo,
                'resumen': resumen,
                'descripcion': descripcion,
                'icono': icono,
                'orden': idx,
                'activo': True,
                'destacado': True,
            },
        )

    proyectos = [
        ('Modernización de campus educativo', 'modernizacion-campus-educativo', 'Institución Educativa', 'Infraestructura', 'Renovación completa de conectividad inalámbrica y administración centralizada.'),
        ('Portal corporativo de ventas', 'portal-corporativo-ventas', 'Empresa de servicios', 'Desarrollo web', 'Implementación de portal comercial con formularios inteligentes y CRM.'),
        ('Migración a nube híbrida', 'migracion-nube-hibrida', 'Grupo empresarial', 'Cloud', 'Consolidación de servidores, backups y colaboración digital en entorno híbrido.'),
    ]
    for idx, (titulo, slug, cliente, categoria, resumen) in enumerate(proyectos, start=1):
        Proyecto.objects.get_or_create(
            slug=slug,
            defaults={
                'titulo': titulo,
                'cliente': cliente,
                'categoria': categoria,
                'resumen': resumen,
                'descripcion': resumen,
                'orden': idx,
                'activo': True,
                'destacado': True,
            },
        )

    for idx, data in enumerate([
        ('Carla Mejía', 'Gerente General', 'Grupo Innovar', 'El equipo implementó una solución robusta y elevó nuestra productividad operacional.'),
        ('Luis Arévalo', 'Director TI', 'Colegio Digital', 'Logramos estabilidad de red, plataforma educativa y soporte continuo en tiempo récord.'),
    ], start=1):
        Testimonio.objects.get_or_create(nombre=data[0], defaults={'cargo': data[1], 'empresa': data[2], 'comentario': data[3], 'orden': idx, 'activo': True, 'destacado': True})

    for idx, (pregunta, respuesta) in enumerate([
        ('¿Atienden proyectos fuera de Ciudad de Guatemala?', 'Sí, trabajamos en todo el país con despliegues presenciales y soporte remoto.'),
        ('¿Pueden administrar el mantenimiento continuo?', 'Sí. Ofrecemos planes mensuales de soporte, monitoreo y mejora continua.'),
        ('¿Qué tiempo toma iniciar un proyecto?', 'Normalmente entre 3 y 10 días hábiles según alcance y disponibilidad técnica.'),
    ], start=1):
        PreguntaFrecuente.objects.get_or_create(pregunta=pregunta, defaults={'respuesta': respuesta, 'orden': idx, 'activo': True})

    bloques = [
        ('beneficios', 'Diagnóstico especializado', 'Identificamos brechas tecnológicas y priorizamos acciones de alto impacto.', 'fa fa-search', None),
        ('beneficios', 'Implementación end-to-end', 'Desde diseño hasta operación y soporte continuo.', 'fa fa-cogs', None),
        ('beneficios', 'Equipo multidisciplinario', 'Consultores, desarrolladores e ingenieros de infraestructura.', 'fa fa-users', None),
        ('beneficios', 'Escalabilidad garantizada', 'Soluciones listas para crecer con tu negocio.', 'fa fa-line-chart', None),
        ('estadisticas', 'Proyectos completados', '', 'fa fa-briefcase', 180),
        ('estadisticas', 'Clientes activos', '', 'fa fa-building', 120),
        ('estadisticas', 'Años de experiencia', '', 'fa fa-clock-o', 12),
        ('estadisticas', 'Especialistas técnicos', '', 'fa fa-user-secret', 35),
        ('cta', 'Impulsa tu transformación digital', 'Agenda una consultoría para diseñar tu hoja de ruta tecnológica.', 'fa fa-bullhorn', None),
    ]
    for idx, (clave, titulo, descripcion, icono, valor) in enumerate(bloques, start=1):
        BloqueContenido.objects.get_or_create(clave=clave, titulo=titulo, defaults={'descripcion': descripcion, 'icono': icono, 'valor_numerico': valor, 'orden': idx, 'activo': True})

    Pagina.objects.get_or_create(slug='politica-privacidad', defaults={
        'titulo': 'Política de Privacidad',
        'resumen': 'Compromiso de protección de datos y uso responsable de la información.',
        'contenido': 'Administramos los datos de contacto para fines de seguimiento comercial y soporte.',
        'mostrar_en_menu': True,
        'activa': True,
        'orden': 100,
    })

    MenuItem.objects.get_or_create(titulo='Blog', defaults={'url': '#', 'orden': 90, 'activo': True})


def reverse_seed(apps, schema_editor):
    ConfiguracionSitio = apps.get_model('sitio_web', 'ConfiguracionSitio')
    if ConfiguracionSitio.objects.filter(nombre_sitio='AulaPro Tecnología').exists():
        apps.get_model('sitio_web', 'MenuItem').objects.filter(titulo='Blog').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed),
    ]
