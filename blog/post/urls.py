from django.urls import path
from django.urls import path
from . import views
# from post.views import index_view

urlpatterns = [
    path('', views.post_list, name='index'),
    path('create/', views.create_post, name='create_post'),
]