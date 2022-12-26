from django.db import models
from movies.models import Movie


class Actor(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)

    def top_genre(self):
        roles = Role.objects.filter(actor_id=self.id)
        genres = [role.movie_id.genres.genre for role in roles]
        return max(set(genres), key=genres.count)

    def number_of_movies(self):
        roles = Role.objects.filter(actor_id=self.id)
        movies = [role.movie_id for role in roles]
        return len(list(dict.fromkeys(movies)))

    def number_of_movies_by_genre(self):
        roles = Role.objects.filter(actor_id=self.id)
        genres = [role.movie_id.genres.genre for role in roles]
        genre_numbers = {}
        for genre in genres:
            if genre not in genre_numbers:
                genre_numbers[genre] = 1
            else:
                genre_numbers[genre] += 1

        return genre_numbers

    def most_frequent_partner(self):
        roles = Role.objects.filter(actor_id=self.id)
        movies = [role.movie_id for role in roles]
        actors = []
        for movie in movies:
            roles = Role.objects.filter(movie_id=movie.id)
            for role in roles:
                if role.actor_id.id != self.id:
                    actors.append(role.actor_id)

        return max(set(actors), key=actors.count)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Role(models.Model):
    actor_id = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name='role')
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='role')
    role = models.CharField(max_length=300)

    def __str__(self):
        return self.movie_id.name + ' --> ' + self.role
