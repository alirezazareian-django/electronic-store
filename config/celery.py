# project_name/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیم محیط Django برای Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

app = Celery('products')

# بارگذاری تنظیمات Celery از فایل settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# کشف و ثبت task ها
app.autodiscover_tasks()
