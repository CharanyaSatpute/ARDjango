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



def student_page(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_password = request.POST.get('password')
        st = Student(student_id=student_id, student_password=student_password)
        st.save()
    return render(request, "student.html")

def my_view(request):
    data=Words.word.all()
    data_list= json.dumps(list(data))
    return render(request, 'threeGameAR.js', {'data_list': data_list})









