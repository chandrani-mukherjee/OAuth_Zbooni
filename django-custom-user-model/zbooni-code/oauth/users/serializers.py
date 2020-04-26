from rest_framework import serializers
from .models import CustomUser


class CreateUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password','is_active','is_superuser')
