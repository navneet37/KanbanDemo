from rest_framework import serializers
# from .models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

# class PackageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
