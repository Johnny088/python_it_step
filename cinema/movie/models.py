from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    genre = models.CharField(max_length=100)
    poster = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    date_time = models.DateTimeField()
    hall_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['date_time']

    def __str__(self):
        return f"{self.movie.title} - {self.date_time.strftime('%Y-%m-%d %H:%M')} (Hall {self.hall_number})"


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Rating from 1 to 10"
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user_name} on {self.movie.title} ({self.rating}/10)"