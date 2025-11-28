from pathlib import Path
import os
from decouple import config # <-- NEW: Import config
import datetime # <-- NEW: Using standard library for time logic

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# CORE SETTINGS
# -----------------------------
# Load SECRET_KEY from .env file, with a secure fallback
SECRET_KEY = config(
    "DJANGO_SECRET_KEY", 
    default="django-insecure-1234567890-your-secret-key"
)

# Load DEBUG from .env file
DEBUG = True 

# --- OPENAI API KEY (ADDED HERE) ---
OPENAI_API_KEY = config("OPENAI_API_KEY", default=None) 

# --- ALLOWED HOSTS (UPDATED FOR PRODUCTION/VERCEL) ---
ALLOWED_HOSTS = [ '3.110.26.126', '3.108.252.40',  'localhost', '127.0.0.1', ]

CSRF_TRUSTED_ORIGINS = [
    'http://3.110.26.126',
    'http://3.108.252.40:8000',
    'http://localhost:3000',
    'http://127.0.0.1:8000',
]

# -----------------------------
# INSTALLED APPS
# -----------------------------
INSTALLED_APPS = [
    'jazzmin',  # <--- JAZZMIN Added at the TOP

    # 'admin_interface', # <--- Commented out to avoid conflict
    # 'colorfield',      # <--- Commented out to avoid conflict

    'django.contrib.admin',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "rest_framework",
    "corsheaders",
    "adminsortable2",

    # custom apps
    "core",
    "blog",
    "cms",
    "contact",
    "leads",
    "theme",
    "pages",
    "careers",
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must be at the top
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "backend.middleware.ConditionalCoopMiddleware",
]

ROOT_URLCONF = "backend.urls"

# -----------------------------
# TEMPLATES
# -----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # --- NEW: Profile Image Context Processor Registration ---
                "backend.context_processors.user_avatar_context", 
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# -----------------------------
# DATABASE (SQLite)
# -----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -----------------------------
# PASSWORD VALIDATION
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------
# INTERNATIONALIZATION
# -----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC" # <-- Keep as UTC for standard practice
USE_I18N = True
USE_TZ = True

# -----------------------------
# STATIC & MEDIA FILES
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") 
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# -----------------------------
# DJANGO REST FRAMEWORK
# -----------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ]
}

# -----------------------------
# CORS SETTINGS
# -----------------------------
CORS_ALLOWED_ORIGINS = [
    "http://3.110.26.126:3000",
]
CORS_ALLOW_CREDENTIALS = True

# -----------------------------
# DEFAULT PRIMARY KEY
# -----------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ==========================================
#  DYNAMIC THEME LOGIC (6 AM - 6 PM IST)
#  (Uses standard datetime to avoid 'pytz' error)
# ==========================================

# 1. Calculate current time adjusted to IST (UTC + 5:30)
IST_OFFSET = datetime.timedelta(hours=5, minutes=30)
now_utc = datetime.datetime.utcnow()
now_ist = now_utc + IST_OFFSET

# 2. Determine if it is day time (6 AM to 6 PM IST)
# Note: Hours are compared in 24-hour format (6=6AM, 18=6PM)
is_daytime = 6 <= now_ist.hour < 18

if is_daytime:
    # --- LIGHT MODE CONFIGURATION (6 AM - 6 PM IST) ---
    DYNAMIC_THEME_TWEAKS = {
        "theme": "lux",                     
        "dark_mode_theme": None,            
        "brand_colour": "navbar-light",     
        "navbar": "navbar-white",           
        "sidebar": "sidebar-light-primary", 
        "accent": "accent-info",            
    }
else:
    # --- DARK MODE CONFIGURATION (6 PM - 6 AM IST) ---
    DYNAMIC_THEME_TWEAKS = {
        "theme": "darkly",                  
        "dark_mode_theme": None,            
        "brand_colour": "navbar-dark",      
        "navbar": "navbar-dark",            
        "sidebar": "sidebar-dark-indigo",   
        "accent": "accent-warning",         
    }


# ==========================================
#  JAZZMIN SETTINGS (Modern Admin UI)
# ==========================================

JAZZMIN_SETTINGS = {
    # Branding
    "site_title": "XpertAI Admin",
    "site_header": "XpertAI Global",
    "site_brand": "XpertAI CMS",
    "welcome_sign": "Welcome to XpertAI Global Headquarters",
    "copyright": "XpertAI Global Ltd",
    "search_model": ["auth.User", "cms.Service"],

    # UI Customization
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Website", "url": "http://3.110.26.126:3000", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # Icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "cms.HomeContent": "fas fa-home",
        "cms.AboutContent": "fas fa-info-circle",
        "cms.ServicesContent": "fas fa-briefcase",
        "cms.ContactContent": "fas fa-envelope",
        "cms.CareersContent": "fas fa-user-tie",
        "cms.ResourcesContent": "fas fa-book",
        "cms.Page": "fas fa-file-alt",
        "cms.Service": "fas fa-cogs",
        "cms.CaseStudy": "fas fa-chart-line",
        "cms.Resource": "fas fa-download",
        "careers.JobOpening": "fas fa-briefcase",
        "careers.JobApplication": "fas fa-file-signature",
        "leads.Lead": "fas fa-bullhorn",
        "leads.WebsiteLead": "fas fa-globe",
        "leads.ChatbotLead": "fas fa-robot",
        "contact.ContactMessage": "fas fa-paper-plane",
        "blog.BlogPost": "fas fa-newspaper",
    },
    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "use_google_fonts_cdn": True,
    "show_ui_builder": True,
    
    # --- USER AVATAR CONFIGURATION ---
    # Jazzmin ko batana ki context se 'user_avatar' variable uthana hai
    "user_avatar": "user_avatar", 
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    # OVERWRITE BASE TWEAKS WITH DYNAMIC THEME SETTINGS
    **DYNAMIC_THEME_TWEAKS
}
