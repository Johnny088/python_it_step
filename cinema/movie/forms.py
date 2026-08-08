from django import forms
from .models import Movie, Showtime, Review

input_style: str = 'w-full p-2.5 border rounded-lg focus:ring-2 focus:ring-blue-500'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year', 'duration', 'poster', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': {input_style}}),
            'genre': forms.TextInput(attrs={'class': {input_style}}),
            'release_year': forms.NumberInput(attrs={'class': {input_style}}),
            'duration': forms.NumberInput(attrs={'class': {input_style}}),
            'poster': forms.TextInput(attrs={'class': 'w-full p-2.5 border rounded-lg focus:ring-2 focus:ring-blue-500', 'placeholder': ' example: https://movie/posters/name.jpg'}),
            'description': forms.Textarea(attrs={'class': {input_style}, 'rows': 4}),
        }

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class ShowtimeForm(forms.ModelForm):
    class Meta:
        model = Showtime
        fields = ['date_time', 'hall_number']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'p-2 border rounded-lg w-full'}),
            'hall_number': forms.NumberInput(attrs={'class': 'p-2 border rounded-lg w-full'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'text']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'p-2 border rounded-lg w-full', 'placeholder': 'Your Name'}),
            'rating': forms.NumberInput(attrs={'class': 'p-2 border rounded-lg w-full', 'min': 1, 'max': 10, 'placeholder': '1-10'}),
            'text': forms.Textarea(attrs={'class': 'p-2 border rounded-lg w-full', 'rows': 3, 'placeholder': 'Write your review...'}),
        }