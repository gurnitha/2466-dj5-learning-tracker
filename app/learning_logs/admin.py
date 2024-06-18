# src/app/learning_logs/admin.py

# Django and third parties modules
from django.contrib import admin

# Locals
from app.learning_logs.models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)