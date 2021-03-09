from django.db import models
from actors.models import Actor

class Language(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    last_update = models.DateTimeField(null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    last_update = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=240, null=False, blank=False)
    description = models.TextField()
    release_year = models.PositiveSmallIntegerField()
    language_id = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL, db_column="language_id")
    original_language_id = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL, related_name='fromlanguage', db_column="original_language_id")
    rental_duration = models.PositiveSmallIntegerField()
    rental_rate = models.PositiveIntegerField()
    length = models.PositiveIntegerField()  
    replacement_cost = models.PositiveIntegerField()
    rating = models.CharField(max_length=120)
    last_update = models.DateTimeField(null=True)
    special_features = models.TextField()
    full_text = models.TextField()
    def __str__(self):
        return self.title

class FilmCategory(models.Model):
    film_id = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = 'Film Categories'

class FilmActor(models.Model):
    actor_id = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL)
    film_id = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(null=True)