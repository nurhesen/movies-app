from django.contrib import admin

# Register your models here.
from .models import Actor, Role

admin.site.register(Actor)
admin.site.register(Role)
