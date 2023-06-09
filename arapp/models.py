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
    name = models.CharField(max_length=50, blank=False)
    admin_id = models.CharField(max_length=50, primary_key=True, blank=False)
    admin_password = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=50, choices=my_choices, blank=False, default=my_choices[1])

class Student(models.Model):
    my_choices = [
        ('select', 'select'),
        ('ENGLISH', 'ENGLISH'),
        ('MATHEMATICS', 'MATHEMATICS'),
        ('BIOLOGY', 'BIOLOGY'),
        ('PHYSICS', 'PHYSICS'),
        ('SOCIAL STUDIES', 'SOCIAL STUDIES')
    ]
    name = models.CharField(max_length=50, blank=False)
    student_id = models.CharField(max_length=50, primary_key=True, blank=False)
    student_password = models.CharField(max_length=50, blank=False)
# score table
# studentid - foreign key
# auto primary key
# score numeric field
# timetamp

class Score(models.Model):
    my_choices = [
        ('select', 'select'),
        ('ENGLISH', 'ENGLISH'),
        ('MATHEMATICS', 'MATHEMATICS'),
        ('BIOLOGY', 'BIOLOGY'),
        ('PHYSICS', 'PHYSICS'),
        ('SOCIAL STUDIES', 'SOCIAL STUDIES')
    ]
    id = models.BigAutoField(primary_key=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, choices=my_choices, blank=False, default=my_choices[1])
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Words(models.Model):
    subject = models.CharField(max_length=50, blank=False)
    word = models.CharField(max_length=50, blank=False)

