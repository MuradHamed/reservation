from django.contrib import admin
from .models import Client, ClientTypes, Product, Order

admin.site.register(Client)
admin.site.register(ClientTypes)
admin.site.register(Product)
admin.site.register(Order)

