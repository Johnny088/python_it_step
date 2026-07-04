from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from workers.models import Worker

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