import pathlib

from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        """this code will be run only once at the startup of the Django"""
        
        # create "another_image_thumbnail" folder in media root
        another_image_thumbnail_path = settings.MEDIA_ROOT.joinpath("another_image_thumbnail")
        directory = pathlib.Path(another_image_thumbnail_path)
        directory.mkdir(parents = False, exist_ok = True)

        return
