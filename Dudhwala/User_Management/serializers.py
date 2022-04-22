from pyexpat import model
from rest_framework import serializers
from .models import Staff_Details, userDetails, userDetails_hist, Credential_Details, Credential_Details_hist

class userDetails_serializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ['firstname','middlename','lastname','gender','email_id','address','birth_date']

class userDetails_hist_serializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails_hist
        fields = ['user','firstname','middlename','lastname','gender','email_id','address','birth_date','hist_date','date']

class Credential_Details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Credential_Details
        fields = ['username','password']

class Credential_Details_hist_serializer(serializers.ModelSerializer):
    class Meta:
        model = Credential_Details_hist
        fields = ['username','password','hist_date','credential']
    
class Staff_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_Details
        fields = ['firstname','middlename','lastname','email','username','password']
        