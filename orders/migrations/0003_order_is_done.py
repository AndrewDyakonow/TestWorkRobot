# Generated by Django 4.2.5 on 2023-09-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_customer_alter_order_robot_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Статус заказа'),
        ),
    ]
