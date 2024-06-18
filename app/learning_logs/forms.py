# app/learning_logs/forms.py

# Django and third parties modules
from django import forms

# Locals
from app.learning_logs.models import Topic, Entry

class TopicForm(forms.ModelForm):
	
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}