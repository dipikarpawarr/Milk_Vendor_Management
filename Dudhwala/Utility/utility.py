from datetime import datetime
import calendar
from django.contrib.auth.models import User

def get_DateTime():
    return datetime.now()

def get_Current_User(request):
    current_user = request.user
    user= User.objects.get(id=current_user.id)
    return user

def get_Start_End_Date_of_Month(month_year, month_number):
    last_day = calendar.monthrange(int(month_year), int(month_number))
    str_last_day = month_year +"-"+ month_number +"-"+ str(last_day[1])
    last_day = datetime.strptime(str_last_day,"%Y-%m-%d")
    str_first_day = month_year +"-"+ month_number +"-"+ str(1)
    first_day = datetime.strptime(str_first_day,"%Y-%m-%d")
    return first_day, last_day

def get_Start_End_Date_of_Year(month_year):
    str_first_day = month_year +"-"+ "01" +"-"+ "31"
    first_day = datetime.strptime(str_first_day,"%Y-%m-%d")
    str_last_day = month_year +"-"+ "12" +"-"+ "31"
    last_day = datetime.strptime(str_last_day,"%Y-%m-%d")
    return first_day, last_day