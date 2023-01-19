from django.shortcuts import render, HttpResponseRedirect
from arapp.models import Admin, Words, Student

import logging

logger = logging.getLogger("mylogger")

def index(request):
    if request.method == 'POST':
        if request.POST.get('myselection') == "student":
            return HttpResponseRedirect('/students')
        elif request.POST.get('myselection') == "admin":
            return HttpResponseRedirect('/admins')
    return render(request, 'arapp/index.html')

def admins_view(request): #consider changing to teacher
    #logger.info("here")
    #logger.info(request,request.method)
    print ("printed here")
    print(request,request.method)
    if request.method == 'POST':
        print ("POST request")
        admin_id = request.POST.get("admin_id")
        password = request.POST.get("password")
        subject = request.POST.get("subject")
        #ad = Admin(admin_id=admin_id, admin_password=password, subject=subject)
        #ad.save()
        ad = Admin.objects.create(admin_id=admin_id, admin_password=password, subject=subject)
        ad.save()
        logger.info(ad)
        return HttpResponseRedirect('choose')
    return render(request, 'arapp/admins.html')

def students_view(request):
    if request.method == 'POST':
        student_id = request.POST.get("student_id")
        password = request.POST.get("password")
        subject = request.POST.get("subject")
        st = Student(student_id=student_id, student_password=password, subject=subject)
        st.save()
        return HttpResponseRedirect('/argame')
    return render(request, 'arapp/student.html')

def argame_view(request):
    return render(request, 'arapp/argame.html')

def choose_view(request):
    logger.info("choose here")
    if request.method == 'POST':
        if request.POST.get('myselection') == "add words":
            return HttpResponseRedirect('/addWords')
        elif request.POST.get('myselection') == "play game":
            return HttpResponseRedirect('/argame')
    return render(request, 'arapp/choose.html')

def addWords_view(request):
    if request.method == 'POST':
        subject = request.POST.get("subject")
        word = request.POST.get("word")
        wd = Words(subject=subject, word=word)
        wd.save()
        return HttpResponseRedirect('/addWords')
    return render(request, 'arapp/addWords.html')
