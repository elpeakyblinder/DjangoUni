import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+@aga+_!e&d0!f)l!i0wtp%cu!k3@w-5m68gnrv_4u(jf)fug6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
    'registros.apps.RegistrosConfig',
    'cursos.apps.CursosConfig',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prueba.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'prueba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Prueba',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : '3307',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City' # También es buena idea ajustar la zona horaria
USE_I18N = True
USE_L10N = True
USE_TZ = False


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
    'actividad_editor': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ],
    }
}

JAZZMIN_SETTINGS = {
    # Título que aparece en la pestaña del navegador y en la página de login
    "site_title": "Panel de Administración",

    # Título en la parte superior izquierda de la barra de navegación
    "site_header": "Mi Proyecto",

    # Logo para la página de login (puedes poner la ruta a tu logo)
    # ej: "images/logo.png" (debe estar en tu carpeta static)
    "login_logo": None,

    # Texto del "copyright" en el pie de página
    "copyright": "Mi Proyecto Ltd.",

    # --- AJUSTES DE LA INTERFAZ (UI) ---
    # Aquí es donde aplicamos tu paleta de colores neuromórfica
    "ui_tweaks": {
        # Usamos un tema general claro para el fondo, como en tu paleta (--bg-primary)
        "theme": "default",

        # Hacemos que la barra de navegación use tu color de marca azul (--blue-500)
        "navbar": "navbar-dark navbar-primary",

        # Texto claro para que contraste con la barra de navegación oscura
        "navbar_text": "text-light",
        "navbar_links_text": "text-light",

        # La barra lateral también usará el color de marca azul
        "sidebar": "sidebar-dark-primary",
        "sidebar_text": "text-light",
        "sidebar_links_text": "text-light",
        "sidebar_brand_text": "text-light",
        "sidebar_nav_child_indent": True,
        "sidebar_nav_compact_style": True,

        # Clases para los botones, usando tus colores de estado
        "button_classes": {
            "primary": "btn-primary",    # Azul
            "secondary": "btn-secondary",  # Gris
            "info": "btn-info",          # Azul claro
            "warning": "btn-warning",      # Amarillo
            "danger": "btn-danger",      # Rojo
            "success": "btn-success"     # Verde
        },

        # Esquinas redondeadas para un look más suave, como en el neuromorfismo
        "rounded_corners": True,
        
        # Ocultar el selector de temas si no quieres que los usuarios lo cambien
        "show_ui_builder": False
    },
    
    # --- ICONOS ---
    # Usamos FontAwesome 5 para los iconos
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "registros.alumnos": "fas fa-user-graduate",
        "registros.comentario": "fas fa-comments",
        "registros.comentariocontacto": "fas fa-envelope-open-text",
        "cursos.curso": "fas fa-book-open",
        "cursos.actividad": "fas fa-tasks",
    },
}