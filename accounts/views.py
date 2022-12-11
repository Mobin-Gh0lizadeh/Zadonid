from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)