from django.contrib import admin
from .models import Film, Language, Category, FilmActor, FilmCategory

film_models = [Film, Language, Category, FilmActor, FilmCategory]
admin.site.register(film_models)
