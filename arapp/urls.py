
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_page_view, name='registration_page'),
    path('login/', views.index, name='index'),
    path('login/students/', views.students_view, name='student'),
    path('login/admins/', views.admins_view, name='admins'),
    path('argame/', views.argame_view, name='argame'),
    path('login/students/argame/', views.argame_view, name='argame'),
    path('login/admins/choose/', views.choose_view, name='choose'),
    path('login/admins/choose/argame', views.argame_view, name='argame'),
    path('login/admins/choose/addWords', views.addWords_view, name='addWords'),
    path('login/admins/choose/students_info', views.students_info_view, name='students_info'),
    #path('choose/', views.choose_view, name='choose'),
    path('save_score/', views.save_score, name='save_score'),
    #path('registration_page', views.registration_page_view, name='registration_page'),
    #path('students_info/', views.students_info_view, name='students_info'),

]

