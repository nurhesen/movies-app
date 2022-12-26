from django.shortcuts import render
from movies.models import Movie, MovieGenre
from directors.models import Director
from actors.models import Actor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, ActorSerializer
from rest_framework import generics
from .pagination import StandardResultsSetPagination
from django.db.models import Q


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Movie.objects.all()

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        genre = self.request.query_params.get('genre')

        directors = Director.objects.all()
        all_genres = MovieGenre.objects.all()

        if first_name:
            directors = directors.filter(first_name=first_name)

        if last_name:
            directors = directors.filter(last_name=last_name)

        if genre:
            all_genres = all_genres.filter(genre=genre)

        if not directors.exists():
            return Movie.objects.none()

        movies = Movie.objects.filter(
            director__in=[director.id for director in directors],
            genres__in=[genre.id for genre in all_genres],
        )

        return movies


@api_view(['GET'])
def actor_stats(request, actor_id):

    if request.method == 'GET':
        actor = Actor.objects.get(id=actor_id)

        serializer = ActorSerializer(actor)
        return Response(serializer.data)
