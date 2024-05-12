from django.urls import path
from .views import (
    FileUploadCreateView,
    FileUploadDeleteView,
    FileUploadDetailView,
    FileUploadDownloadView,
    FileUploadListView,
    FileUploadUpdateView
)

app_name = 'uploads'
urlpatterns = [
    path('', FileUploadListView.as_view(), name='list'),
    path('create', FileUploadCreateView.as_view(), name='create'),
    path('<int:pk>', FileUploadDetailView.as_view(), name='detail'),
    path('<int:pk>/download', FileUploadDownloadView.as_view(), name='download'),
    path('<int:pk>/delete', FileUploadDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', FileUploadUpdateView.as_view(), name='update'),
]
