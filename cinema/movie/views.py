from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Showtime, Review
from .forms import MovieForm, ShowtimeForm, ReviewForm

class MovieListView(ListView):
    model = Movie
    template_name = 'movie/movie-list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie-detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['showtimes'] = self.object.showtimes.filter(date_time__gte=timezone.now())
        context['reviews'] = self.object.reviews.all()
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = self.object
            review.save()
            return redirect('movie_detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(review_form=form))

# --- Make sure these views are in movie/views.py ---

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie/movie-form.html'
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie/movie-form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie/movie-confirm-delete.html'
    success_url = reverse_lazy('movie_list')

class AllShowtimesView(ListView):
    model = Showtime
    template_name = 'movie/showtimes-list.html'
    context_object_name = 'showtimes'

    def get_queryset(self):
        return Showtime.objects.filter(date_time__gte=timezone.now()).select_related('movie')

class ShowtimeCreateView(CreateView):
    model = Showtime
    form_class = ShowtimeForm
    template_name = 'movie/showtime-form.html'

    def form_valid(self, form):
        movie = get_object_or_404(Movie, pk=self.kwargs['movie_id'])
        form.instance.movie = movie
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.kwargs['movie_id']})