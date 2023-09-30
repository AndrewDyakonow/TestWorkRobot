from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Заказчик')
    robot_serial = models.CharField(max_length=5, verbose_name='Модель для заказа')
    is_done = models.BooleanField(default=False, verbose_name='Статус заказа')

    def __str__(self):
        return f'{self.customer}, {self.robot_serial}'
