from django import forms
from .models import Admin, Student, Words

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        my_choices = [
            ('select', 'select'),
            ('ENGLISH', 'ENGLISH'),
            ('MATHEMATICS', 'MATHEMATICS'),
            ('BIOLOGY', 'BIOLOGY'),
            ('PHYSICS', 'PHYSICS'),
            ('SOCIAL STUDIES', 'SOCIAL STUDIES')
        ]
        fields = ['admin_id', 'admin_password', 'subject']
        widgets = {
            'admin_id': forms.TextInput(attrs={'required': True}),
            'admin_password': forms.TextInput(attrs={'required': True}),
            'subject': forms.Select(attrs={'required': True}, choices=my_choices)
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'student_password']
        widgets = {
            'student_id': forms.TextInput(attrs={'required': True}),
            'student_password': forms.TextInput(attrs={'required': True}),
        }

class WordsForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = ['subject', 'word']
        widgets = {
            'subject': forms.TextInput(attrs={'required': True}),
            'word': forms.TextInput(attrs={'required': True}),
        }
