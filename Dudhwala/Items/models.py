from statistics import quantiles
from turtle import ondrag
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from User_Management.models import Staff_Details

User = get_user_model()
# Create your models here.
class Items(models.Model):
    item = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'items'

class Prices(models.Model):
    price = models.IntegerField(null=False)
    unit = models.CharField(max_length=200)
    applicable_from_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'prices'

class Daily_Destribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    delivered_by = models.ForeignKey(Staff_Details, on_delete=models.CASCADE)

    class Meta:
        db_table = "daily_destribution"