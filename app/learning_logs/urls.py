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
	# Detail page for a single topic.
 	path('topics/<int:topic_id>/', views.topic, name='topic'),
 	# Page for adding a new topic.
 	path('new_topic/', views.new_topic, name='new_topic'),
 	
 	# Page for adding a new entry.
 	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]