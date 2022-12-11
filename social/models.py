from django.db import models
from django.conf import settings
# Create your models here.

class SellerProfile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Seller_account", primary_key=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/Seller/%Y/%m/%d/')

    def __str__(self):
        return self.user.username

    def get_followers_count(self):
        return Relation.objects.filter(to_user=self.user).count()

class CustomerProfile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Customer_account", primary_key=True)
    image = models.ImageField(upload_to='media/customer/%Y/%m/%d/')

    def __str__(self):
        return self.user.username

    def get_following_count(self):
        return  Relation.objects.filter(user=self.user).exclude(to_user=self.user).count()


class Relation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follower')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def get_following(self, user):
        return Relation.objects.filter(to_user=user)

    def get_followers(self, user):
        return Relation.objects.filter(user=user).exclude(to_user=user)

    def get_following_count(self, user):
        return Relation.objects.filter(to_user=user).count()

    def get_followers_count(self, user):
        return Relation.objects.filter(user=user).count()

    def __str__(self):
        return f'{self.user} following {self.to_user}'
