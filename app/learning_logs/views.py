# src/app/learning_logs/views

# Django and third parties modules
from django.shortcuts import render

# Locals
from app.learning_logs.models import Topic


# Create your views here.

def index(request):
	"""The home page for Learning Log."""
	return render(request, 'learning_logs/index.html')


def topics(request):
	"""Show all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)