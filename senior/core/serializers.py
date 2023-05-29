from rest_framework.serializers import ModelSerializer
from .models import UserModel
from django.contrib.auth import get_user_model

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email']


User = get_user_model()

class UserCreationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
