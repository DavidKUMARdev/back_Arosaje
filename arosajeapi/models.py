
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Définissez les relations avec les groupes et les autorisations
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='customuser_set', related_query_name='user')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='customuser_set', related_query_name='user')

    class Meta:
        # Spécifiez une table supplémentaire si nécessaire
        db_table = 'custom_user'

class City(models.Model):
    cityId = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=255)

class Plant(models.Model):
    plantId = models.AutoField(primary_key=True)
    species = models.CharField(max_length=255)
    plantDescription = models.TextField()
    name = models.CharField(max_length=255)
    plantAddress = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_plants', null=True)
    keepers = models.ManyToManyField(CustomUser, related_name='kept_plants', blank=True)

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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    provide_tips = models.ManyToManyField(Plant, related_name='botanist_tips')

class Guardian(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    kept_plants = models.ManyToManyField(Plant, related_name='guardian_kept_plants')
    send_receive_messages = models.ManyToManyField(MessageHistory, related_name='guardian_messages')

class Owner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    send_receive_messages = models.ManyToManyField(MessageHistory, related_name='owner_messages')
