from functools import partial
from os import stat
from .models import *
from .serializers import Credential_Details_serializer, userDetails_hist_serializer, userDetails_serializer, Staff_Details_Serializer
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from Utility import utility
from rest_framework.exceptions import *

# Create your views here.

''' This class returns username by validating token '''
class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response({'Message':'Authenticate User', 'valid user': usernames})

''' This class insert userDetails and credentials into database '''
class userProfile_CR(APIView):
    def post(self, request):
        try:
            current_user = request.user
            user= User.objects.get(id=current_user.id)
            current_datetime = utility.getDateTime()
            user_serializer = userDetails_serializer(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save(user_id=user, date=current_datetime)
                # return Response(status=status.HTTP_201_CREATED)
            cred_serializer = Credential_Details_serializer(data=request.data)
            if cred_serializer.is_valid():
                cred_serializer.save(user=user, date=current_datetime)
                return Response(status=status.HTTP_201_CREATED)
            # return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e)
    
    def patch(self,request,pk):
        try:
            current_datetime = utility.getDateTime()
            row = userDetails.objects.get(user_id=pk)
            serializer = userDetails_serializer(row, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
            # row = userDetails.objects.get(user_id=pk)
            # hst_userDetails_serializer = userDetails_hist_serializer(data=row)
            # if hst_userDetails_serializer.is_valid():
            #     hst_userDetails_serializer.save(date=current_datetime)
            #     return Response("Updated",hst_userDetails_serializer.data, status=status.HTTP_200_OK)
        

    def delete(self, request, pk):
        try:
            row = userDetails.objects.get(user_id=pk)
            row.delete()
            return Response(status=status.HTTP_200_OK)
        except userDetails.DoesNotExist as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class Staff_User(APIView):
    def post(self,request):
        current_datetime = utility.get_DateTime()
        user = utility.get_Current_User(request)
        serializer = Staff_Details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, date=current_datetime)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)