from django.db import models

# Create your models here.

class Admin(models.Model):
    admin_id = models.CharField(max_length=50, primary_key=True)
    admin_password = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    student_password = models.CharField(max_length=50)

class Words(models.Model):
    subject = models.CharField(max_length=50)
    word = models.CharField(max_length=50)
