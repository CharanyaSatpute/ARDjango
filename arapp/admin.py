from django.contrib import admin
from .models import Words, Admin, Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_password')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'admin_password', 'subject')

class WordsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'word')

admin.site.register(Words, WordsAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Student, StudentAdmin)
