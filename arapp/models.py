from django.db import models
# Create your models here.

class Admin(models.Model):
    my_choices = [
        ('select', 'select'),
        ('ENGLISH', 'ENGLISH'),
        ('MATHEMATICS', 'MATHEMATICS'),
        ('BIOLOGY', 'BIOLOGY'),
        ('PHYSICS', 'PHYSICS'),
        ('SOCIAL STUDIES', 'SOCIAL STUDIES')
    ]
    admin_id = models.CharField(max_length=50, primary_key=True, blank=False)
    admin_password = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=50, choices=my_choices, blank=False)

class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True, blank=False)
    student_password = models.CharField(max_length=50, blank=False)

class Words(models.Model):
    subject = models.CharField(max_length=50, blank=False)
    word = models.CharField(max_length=50, blank=False)
