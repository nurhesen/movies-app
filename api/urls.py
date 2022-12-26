from django.urls import path
from .views import MovieListView, actor_stats

urlpatterns = [
    path('movies', MovieListView.as_view()),
    path('actor_stats/<int:actor_id>', actor_stats),

]
