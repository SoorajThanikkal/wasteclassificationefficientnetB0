from django.contrib import admin

# Register your models here.

from .models import User,Waste

admin.site.register(User)
admin.site.register(Waste)