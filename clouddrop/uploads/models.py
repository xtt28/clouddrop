import os
import time
from django.contrib.auth import get_user_model
from django.db import models

def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{int(time.time())}.{filename}'

class FileUpload(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="uploads")
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.FileField(upload_to=user_directory_path)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f'File upload {os.path.basename(self.data.name)}'
