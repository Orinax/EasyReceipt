from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.billing_home, name='billing_home'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),
    path('menu_items/', views.menu_item_list, name='menu_item_list'),
    path('menu-management/', views.menu_item_management, name='menu_item_management'),
    path('bill_list/', views.bill_list, name='bill_list'),
]
