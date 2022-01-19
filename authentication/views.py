import json
import time
from django.http.response import JsonResponse
from django.shortcuts import render
from authentication.models import RegisterUser
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, serializers, status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



class SignUpUserView(APIView):

    def post(self, request):
        data = json.loads(request.body)
        try:
            User.objects.create_user(username=data['name'],password=data['password'],email=data['email'])
        except:
            return Response({'message':'Already Created User'}, status=status.HTTP_208_ALREADY_REPORTED)
        return Response({'message':'User created Successfully'}, status=status.HTTP_201_CREATED)
