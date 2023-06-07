from django.db import models

from product.models import Product
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        total = 0
        if self.is_paid:
            for od in self.order_detail.all():
                total += od.final_price
        else:
            for od in self.order_detail.all():
                total += od.product.price * od.count
        return total

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     if self.is_paid == True:
    #         self.order_detail.total_price = self.total_price()
    #     return super(Order, self).save()

    def __str__(self):
        return f'{self.user} + is paid: {self.is_paid}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_detail')
    count = models.PositiveSmallIntegerField()
    final_price = models.DecimalField(max_digits=8, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        return self.product.price * self.count

    def __str__(self):
        return str(self.order)