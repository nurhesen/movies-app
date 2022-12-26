from movies.models import Movie
from actors.models import Actor
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'rank']


class ActorSerializer(serializers.ModelSerializer):
    top_genre = serializers.CharField()
    number_of_movies = serializers.CharField()
    number_of_movies_by_genre = serializers.CharField()
    most_frequent_partner = serializers.CharField()

    class Meta:
        model = Actor
        fields = ["top_genre",
                  "number_of_movies",
                  "number_of_movies_by_genre",
                  "most_frequent_partner",
                  "first_name",
                  "last_name",
                  "gender"]
