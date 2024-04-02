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
from copy import deepcopy
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

class PlantListCreateView(generics.ListCreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Plant.objects.filter(owner=user_id)
        
        return queryset

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
    queryset = CustomUser.objects.all() 
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class PlantCreateView(generics.CreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        mutable_data = deepcopy(request.data)
        mutable_data['owner'] = request.user.id

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)