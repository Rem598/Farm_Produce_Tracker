
# Register your models here.
# produce/admin.py
from django.contrib import admin
from .models import Crop, Yield, Sale

admin.site.register(Crop)
admin.site.register(Yield)
admin.site.register(Sale)
