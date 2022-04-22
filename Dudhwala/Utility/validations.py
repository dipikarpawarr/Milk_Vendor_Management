from datetime import datetime
from . import utility
from rest_framework.response import Response
from rest_framework import status

def isValid_vacationDate(fromDate, toDate):
    try:
        current_date = utility.get_DateTime()
        isValid = False
        fromDate = datetime.strptime(fromDate,"%Y-%m-%d")
        toDate = datetime.strptime(toDate,"%Y-%m-%d")
        if current_date.date() < fromDate.date() and fromDate.date() <= toDate.date():
            isValid = True
        return isValid
    except Exception as e:
        raise e