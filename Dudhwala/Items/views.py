from functools import partial
from multiprocessing import managers
from django.shortcuts import render
from Extra_Requests import serializers
from .models import Items, Prices, Daily_Destribution
from .serializers import Items_Serializer, Prices_Serializer, Daily_Destribution_Serializer
from Utility import utility
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class Items_CRUD(APIView):
    def get_object(self, pk):
        row = Items.objects.get(id=pk)
        return row

    def get(self, request):
        rows = Items.objects.all()
        serializer = Items_Serializer(rows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        current_datetime = utility.get_DateTime()
        serializer = Items_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(date=current_datetime)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            row = self.get_object(pk)
        except Items.DoesNotExist:
            return Response("Object does not exist", status=status.HTTP_400_BAD_REQUEST)
        serializer = Items_Serializer(row, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            row = self.get_object(pk)
        except Items.DoesNotExist:
            return Response("Object does not exist", status=status.HTTP_400_BAD_REQUEST)
        row.delete()
        return Response("Item Deleted", status=status.HTTP_200_OK)

class Price_CRUD(APIView):
    def get_object(self, pk):
        row = Prices.objects.get(id=pk)
        return row

    def get(self, request):
        # data = kwargs
        # if data['pk']:
        #     row = Prices.objects.get(id=data['pk'])
        #     return row
        # else:
            rows = Prices.objects.all()
            serializer = Prices_Serializer(rows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        current_datetime = utility.get_DateTime()
        user = utility.get_Current_User(request)
        serializer = Prices_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, date=current_datetime)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            row = self.get_object(pk)
        except Prices.DoesNotExist:
            return Response("Object does not exist", status=status.HTTP_400_BAD_REQUEST)
        serializer = Prices_Serializer(row, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            row = self.get_object(pk)
        except Prices.DoesNotExist:
            return Response("Object does not exist", status=status.HTTP_400_BAD_REQUEST)
        row.delete()
        return Response("Item Deleted", status=status.HTTP_200_OK)

class Daily_Destribution_CRUD(APIView):
    def get_object(self, pk):
        row = Daily_Destribution.objects.get(id=pk)
        return row

    def post(self, request):
        with transaction.Atomic():
            current_datetime = utility.get_DateTime()
            user = utility.get_Current_User(request)
            serializer = Daily_Destribution_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user, date=current_datetime)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        with transaction.atomic():
            try:
                row = self.get_object(pk)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
            serializer = Daily_Destribution_Serializer(row, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            row = self.get_object(pk)
        except Exception as e:
            logger.error("DAILY_DESTRI|",e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        row.delete()
        return Response("Deleted", status=status.HTTP_200_OK)