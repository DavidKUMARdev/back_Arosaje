# arosajeapi/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('plants/', PlantListCreateView.as_view(), name='plant-list-create'),
    path('message-history/', MessageHistoryListCreateView.as_view(), name='message-history-list-create'),
    path('plant-images/', PlantImageListCreateView.as_view(), name='plant-image-list-create'),
    path('botanists/', BotanistListCreateView.as_view(), name='botanist-list-create'),
    path('guardians/', GuardianListCreateView.as_view(), name='guardian-list-create'),
    path('owners/', OwnerListCreateView.as_view(), name='owner-list-create'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/', CurrentUserView.as_view(), name='user-details'),



]