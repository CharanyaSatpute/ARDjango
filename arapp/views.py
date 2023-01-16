from django.shortcuts import render, HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        if request.POST.get('myselection') == "student":
            return HttpResponseRedirect('/students')
        elif request.POST.get('myselection') == "admin":
            return HttpResponseRedirect('/admins')
    return render(request, 'arapp/index.html')

def admins_view(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/choose')
    return render(request, 'arapp/admins.html')

def students_view(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/argame')
    return render(request, 'arapp/student.html')

def argame_view(request):
    return render(request, 'arapp/argame.html')

def choose_view(request):
    if request.method == 'POST':
        if request.POST.get('myselection') == "add words":
            return HttpResponseRedirect('/addWords')
        elif request.POST.get('myselection') == "play game":
            return HttpResponseRedirect('/argame')
    return render(request, 'arapp/choose.html')

def addWords_view(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/addWords')
    return render(request, 'arapp/addWords.html')
