# src/app/learning_logs/urls

# Django and third parties modules
from django.urls import path

# Locals
from app.learning_logs import views

# namespace
app_name = "learning_logs"

urlpatterns = [
    path("", views.index, name="index"),
]
