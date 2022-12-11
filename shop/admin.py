from django.contrib import admin
from .models import Product, Category, Vote, Comment, Save, Share

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Vote)
admin.site.register(Comment)
admin.site.register(Save)
admin.site.register(Share)
