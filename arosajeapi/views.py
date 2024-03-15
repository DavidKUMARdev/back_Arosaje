from django.shortcuts import render

# arosajeapi/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics

class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class PlantListCreateView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

class PlantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

class MessageHistoryListCreateView(generics.ListCreateAPIView):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer
    permission_classes = [IsAuthenticated]

class PlantImageListCreateView(generics.ListCreateAPIView):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
    permission_classes = [IsAuthenticated]

class BotanistListCreateView(generics.ListCreateAPIView):
    queryset = Botanist.objects.all()
    serializer_class = BotanistSerializer
    permission_classes = [IsAuthenticated]

class GuardianListCreateView(generics.ListCreateAPIView):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer
    permission_classes = [IsAuthenticated]

class OwnerListCreateView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer