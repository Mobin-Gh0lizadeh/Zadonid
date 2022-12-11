from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ("New Fields", {'fields': ('is_Seller', 'is_Customer', 'phone', 'job')}),
)
admin.site.register(User, UserAdmin)
