from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie/add/', views.MovieCreateView.as_view(), name='movie_add'),
    path('movie/<int:pk>/edit/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),

    # New endpoints for Showtimes & Reviews
    path('showtimes/', views.AllShowtimesView.as_view(), name='all_showtimes'),
    path('movie/<int:movie_id>/showtimes/add/', views.ShowtimeCreateView.as_view(), name='add_showtime'),
]