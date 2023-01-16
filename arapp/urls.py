from django.urls import path
from . import views

'''urlpatterns = [
    path('', views.index, name='index.html'),
    path('index.html', views.index, name='index.html'),
    path('student.html', views.student, name='student.html'),
    path('admins.html', views.admin, name='admins.html'),
    path('argame.html', views.argame, name='argame.html'),
    path('addWords.html', views.addWords, name='addWords.html'),
    path('choose.html', views.choose, name='choose.html'),
    path('admins.html', views.admin_view, name='admins.html'),
    path('student.html', views.student_view, name='student.html'),
    path('addWords.html', views.words_view, name='addWords.html'),
]'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students_view, name='student'),
    path('admins/', views.admins_view, name='admins'),
    #path('argame/', views.argame_view, name='argame_view'),
    path('students/argame/', views.argame_view, name='argame'),
    path('admins/choose/', views.choose_view, name='choose'),
    path('admins/choose/argame', views.argame_view, name='argame'),
    path('admins/choose/addWords', views.addWords_view, name='addWords'),
]

