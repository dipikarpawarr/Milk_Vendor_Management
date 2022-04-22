from dataclasses import field
from rest_framework import serializers
from .models import Items, Prices, Daily_Destribution

class Items_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['item','category']

class Prices_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['price','unit','applicable_from_date','item']

class Daily_Destribution_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_Destribution
        fields = ['item','quantity','unit','delivered_by']