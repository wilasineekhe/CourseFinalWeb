# settings.py
from pathlib import Path
import os
import dj_database_url  # ✅ ใช้แปลง DATABASE_URL ของ Render

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Media (ใส่ค่าเริ่มต้นให้ไม่ว่าง) ─────────────────────────────
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ── Security / Debug / Hosts ─────────────────────────────────────
# ใช้ env บน Render: DEBUG=false, SECRET_KEY=xxx
DEBUG = os.getenv("DEBUG", "True").lower() == "true"   # local = True, Render = False

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-p%3fz@s957g%0&)cs4nfwekbr4-(aq3alqpdn3)&oy!zt3zvxm",  # อย่าลืมตั้งใน Render
)

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "kaminqq.pythonanywhere.com",
    # 👉 เปลี่ยนด้านล่างเป็นโดเมนจริงของ Render คุณ
    "your-service.onrender.com",
    "your-custom-domain.com",
]

# ถ้าใช้ https บน Render ต้อง trust โดเมนนี้สำหรับ CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://your-service.onrender.com",
    "https://your-custom-domain.com",
]

# ── Installed apps (คงเดิม) ──────────────────────────────────────
INSTALLED_APPS = [
    'app_user.apps.AppUserConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'general_APP',
]

# ── Middleware: เพิ่ม WhiteNoise ใต้ SecurityMiddleware ──────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ ต้องมีสำหรับ static บน Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Training_management_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ✔ ใช้ได้ทั้ง local/Render (ถ้ามีโฟลเดอร์ templates)
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

WSGI_APPLICATION = 'Training_management_project.wsgi.application'

# ── Database: ใช้ dj_database_url เพื่ออ่าน env DATABASE_URL ─────
# local ไม่มี DATABASE_URL → fallback เป็น sqlite (เดิม)
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

# ── Password validators (คงเดิม) ─────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ── i18n / tz (คงเดิม) ───────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Bangkok'
USE_I18N = True
USE_TZ = True

# ── Static files (สำคัญสำหรับ Render + WhiteNoise) ───────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # ✅ ให้ collectstatic มารวมไว้ที่นี่
# ถ้ามีโฟลเดอร์ static ฝั่ง source เอง ให้เปิดบรรทัดนี้:
# STATICFILES_DIRS = [BASE_DIR / "static"]

# เปิด storage ผ่าน WhiteNoise (gzip+manifest)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ── Default PK / Auth redirects ───────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'user_homepage'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = "home"

# ── Email (คงเดิม) ───────────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / "test_inbox"
PASSWORD_RESET_TIMEOUT = 180

# ── Security headers (แนะนำให้เปิดเมื่อ DEBUG=False/บน Render) ──
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Render อยู่หลัง reverse proxy:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
