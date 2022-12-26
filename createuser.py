from django.contrib.auth.models import User
from actors.models import Actor, Role
from movies.models import Movie, MovieGenre, MoviesDirector
from directors.models import Director, DirectorsGenre
try:
    usr = User.objects.create_superuser('test', 'test@example.com', 'test')
except:
    pass
