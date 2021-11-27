from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title','content', 'is_published', 'category']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'row': 5}),
			'category': forms.Select(attrs={'class': 'form-control'}),
		}
	def clean_title(self):
		title = self.cleaned_data['title']
		if re.match(r'\d', title):
			raise ValidationError('Название не должно начинаться с цифры')
		return title