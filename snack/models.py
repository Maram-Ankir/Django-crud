from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    title =models.CharField(max_length=64)
    purchaser =models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    description =models.TextField()


