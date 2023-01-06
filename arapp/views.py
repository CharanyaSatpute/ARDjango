from django.shortcuts import render
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

