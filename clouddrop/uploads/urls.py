from django.urls import path
from .views import FileUploadCreateView, FileUploadDetailView, FileUploadListView

app_name = 'uploads'
urlpatterns = [
    path('', FileUploadListView.as_view(), name='list'),
    path('create', FileUploadCreateView.as_view(), name='create'),
    path('<int:pk>', FileUploadDetailView.as_view(), name='detail'),
]
