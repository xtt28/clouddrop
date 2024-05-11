from django.contrib.auth import get_user_model
from django.db import models

def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'

class FileUpload(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.FileField(upload_to=user_directory_path)
