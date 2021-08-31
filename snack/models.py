from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    title =models.CharField(max_length=256)
    purchaser =models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    description =models.TextField()



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])
