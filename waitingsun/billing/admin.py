from django.contrib import admin
from .models import Customer, Order, MenuItem, Bill

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Bill)
