
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students_view, name='student'),
    path('admins/', views.admins_view, name='admins'),
    #path('argame/', views.argame_view, name='argame_view'),
    path('students/argame/', views.argame_view, name='argame1'),
    path('admins/choose/', views.choose_view, name='choose'),
    path('admins/choose/argame', views.argame_view, name='argame'),
    path('admins/choose/addWords', views.addWords_view, name='addWords'),
]

