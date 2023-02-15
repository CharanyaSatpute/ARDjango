from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from arapp.models import Admin, Words, Student, Score
from django.http import JsonResponse
import json
import logging
from django.contrib import messages

logger = logging.getLogger("mylogger")

def index(request):    
    if request.method == 'POST':
        if request.POST.get('myselection') == "student":
            return HttpResponseRedirect('students')
        elif request.POST.get('myselection') == "admin":
            return HttpResponseRedirect('admins')
    return render(request, 'arapp/index.html')

def admins_view(request): #consider changing to teacher
    #logger.info("here")
    #logger.info(request,request.method)
    print("printed here")
    print(request, request.method)
    if request.method == 'POST':
        print("POST request")
        admin_id = request.POST.get("admin_id")
        password = request.POST.get("password")
        flag = 0
        #ad = Admin(admin_id=admin_id, admin_password=password, subject=subject)
        #ad.save()
        request.session['admin_id'] = admin_id
        ad = Admin.objects.get(admin_id=admin_id)
        if ad.admin_password == password:
            subject = ad.subject
            request.session['flag'] = flag
            return HttpResponseRedirect('choose', {'admin_id': admin_id, 'flag': flag})
        else:
            messages.success(request, 'Passwords do not match or user type is not Admin.')

    return render(request, 'arapp/admins.html')

def students_view(request):
    if request.method == 'POST':
        print("POST request")
        student_id = request.POST.get("student_id")
        password = request.POST.get("password")
        subject = request.POST.get("subject")
        flag=1
        st = Student.objects.get(student_id=student_id)
        if st.student_password == password:
            request.session['subject'] = subject
            request.session['student_id'] = student_id
            request.session['flag'] = flag
            return HttpResponseRedirect('argame', {'student_id': student_id, 'flag': flag})
        else:
            messages.success(request, 'Passwords do not match or user type is not Student.')
    return render(request, 'arapp/student.html')

#def argame_view(request):
 #   wordList = list(Words.objects.filter(subject__contains=Student.subject).values_list('word', flat=True))
  #  print(list(wordList))
   # return render(request, 'arapp/argame.html', {'wordList': wordList})
    #return render(request, 'arapp/argame.html')


def argame_view(request):
    subject = request.session.get('subject', None)
    wordList = list(Words.objects.filter(subject__contains=subject).values_list('word', flat=True))
    print(wordList)
    return render(request, 'arapp/argame.html', {'wordList': wordList})


def choose_view(request):    
    if request.method == 'POST':        
        if request.POST.get('myselection') == "add words":
            return HttpResponseRedirect('/addWords',{'subject':request.session.get('subject')})
        elif request.POST.get('myselection') == "play game":
            print("play game")
            return HttpResponseRedirect('/argame')
        elif request.POST.get('myselection') == "students information":
            print("students info")
            return HttpResponseRedirect('students_info')
    return render(request, 'arapp/choose.html')

def addWords_view(request):
    if request.method == 'POST':
        admin_id = request.session.get('admin_id', None)
        subject = Admin.objects.filter(admin_id__contains=admin_id).values_list('subject', flat=True)
        word = request.POST.get("word")
        if Words.objects.filter(word=word).exists():
            messages.success(request, 'This word is already exists in the database.')
        else:
            wd = Words.objects.create(subject=subject, word=word)
            wd.save()
            logger.info(wd)
            return HttpResponseRedirect('addWords')
    return render(request, 'arapp/addWords.html')


def save_score(request):
    if request.method == 'POST':
        print("post here")
        final_score = request.POST.get('FinalScore')
        flag = request.session.get('flag')
        print(final_score)
        if flag == 1:
            student_id = request.session.get('student_id')
            subject = request.session.get('subject', None)
            print(student_id)
            print(type(student_id))
            id = Student.objects.get(student_id=student_id)
            sc = Score.objects.create(student_id=id, score=final_score, subject =subject )
            sc.save()
            return HttpResponse("Score Saved.")
    return HttpResponse("Error Occured.")


def students_info_view(request):
    si = Score.objects.all()
    return render(request, 'arapp/students_info.html', {'si': si})

def registration_page_view(request):
    if request.method == 'POST':
        name = request.POST.get('Full Name')
        id = request.POST.get('Roll Number')
        password = request.POST.get('psw')
        password_repeat = request.POST.get('psw-repeat')
        type = request.POST.get('category')
        print(type)
        print('register')
        try:
            if type == 'admin' :
                print('admin')
                subject = request.POST.get('subject')
                ad = Admin.objects.get(admin_id=id)
                #message = 'You have already registered. Please log in.'
                messages.success(request, 'You have already registered. Please log in.')
                #return render(request, 'arapp/registration_page.html',{'message': message})
            else:
                print('student')
                st = Student.objects.get(student_id=id)
                #message = 'You have already registered. Please log in.'
                messages.success(request, 'You have already registered. Please log in.')
                #return render(request, 'arapp/registration_page.html',{'message': message})

        except Admin.DoesNotExist:
            if type == 'admin' and password == password_repeat:
                ad = Admin.objects.create(name=name, admin_id=id, admin_password=password, subject=subject)
                ad.save()
                return HttpResponseRedirect('login')
            else:
                #message = 'Passwords do not match or user type is not Admin.'
                messages.success(request, 'Passwords do not match or user type is not Admin.')
                #return render(request, 'arapp/registration_page.html', {'message': message})
        except Student.DoesNotExist:
            if type == 'student' and password == password_repeat:
                st = Student.objects.create(student_id=id, name=name, student_password=password)
                st.save()
                return HttpResponseRedirect('login')
            else:
                #message = 'Passwords do not match or user type is not Admin.'
                messages.success(request, 'Passwords do not match or user type is not Student.')
                #return render(request, 'arapp/registration_page.html', {'message': message})


    return render(request, 'arapp/registration_page.html')