from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=120)
    quantity = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])