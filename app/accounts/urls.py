# src/app/learning_logs/urls.py

# Django and third parties modules
from django.urls import path, include

# Locals
from app.accounts import views

# namespace
app_name = "accounts"


urlpatterns = [
	# Include default auth urls.
	path('', include('django.contrib.auth.urls')),
	# Registration page.
 	path('register/', views.register, name='register'),
]