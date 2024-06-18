# app/learning_logs/forms.py

# Django and third parties modules
from django import forms

# Locals
from app.learning_logs.models import Topic

class TopicForm(forms.ModelForm):
	
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}


