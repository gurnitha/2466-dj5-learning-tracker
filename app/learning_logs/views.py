# src/app/learning_logs/views

# Django and third parties modules
from django.shortcuts import render

# Create your views here.

def index(request):
	"""The home page for Learning Log."""
	return render(request, 'learning_logs/base.html')