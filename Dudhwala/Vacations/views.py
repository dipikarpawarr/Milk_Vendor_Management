from typing import Container
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vacations
from .seralizers import vacations_serializer
from Constants import Constants
from Utility import utility, validations
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import datetime
# from datetime import datetime, date

from Vacations import seralizers


# Create your views here.

class Vacations_CRUD(APIView):
    def get_object(self,pk):
        permission_classes = [IsAdminUser, IsAuthenticated]
        row = Vacations.objects.get(id=pk)
        return row
        
    def get(self, request, **kwargs):
        params = kwargs
        permission_classes = [IsAdminUser, IsAuthenticated]
        if params['show_record_by'] == Constants.MONTHLY:
            first_day, last_day = utility.get_Start_End_Date_of_Month(params['year'], params['month'])
            vacationList = Vacations.objects.filter(fromDate__range = [first_day, last_day])
            seralizer = vacations_serializer(vacationList, many=True)
            return Response(seralizer.data, status=status.HTTP_200_OK)
        elif params['show_record_by'] == Constants.YEARLY:
            first_day, last_day = utility.get_Start_End_Date_of_Year(params['year'])
            vacationList = Vacations.objects.filter(fromDate__range = [first_day, last_day])
            seralizer = vacations_serializer(vacationList, many=True)
            return Response(seralizer.data, status=status.HTTP_200_OK)
        elif params['show_record_by'] == Constants.ALL:
            vacationList = Vacations.objects.all()
            seralizer = vacations_serializer(vacationList, many=True)
            return Response(seralizer.data, status=status.HTTP_200_OK)
        return Response(seralizer.errors, status=status.HTTP_200_OK)

    def post(self, request):
        permission_classes = [IsAdminUser, IsAuthenticated]
        req_data = request.data
        try:
            isValid = validations.isValid_vacationDate(req_data['fromDate'], req_data['toDate'])
        except:
            return Response('day is out of range for month', status=status.HTTP_400_BAD_REQUEST)
        if isValid:
            current_date = utility.get_DateTime()
            user = utility.get_Current_User(request)
            seralizer = vacations_serializer(data=request.data)
            if seralizer.is_valid():
                seralizer.save(date=current_date, user=user)
                return Response(seralizer.data,status=status.HTTP_200_OK)
            return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('Please enter valid dates', status = status.HTTP_400_BAD_REQUEST)
       
    def patch(self, request, pk):
        permission_classes = [IsAdminUser, IsAuthenticated]
        current_date = utility.get_DateTime()
        current_date = datetime.date(current_date.year, current_date.month, current_date.day)
        row = self.get_object(pk)
        if not(row.fromDate <= current_date and row.toDate >= current_date):
            seralizer = vacations_serializer(row, data=request.data, partial=True)
            if seralizer.is_valid():
                seralizer.save(last_updated=current_date)
                return Response(seralizer.data,status=status.HTTP_200_OK)
            return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Cannot update", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            permission_classes = [IsAdminUser, IsAuthenticated]
            current_date = utility.get_DateTime()
            current_date = datetime.date(current_date.year, current_date.month, current_date.day)
            row = Vacations.objects.get(id=pk)
            if not(row.fromDate > current_date):
                row.delete()
                return Response(status=status.HTTP_200_OK)
            return Response("Cannot Delete",status=status.HTTP_400_BAD_REQUEST)
        except Vacations.DoesNotExist as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)