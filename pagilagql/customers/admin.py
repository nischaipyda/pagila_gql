from django.contrib import admin
from .models import Customer, Country, City, Address

customer_models = [Customer, Address, City, Country]
admin.site.register(customer_models)
