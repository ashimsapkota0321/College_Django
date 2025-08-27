from django import forms
from .models import Student


class BioModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'address', 'age', 'bio_summary', 'phone_number', 'education']