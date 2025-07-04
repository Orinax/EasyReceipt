from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - Room {self.room_number}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.item.name} x{self.quantity}"

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    generated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill for {self.customer.name} - ${self.total_amount}"

