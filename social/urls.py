from django.urls import path
from .views import SellerList, CustomerCreate, SellerDetail, SellerCreate, CustomerDetail, Following, Followers, CreateRelation


urlpatterns = [
    path('sellers_list/', SellerList.as_view(), name ='SellerList'),
    path('customers/create/', CustomerCreate.as_view(), name ='CustomerCreate'),
    path('sellers/<int:pk>/', SellerDetail.as_view(), name='SellerDetail'),
    path('sellers/create/', SellerCreate.as_view(), name='SellerCreate'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='CustomerDetail'),
    path('follow/', CreateRelation.as_view(), name='ListCreateRelation'),
    path('following/<int:pk>/', Following.as_view(), name='following'),
    path('followers/<int:pk>/', Followers.as_view(), name='followers'),
]
