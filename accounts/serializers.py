from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from allauth.account.adapter import get_adapter
from django.conf  import settings
from .models import User
from allauth.account.adapter import get_adapter

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_Seller = serializers.BooleanField()
    is_Customer = serializers.BooleanField()
    phone = serializers.IntegerField()
    job = serializers.CharField()

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.is_Seller = self.data.get('is_Seller')
        user.is_Customer = self.data.get('is_Customer')
        user.phone = self.data.get('phone')
        user.job = self.data.get('job')
        user.save()
        return user

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'job', 'is_Seller', 'is_Customer')
        read_only_fields = ('id', 'is_Seller', 'is_Customer')