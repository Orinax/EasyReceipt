from django.shortcuts import render
from .models import Customer, Order, MenuItem, Bill

def billing_home(request):
    return render(request, 'billing/home.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'billing/customer_list.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'billing/order_list.html', {'orders': orders})

def menu_item_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'billing/menu_item_list.html', {'menu_items': menu_items})

def menu_item_management(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'billing/menu_item_management.html', {'menu_items': menu_items})

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'billing/bill_list.html', {'bills': bills})

