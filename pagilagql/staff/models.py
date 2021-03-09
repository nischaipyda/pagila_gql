from django.db import models
from customers.models import Address

class Staff(models.Model):
    first_name = models.CharField(max_length=120, null=False)
    last_name = models.CharField(max_length=120, null=False)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(null=False)
    store = models.ForeignKey('store.Store', null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=False)
    username = models.CharField(max_length=120, null=False, blank=False)
    password = models.CharField(max_length=120, null=False, blank=False)
    last_update = models.DateTimeField(auto_now_add=True)
    picture = models.CharField(max_length=1000, null=True, blank=True) #TODO: Convert to ImageField
    class Meta:
        verbose_name_plural = 'Staff'
    def __str__(self):
        return self.first_name + " " + self.last_name