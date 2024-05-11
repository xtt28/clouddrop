from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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
        return super().get_queryset().filter(Q(public=True) | Q(user=self.request.user.id))
