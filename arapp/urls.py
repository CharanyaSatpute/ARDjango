
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students_view, name='student'),
    path('admins/', views.admins_view, name='admins'),
    path('argame/', views.argame_view, name='argame'),
    path('students/argame/', views.argame_view, name='argame'),
    path('admins/choose/', views.choose_view, name='choose'),
    path('admins/choose/argame', views.argame_view, name='argame'),
    path('admins/choose/addWords', views.addWords_view, name='addWords'),
    path('admins/choose/students_info', views.students_info_view, name='students_info'),
    path('choose/', views.choose_view, name='choose'),
    path('save_score/', views.save_score, name='save_score'),
    #path('students_info/', views.students_info_view, name='students_info'),

]

