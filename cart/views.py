from decimal import Decimal
from rest_framework import serializers, status, generics
from rest_framework.response import Response
from .serializers import AddToCartSerializer, DeleteCartItemSerializer
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse


class AddToCart(generics.GenericAPIView):
    serializer_class = AddToCartSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        cart = Cart(request)
        if serializer.is_valid():
            #user = request.user
            product_id = serializer.data['product_id']
            quantity = serializer.data['quantity']

            try:
                product = Product.objects.get(id=product_id)
                cart.add(
                    product=product,
                    #product_image=str(product.image.url),
                    #product_price=str(Decimal(product.price) * quantity),
                    quantity=quantity,
                )
                content = {'success': 'add to cart.'}
                return Response(content, status=status.HTTP_200_OK)

            except Product.DoesNotExist:
                content = {'error': 'Product matching query does not exist.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCart(generics.GenericAPIView):

    def get(self, request):
        cart = Cart(request)
        total = cart.get_total_price()
        content={"items":[],
                 "total":total}
        for item in cart:
            total_price = item['total_price']
            price = item['price']
            quantity = item['quantity']
            product = item['product']

            data = {
                'total_price': total_price,
                'price': price,
                'quantity': quantity,
                'product': product.id,
            }
            content["items"].append(data)
        return Response(content, status=status.HTTP_200_OK)

class RemoveFromCart(generics.GenericAPIView):
    serializer_class = DeleteCartItemSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        cart = Cart(request)
        if serializer.is_valid():
            product_id = serializer.data['product_id']
            try:
                product = Product.objects.get(id=product_id)
                cart.remove(
                    product=product,
                )
                content = {'success': 'remove from cart.'}
                return Response(content, status=status.HTTP_204_NO_CONTENT)

            except Product.DoesNotExist:
                content = {'error': 'Product matching query does not exist.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClearCart(generics.GenericAPIView):

    def get(self, request):
        cart = Cart(request)
        cart.clear()
        content = {'success': 'clear cart.'}
        return Response(content, status=status.HTTP_204_NO_CONTENT)