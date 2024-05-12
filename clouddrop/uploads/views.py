from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from .models import FileUpload


class FileUploadListView(LoginRequiredMixin, ListView):
    model = FileUpload
    paginate_by = 20
    context_object_name = 'uploads'
    ordering = '-created_at'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.id)


class FileUploadCreateView(LoginRequiredMixin, CreateView):
    model = FileUpload
    fields = ('data', 'public')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return super().form_valid(form)


class FileUploadDetailView(DetailView):
    model = FileUpload
    context_object_name = 'upload'

    def get_queryset(self):
        return (
            super().get_queryset().filter(Q(public=True) | Q(user=self.request.user.id))
        )


class FileUploadDownloadView(View):
    def get(self, request, pk):
        upload = get_object_or_404(
            FileUpload.objects.filter(id=pk).filter(
                Q(public=True) | Q(user=request.user.id)
            )
        )
        return FileResponse(upload.data.open('rb'), as_attachment=True)
    

class FileUploadDeleteView(LoginRequiredMixin, DeleteView):
    model = FileUpload
    success_url = reverse_lazy('uploads:list')
    context_object_name = 'upload'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.id)
