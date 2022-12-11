from rest_framework import serializers
from .models import Product, Category, Vote, Comment, Save, Share


class CategorySerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    likes_count = serializers.IntegerField(source='get_likes_count', read_only = True)
    comment_count = serializers.IntegerField(source='get_comment_count', read_only=True)
    save_count = serializers.IntegerField(source='get_save_count', read_only=True)
    share_count = serializers.IntegerField(source='get_share_count', read_only=True)
    pure_price = serializers.IntegerField(source='get_pure_price', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('likes_count', 'comment_count', 'save_count', 'share_count', 'pure_price')

class VoteSerializer (serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Vote
        fields = '__all__'

class CommentSerializer (serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = '__all__'

class SaveSerializer (serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Save
        fields = '__all__'

class ShareSerializer (serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Share
        fields = '__all__'