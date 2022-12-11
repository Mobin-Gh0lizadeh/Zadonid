from django.urls import path
from .views import AddToCart, RemoveFromCart, ListCart, ClearCart


urlpatterns = [
    path('add_to_cart/', AddToCart.as_view(), name='add_to_cart'),
    path('list_cart/', ListCart.as_view(), name='list_cart'),
    path('remove_from_cart/', RemoveFromCart.as_view(), name='remove_from_cart'),
    path('clear_cart/', ClearCart.as_view(), name='clear_cart')
]