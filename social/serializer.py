from rest_framework import serializers
from .models import SellerProfile, CustomerProfile, Relation
from accounts.models import User

class SellerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    followers_count = serializers.IntegerField(source = 'get_followers_count', read_only=True)
    class Meta:
        model = SellerProfile
        fields = '__all__'
        read_only_fields = ('followers_count',)

class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    following_count = serializers.IntegerField(source='get_following_count', read_only=True)
    class Meta:
        model = CustomerProfile
        fields = '__all__'
        read_only_fields = ('following_count',)

class RelationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Relation
        fields = '__all__'
        read_only_fields = ('user',)
