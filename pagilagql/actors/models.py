from django.db import models

class Actor(models.Model):
    first_name = models.TextField(max_length=120, null=False)
    last_name = models.TextField(max_length=120, null=False)
    last_update = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name + " " + self.last_name