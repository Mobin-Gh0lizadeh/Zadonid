from .models import CustomerProfile, SellerProfile, Relation
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from .serializer import SellerSerializer, CustomerSerializer, RelationSerializer
from .permissions import IsOwnerOrReadOnly, IsSellerUser, IsCustomerUser
from django.shortcuts import get_object_or_404
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SellerList(ListAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerSerializer

class SellerCreate(CreateAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsSellerUser, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SellerDetail(RetrieveUpdateAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CustomerCreate(ListCreateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsCustomerUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CustomerDetail(RetrieveUpdateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsCustomerUser,IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CreateRelation (ListCreateAPIView):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer
    permission_classes = (IsCustomerUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Following(ListAPIView):
    serializer_class = RelationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = get_object_or_404(User, pk = self.kwargs["pk"])
        return Relation.objects.filter(to_user = user)

class Followers(ListAPIView):
   # queryset = Relation.objects.all()
    serializer_class = RelationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = get_object_or_404(User, pk = self.kwargs["pk"])
        return Relation.objects.filter(user = user).exclude(to_user = user)