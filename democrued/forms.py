from .models import task
from django.forms import ModelForm
from django import forms

class taskForm(ModelForm):
	class Meta:
		model = task
		fields = '__all__'