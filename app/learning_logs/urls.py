# src/app/learning_logs/urls

# Django and third parties modules
from django.urls import path

# Locals
from app.learning_logs import views

# namespace
app_name = "learning_logs"


urlpatterns = [
	# Home page
    path("", views.index, name="index"),
	# Page that shows all topics.
	path('topics/', views.topics, name='topics'),
]