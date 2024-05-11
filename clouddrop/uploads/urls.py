from django.urls import path
from .views import FileUploadListView

app_name = 'uploads'
urlpatterns = [
    path('', FileUploadListView.as_view(), name='list')
]
