from django.urls import path, include
from .views import UserList

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('userlist/', UserList.as_view(), name='UserList'),
    ]