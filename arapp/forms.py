from django import forms
from arapp.models import Admin, Student, Words

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
        fields = '__all__'
        widgets = {
            'admin_id': forms.TextInput(attrs={'required': True, "class": "control-label"}),
            'admin_password': forms.TextInput(attrs={'required': True, "class": "control-label"}),
            'subject': forms.Select(attrs={'required': True, "class": "control-label"}, choices=my_choices),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        my_choices = [
            ('select', 'select'),
            ('ENGLISH', 'ENGLISH'),
            ('MATHEMATICS', 'MATHEMATICS'),
            ('BIOLOGY', 'BIOLOGY'),
            ('PHYSICS', 'PHYSICS'),
            ('SOCIAL STUDIES', 'SOCIAL STUDIES')
        ]
        fields = '__all__'
        widgets = {
            'student_id': forms.TextInput(attrs={'required': True, "class": "control-label"}),
            'student_password': forms.TextInput(attrs={'required': True, "class": "control-label"}),
            'subject': forms.Select(attrs={'required': True, "class": "control-label"}, choices=my_choices),
        }

class WordsForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(attrs={'required': True, "class": "control-label"}),
            'word': forms.TextInput(attrs={'required': True, "class": "control-label"}),
        }
