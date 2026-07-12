from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from workers.models import Worker, Resume

from workers.forms import WorkerCreateForm, WorkerSearchForm

# Create your views here.


def all_workers(request):
    context = {
        'all_workers': Worker.objects.all()
    }
    return render(request, 'workers/all-workers.html', context)


class WorkerCreateView(PermissionRequiredMixin, CreateView):
    model = Worker
    #fields = ['name', 'salary', 'note']
    form_class = WorkerCreateForm
    template_name = 'workers/create-worker.html'
    success_url = reverse_lazy('all_workers')
    permission_required = 'workers.add_worker' # <app name>.<action>_<model's name> <create ==> add /  >

class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'workers/details-worker.html'
    context_object_name = 'worker'                        #key


class WorkerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Worker
    template_name = 'workers/delete-worker.html'
    context_object_name = 'worker'
    success_url = reverse_lazy('all_workers')
    Permission_required = 'workers.delete_worker'

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

class WorkerSearchView(View):
        template_name = 'workers/search-worker.html'

        def get(self, request):
            form = WorkerSearchForm(request.GET or None)
            workers = Worker.objects.all()

            if form.is_valid():
                form_data = form.cleaned_data

                name = form_data.get('name')
                min_salary = form_data.get('min_salary')
                max_salary = form_data.get('max_salary')

                if name:
                    workers = workers.filter(name__icontains=name)

                if min_salary:
                    workers = workers.filter(salary__gte=min_salary)

                if max_salary:
                    workers = workers.filter(salary__gte=max_salary)

            return render(request, self.template_name, {'form': form, 'workers': workers})





