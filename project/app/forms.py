from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'telegram_username', 'phone', 'age', 'gender', 'text']
    
        gender = forms.ChoiceField(choices=[('male', 'Erkak'), ('female', 'Ayol')], widget=forms.RadioSelect)