from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping_dojo.settings')
app = Celery('scraping_dojo')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.CELERYBEAT_SCHEDULE = {
    'add-every-10-seconds': {
        'task': 'recurrencia_app.tasks.add',
        'schedule': timedelta(seconds=10),
        # 'args': ()
    },
}

