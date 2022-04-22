import re
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from Constants import Constants


def isValid_email(email):
    regex = re.compile(Constants.RGX_EMAIL)
    if re.fullmatch(regex, email):
        return email
    else:
        raise ValidationError(email)

def isValid_contactNo(value):
    regex = re.compile(Constants.RGX_CONTACT_NO)
    if re.fullmatch(regex, value):
        return value
    else:
        raise ValidationError('Enter valid contact number')

def isValid_gender(value):
    isSame=False
    for gender in Constants.LST_GENDER:
        if gender==value:
            isSame = True
            break;
    if isSame:
        return value.capitalize() 
    else:
        raise ValidationError('Enter valid gender') 

User=get_user_model()                                          # get_user_model returns currently active user model... either custom user model or built-in user model
class userDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    firstname = models.CharField(max_length=200, null=False)
    middlename = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=50, null=False, validators=[isValid_gender])
    email_id = models.EmailField(validators=[isValid_email])
    address = models.CharField(max_length=500, null=False)
    birth_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'user_details'

class userDetails_hist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200, null=False)
    middlename = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=50, null=False, validators=[isValid_gender])
    email_id = models.EmailField(validators=[isValid_email])
    address = models.CharField(max_length=500, null=False)
    birth_date = models.DateField()
    hist_date = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'user_details_hist'

class Credential_Details(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=10,null=False, validators=[isValid_contactNo])
    password = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    class Meta:
        db_table = 'credential_details'

class Credential_Details_hist(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.IntegerField()
    password = models.CharField(max_length=200)
    hist_date = models.DateTimeField()
    credential = models.ForeignKey(Credential_Details, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'credential_details_hist'

class Staff_Details(models.Model):
    firstname = models.CharField(max_length=200, null=False)
    middlename = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    email = models.EmailField(validators=[isValid_email])
    username = models.CharField(max_length=500, null=False)
    password = models.CharField(max_length=500, null=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'staff_details'