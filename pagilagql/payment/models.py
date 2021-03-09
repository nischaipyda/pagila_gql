from django.db import models

class Payment(models.Model):
    customer = models.ForeignKey('customers.Customer', null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey('staff.Staff', null=True, on_delete=models.SET_NULL)
    rental = models.ForeignKey('store.Rental', null=True, on_delete=models.SET_NULL)
    amount = models.SmallIntegerField()
    payment_date = models.DateTimeField()