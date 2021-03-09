from django.db import models

class Country(models.Model):
    country = models.TextField(max_length=120, null=False)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.country

class City(models.Model):
    city = models.TextField(max_length=120, null=False)
    country_id = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Cities'
    def __str__(self):
        return self.city

class Address(models.Model):
    address = models.TextField(max_length=240, null=False)
    address2 = models.TextField(max_length=240, null=True)
    district = models.TextField(max_length=120, null=False)
    city_id = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    postal_code = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=False)
    last_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Addresses'
    def __str__(self):
        return self.address

class Customer(models.Model):
    store_id = models.ForeignKey('store.Store', null=True, on_delete=models.SET_NULL)
    first_name = models.TextField(max_length=120, null=False)
    last_name = models.TextField(max_length=120, null=False)
    email = models.EmailField(null=False)
    address_id = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    active_bool = models.BooleanField(null=False, default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateField(null=True)
    active = models.SmallIntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name