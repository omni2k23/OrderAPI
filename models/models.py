from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    email = models.TextField()
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    address_line_one = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.IntegerField()
    card_number = models.IntegerField()
    name_on_card = models.TextField()
    expiration_date = models.DateField()

    class Meta:
        app_label = 'OrderAPI'
        db_table = 'customer'


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    email = models.TextField()
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()
    vehicle_type = models.TextField()
    license_number = models.TextField()
    year = models.IntegerField()
    make = models.TextField()
    model = models.TextField()

    class Meta:
        app_label = 'OrderAPI'
        db_table = 'driver'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.IntegerField()
    order_datetime = models.DateTimeField()
    store_name = models.TextField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    item_name = models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_picture = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.TextField()

    class Meta:
        app_label = 'OrderAPI'
        db_table = 'order'
        constraints = [
            models.UniqueConstraint(fields=['order_number'], name='unique_order_number')
        ]

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store_name = models.TextField()
    store_address = models.TextField()
    status = models.TextField()

    class Meta:
        app_label = 'OrderAPI'
        db_table = 'delivery'
