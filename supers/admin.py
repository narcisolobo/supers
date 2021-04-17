from django.contrib import admin

# Register your models here.
from .models import Super, Power

admin.site.register(Super)
admin.site.register(Power)