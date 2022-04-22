from .models import Vacations
from rest_framework import serializers

class vacations_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vacations
        fields = ['fromDate','toDate']
