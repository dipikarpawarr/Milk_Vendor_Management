from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
User=get_user_model()

class Vacations(models.Model):
    id = models.BigAutoField(primary_key=True)
    fromDate = models.DateField()
    toDate = models.DateField()
    date = models.DateTimeField()
    last_updated = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Vacations'