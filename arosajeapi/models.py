# arosajeapi/models.py
from django.db import models

class City(models.Model):
    cityId = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=255)

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=255)
    userAddress = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    lives = models.ForeignKey(City, on_delete=models.CASCADE)

class Plant(models.Model):
    plantId = models.AutoField(primary_key=True)
    species = models.CharField(max_length=255)
    plantDescription = models.TextField()
    name = models.CharField(max_length=255)
    plantAddress = models.CharField(max_length=255)
    keepers = models.ManyToManyField(User, related_name='plants_kept')

class MessageHistory(models.Model):
    messageId = models.AutoField(primary_key=True)
    messageDate = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class PlantImage(models.Model):
    imageId = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='plant_images/')
    imageDate = models.DateTimeField(auto_now_add=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

class Botanist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    provide_tips = models.ManyToManyField(Plant, related_name='botanist_tips')

class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kept_plants = models.ManyToManyField(Plant, related_name='guardian_kept_plants')
    send_receive_messages = models.ManyToManyField(MessageHistory, related_name='guardian_messages')

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    send_receive_messages = models.ManyToManyField(MessageHistory, related_name='owner_messages')
