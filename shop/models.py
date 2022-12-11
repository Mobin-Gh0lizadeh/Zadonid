from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Category")
    name = models.CharField(max_length=200)
#    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productCategory')
    image = models.ImageField(upload_to='media/products/%Y/%m/%d/')
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True, default=None)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.id}'

    def get_likes_count(self):
        return Vote.objects.filter(product=self).count()

    def get_comment_count(self):
        return Comment.objects.filter(product=self).count()

    def get_save_count(self):
        return Save.objects.filter(product=self).count()

    def get_share_count(self):
        return Share.objects.filter(product=self).count()

    def get_pure_price(self):
        if self.discount:
            return int(price - discount)
        return price

class Vote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pvote')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uvote')

    def __str__(self):
        return f'{self.user} liked {self.product}'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ucomment')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pcomment')
    body = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'

    class Meta:
        ordering = ('-created',)

class Save(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='psave')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usave')

    def __str__(self):
        return f'{self.user} saved {self.product}'

class Share(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pshare')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ushare')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tousershare')

    def __str__(self):
        return f'{self.user} shared {self.product}'