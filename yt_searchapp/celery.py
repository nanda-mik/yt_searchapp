from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
import dotenv


dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yt_searchapp.settings')

app = Celery('yt_searchapp')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
