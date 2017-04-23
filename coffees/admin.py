from django.contrib import admin
from .models import Coffee
from .models import Purchase

admin.site.register(Coffee)
admin.site.register(Purchase)
