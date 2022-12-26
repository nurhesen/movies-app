from django.db import models



class Director(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class DirectorsGenre(models.Model):
    director_id=models.ForeignKey(Director, on_delete=models.CASCADE,related_name='genre')
    genre=models.CharField(max_length=300)
    prob=models.FloatField()

    def __str__(self):
        return self.director_id.first_name +' '+ self.director_id.last_name + ' --> '+self.genre

