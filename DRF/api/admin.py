from django.contrib import admin
from.models import Product,Cart_item,Order_item,Order,Cart



admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cart_item)
admin.site.register(Order)
admin.site.register(Order_item)
