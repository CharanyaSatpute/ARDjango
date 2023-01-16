from django.apps import AppConfig
import sys

class ArappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arapp'

print("hello")
print(sys.path)