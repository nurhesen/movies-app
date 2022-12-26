from django.contrib import admin

# Register your models here.
from .models import Movie, MovieGenre, MoviesDirector


admin.site.register(Movie)
admin.site.register(MovieGenre)
admin.site.register(MoviesDirector)
