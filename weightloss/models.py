from django.db import models
from django.contrib.auth.models import User

class WeightRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
