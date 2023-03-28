from django.db import models

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_number = models.IntegerField()
    user_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_price = models.FloatField()
    store_name = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    order_date = models.DateField()


    class Meta:
        app_label  = 'OrderAPI'
        db_table = 'ORDERS'
        constraints = [
            models.UniqueConstraint(fields=['order_id', 'order_number', 'user_id'], name='unique_order')
        ]