from django.apps import AppConfig

# its referenced on setting.py project file
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
