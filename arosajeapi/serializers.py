from rest_framework import serializers
from .models import City, CustomUser, Plant, MessageHistory, PlantImage, Botanist, Guardian, Owner
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    # Ajoutez les champs supplémentaires de CustomUser
    age = serializers.IntegerField(required=True)
    phone = serializers.CharField(max_length=20, required=True)
    status = serializers.CharField(max_length=255, required=True)
    userAddress = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'age', 'phone', 'status', 'userAddress')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],  # Assurez-vous d'inclure les champs supplémentaires lors de la création de l'utilisateur
            phone=validated_data['phone'],
            status=validated_data['status'],
            userAddress=validated_data['userAddress']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = '__all__'


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'


class BotanistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Botanist
        fields = '__all__'


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
