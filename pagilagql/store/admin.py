from django.contrib import admin
from .models import Store, Rental


store_models = [Store, Rental]
admin.site.register(store_models)
