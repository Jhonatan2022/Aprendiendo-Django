from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Nos permite acceder a los archivos de la aplicación desde cualquier parte del sistema
# Nos indica la ruta de los directorios
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Este apartado determinara la clave secreta que se usara para encriptar la información
# Sirve para mejorar la encriptación de los usuarios y contraseñas
# SECRET_KEY = 'django-insecure-9a8e7lb+hvz1rbdy%xc5m8a@wj_%x50)@mdp1cbp71&e5u*-eb'

# Modified SECRET_KEY para que no se muestre en el repositorio de GitHub
SECRET_KEY = "django-insecure-9a8e7lb+hvz1rbdy%xc5m8a@wj_%x50)@mdp1cbp71&e5u*-eb"
# os.environ.get('SECRET_KEY', default='your secret key')
# Ahora podra leer la variable de entorno que nos brinda la nube

# SECURITY WARNING: don't run with debug turned on in production!
# Este apartado determinara si la aplicación se ejecutara en modo desarrollo o producción
DEBUG = True
#'RENDER' not in os.environ # Render no se encuentra en el entorno de producción
# True  # Modo desarrollo (True) / Modo producción (False)


# Este apartado determinara que direcciónes tiene permitido acceder a la aplicación
ALLOWED_HOSTS = []

# RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

# Creamos una condicional para validar si la variable existe o no y agregarla a la lista de ALLOWED_HOSTS
# if RENDER_EXTERNAL_HOSTNAME:
#   ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition
# Django nos permite dividir el proyecto en diferentes aplicaciones
# También este apartado nos permite conectar nuestro proyecto principal con la nueva aplicación
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",  # Nuestro proyecto principal ya reconoce a la carpeta de myapp
]

# Este apartado determinara las aplicaciones que se usaran en el proyecto
# Nos permite procesar determinado tipo de datos en la aplicación
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "mysite.urls"

# Este apartado determinara el motor de plantillas que se usara en el proyecto
# Aunque nos sirve más para el modo de producción de la aplicación
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Este apartado determinara el motor de base de datos que se usara en el proyecto
# Nos indica a que base de datos nos vamos a conectar o estamos conectados
DATABASES = {
    # Instalamos el paquete de mysqlclient para poder usar la base de datos de mysql
    # Cambiamoa a la base de datos mysql
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "3306",
    }
    # Configuración para la base de datos de Postgres
    #'default': dj_database_url.config(
    #   default='postgresql://postgres:postgres@localhost/postgres',
    #  conn_max_age=600,
    # )
    #'default': {
    #  'ENGINE': 'django.db.backends.sqlite3',
    #  'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# Este apartado determinara el lenguaje por defecto
LANGUAGE_CODE = "en-us"

# Este apartado determinara la zona horaria por defecto
TIME_ZONE = "UTC"

# Este apartado determinara si se usara o no la internacionalización
USE_I18N = True

# Este apartado determinara si se usara o no la localización
USE_TZ = True

STATIC_URL = "static/"
# Creamos la ruta para que redirija al usuario a login
LOGIN_URL = "/login"

# Creamos la ruta de las imagenes que se subiran al servidor
MEDIA_ROOT = os.path.join(BASE_DIR, "")

# Indicamos la ruta de las imagenes
MEDIA_URL = "/images/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
