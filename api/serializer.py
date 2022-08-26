from rest_framework import serializers
from django.contrib.auth.models import User
from .models import OfficeModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')

class OfficialSerializer(serializers.ModelSerializer):
    class Meta:
        model=OfficeModel
        fields=('id','designation','department')

   

