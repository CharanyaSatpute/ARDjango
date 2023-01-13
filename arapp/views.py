import json

from django.shortcuts import render, redirect
from .models import Admin, Student, Words
from .forms import WordsForm, AdminForm, StudentForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'arapp/index.html')

def student(request):
    return render(request, 'arapp/student.html')

def admin(request):
    return render(request, 'arapp/admin.html')

def argame(request):
    return render(request, 'arapp/argame.html')

def addWords(request):
    return render(request, 'arapp/addWords.html')

def choose(request):
    return render(request, 'arapp/choose.html')


def admin_view(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AdminForm()
    return render(request, 'arapp/admin.html', {'form': form})

def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'arapp/student.html', {'form': form})

def words_view(request):
    if request.method == 'POST':
        form = WordsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WordsForm()
    return render(request, 'arapp/addWords.html', {'form': form})










