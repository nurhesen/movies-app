from django.db import models
from directors.models import Director


class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return self.name + ' ('+str(self.year)+')'


class MovieGenre(models.Model):
    movie_id = models.OneToOneField(
        Movie, on_delete=models.CASCADE, related_name='genres')
    genre = models.CharField(max_length=300)

    def __str__(self):
        return self.genre + ' --> ' + str(self.movie_id)


class MoviesDirector(models.Model):
    director_id = models.ForeignKey(
        Director, on_delete=models.CASCADE, related_name='movie')
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return str(self.movie_id) + ' --> ' + str(self.director_id)
