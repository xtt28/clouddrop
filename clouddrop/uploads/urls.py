from django.urls import path
from .views import (
    FileUploadCreateView,
    FileUploadDetailView,
    FileUploadDownloadView,
    FileUploadListView,
)

app_name = 'uploads'
urlpatterns = [
    path('', FileUploadListView.as_view(), name='list'),
    path('create', FileUploadCreateView.as_view(), name='create'),
    path('<int:pk>', FileUploadDetailView.as_view(), name='detail'),
    path('<int:pk>/download', FileUploadDownloadView.as_view(), name='download'),
]
