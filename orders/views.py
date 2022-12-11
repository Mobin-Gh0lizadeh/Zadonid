from .serializers import OrderSerializer
from .models import OrderItem,Order
from cart.cart import Cart
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from shop.models import Product
from rest_framework import serializers, status, generics


class OrderCreate(GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        cart = Cart(request)
        if serializer.is_valid():
            address = serializer.data['address']
            user = request.user
            total_price = cart.get_total_price()
            if total_price == 0:
                content = {'error': 'carts are empty.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            else :
                order = Order.objects.create(
                owner = user,
                price = total_price,
                paid = False,
                address = address,
                )
                for item in cart:
                    product = item['product']
                    OrderItem.objects.create(
                        product=Product.objects.get(id=product.id),
                        order=order,
                    )
                cart.clear()
                content = {'success': 'create order.'}
                return Response(content, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
