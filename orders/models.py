from django.db import models
from shop.models import Product
from django.conf import settings
# Create your models here.

class Order(models.Model):
    POSTITEM = (
        ('post', 'post'),
        ('T-pox', 'T-pox'),
        ('delivery', 'delivery')
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    create = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
#    processing = models.BooleanField(default=False)
#    post = models.BooleanField(default=False)
#    delivery = models.BooleanField(default=False)
    address = models.TextField()
    post = models.CharField(max_length=30, choices=POSTITEM, default='post')
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True, default=None)


    def __str__(self):
        return f'{self.owner} orders'



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f'{self.id}'

