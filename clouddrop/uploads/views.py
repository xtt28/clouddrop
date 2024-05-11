from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import FileUpload

class FileUploadListView(LoginRequiredMixin, ListView):
    model = FileUpload
    paginate_by = 20
    context_object_name = 'uploads'
    ordering = '-created_at'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class FileUploadCreateView(LoginRequiredMixin, CreateView):
    model = FileUpload
    fields = ('data', 'public')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return super().form_valid(form)
