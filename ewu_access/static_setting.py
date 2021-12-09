import os 
from django.conf import settings
STATIC_URL = '/static/'
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR,'media')
STATIC_ROOT = os.path.join(settings.BASE_DIR,'static','static_root','static')

STATICFILES_DIRS = [

    os.path.join(settings.BASE_DIR, "static","static_dir"),

]