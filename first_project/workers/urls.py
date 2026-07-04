from django.urls import path
from workers.views import all_workers, WorkerCreateView, WorkerDetailView, WorkerDeleteView

urlpatterns = [
    path('all/', all_workers, name='all_workers'),
    path('create/', WorkerCreateView.as_view(), name="create_worker"),
    path('<int:pk>/', WorkerDetailView.as_view(), name="detail_worker"),
    path('<int:pk>/delete', WorkerDeleteView.as_view(), name='delete_worker')
]

