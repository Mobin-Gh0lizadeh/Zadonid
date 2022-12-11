from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from .permissions import IsOwnerOrReadOnly, IsOwnerUserOrReadOnly
from social.permissions import IsSellerUser,IsCustomerUser
# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['owner__username']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsSellerUser]
        elif self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else :
            permission_classes = [IsOwnerOrReadOnly,IsSellerUser]
        return [permission() for permission in permission_classes]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['owner__username', 'price', 'owner__job']
    search_fields = ['owner__username', 'description', 'available']
    ordering_fields =['-created', 'available']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsSellerUser]
        elif self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrReadOnly, IsSellerUser]
        return [permission() for permission in permission_classes]

class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    search_fields = ['product__id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsCustomerUser]
        elif self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerUserOrReadOnly, IsCustomerUser]
        return [permission() for permission in permission_classes]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    search_fields = ['product']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsCustomerUser]
        elif self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerUserOrReadOnly, IsCustomerUser]
        return [permission() for permission in permission_classes]

class SaveViewSet(ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsCustomerUser]
        elif self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerUserOrReadOnly, IsCustomerUser]
        return [permission() for permission in permission_classes]

class ShareViewSet(ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsCustomerUser]
        elif self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerUserOrReadOnly, IsCustomerUser]
        return [permission() for permission in permission_classes]
