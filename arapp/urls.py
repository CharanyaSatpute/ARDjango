from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('student.html', views.student, name='student'),
    path('admin.html', views.admin, name='admin'),
    path('argame.html', views.argame, name='argame'),
    path('addWords.html', views.addWords, name='addWords'),
    path('choose.html', views.choose, name='choose'),
    path('admin.html', views.admin_view, name='admin'),
    path('student.html', views.student_view, name='student'),
    path('addWords.html', views.words_view, name='addWords'),
]
