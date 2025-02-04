from django import forms
from .models import Software

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'description', 'release_date', 'category', 'user']  # Поля формы
