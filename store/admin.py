from django.contrib import admin
from .models import Product, Collection, Promotion, Order, Customer, Cart

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Promotion)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Cart)
