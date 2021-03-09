from django.db import models
from customers.models import Address
from staff.models import Staff

class Store(models.Model):
    manager_staff_id = models.ForeignKey(Staff,null=True, on_delete=models.SET_NULL, related_name='staff_id')
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(auto_now=True)

class Rental(models.Model):
    rental_date = models.DateTimeField(null=True)
    inventory = models.ForeignKey('inventory.Inventory', null=True , on_delete=models.SET_NULL)
    customer = models.ForeignKey('customers.Customer', null=True, on_delete=models.SET_NULL)
    return_date = models.DateTimeField()
    staff = models.ForeignKey('staff.Staff', null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(auto_now=True)