from django.contrib import admin
from .models import SellerProfile, CustomerProfile, Relation


admin.site.register(SellerProfile)
admin.site.register(CustomerProfile)
admin.site.register(Relation)
