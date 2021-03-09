from django.db import models

class Inventory(models.Model):
    film_id = models.ForeignKey('film.Film', null=True, on_delete=models.SET_NULL)
    store_id = models.ForeignKey('store.Store', null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Inventories'