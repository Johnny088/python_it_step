from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, DeleteView

from workers.models import Worker, Resume

# Create your views here.


def all_workers(request):
    context = {
        'all_workers': Worker.objects.all()
    }
    return render(request, 'workers/all-workers.html', context)


class WorkerCreateView(CreateView):
    model = Worker
    fields = ['name', 'salary', 'note']
    template_name = 'workers/create-worker.html'
    success_url = reverse_lazy('all_workers')

class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'workers/details-worker.html'
    context_object_name = 'worker'                        #key


class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'workers/delete-worker.html'
    context_object_name = 'worker'
    success_url = reverse_lazy('all_workers')

class ResumeCreateView(CreateView):
    model = Resume
    fields = ['description']
    template_name = 'workers/create-resume.html'

    def dispatch(self, request, *args, **kwargs):
        self.worker = get_object_or_404(Worker, pk=kwargs['worker_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker'] = self.worker
        return context

    def form_valid(self, form):
        form.instance.worker = self.worker
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_worker', kwargs={'pk':self.worker.id})

