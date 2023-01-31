from django.apps import AppConfig
#import users.signals as defaultuser 

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals

#def ready(self):
#    return defaultuser
