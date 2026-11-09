
"""
Django settings for customer project.
Cinematic Jazzmin Admin Dashboard
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-change-this-key-for-production'
DEBUG = True
ALLOWED_HOSTS = []

# APPLICATIONS
INSTALLED_APPS = [
    'jazzmin',  # Must be before django.contrib.admin

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'customer.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'customer.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PASSWORD VALIDATION
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

# LANGUAGE AND TIME
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = 'static/'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================
# JAZZMIN ADMIN UI CONFIGURATION
# ==========================================

JAZZMIN_SETTINGS = {

    # BRANDING
    "site_title": "Customer REU Admin",
    "site_header": "Customer REU",
    "site_brand": "CUSTOMER REU",
    "welcome_sign": "Welcome to Customer Management Portal",
    "copyright": "Customer REU Management",

    # LOGIN PAGE
    "login_logo": None,
    "site_logo": None,
    "show_ui_builder": True,
    "show_theme_chooser": True,

    # SEARCH
    "search_model": ["auth.User", "auth.Group"],

    # TOP MENU
    "topmenu_links": [
        {
            "name": "Home",
            "url": "admin:index",
            "icon": "fas fa-home",
        },
    ],

    # SIDEBAR
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # ICONS
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user-circle",
        "auth.Group": "fas fa-users",
    },

    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    # FORMS
    "changeform_format": "horizontal_tabs",

    # CUSTOMIZATION
    "related_modal_active": True,
    "language_chooser": False,
}


# ==========================================
# CINEMATIC DARK UI / THEME
# ==========================================

JAZZMIN_UI_TWEAKS = {

    # CINEMATIC THEME
    "theme": "vapor",
    "default_theme_mode": "dark",

    # NAVBAR
    "navbar": "navbar-dark",
    "brand_colour": "navbar-dark",

    # SIDEBAR
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_flat_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_small_text": False,

    # COLORS
    "accent": "accent-info",
    "primary": "primary",
    "info": "info",
    "success": "success",
    "warning": "warning",
    "danger": "danger",

    # CONTENT
    "body_small_text": False,
    "brand_small_text": False,
    "footer_small_text": False,
    "navbar_small_text": False,

    # BUTTONS
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "success": "btn-success",
        "warning": "btn-warning",
        "danger": "btn-danger",
    },

    # LAYOUT
    "actions_sticky_top": True,
}
