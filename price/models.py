from django.db import models
from datetime import  datetime
# Create your models here.
class Discount(models.Model):
    description = models.CharField(max_length=1000)
    upto = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.description
