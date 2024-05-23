from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
	list_display = ['fullname',]
admin.site.register(CustomUser,CustomUserAdmin)
