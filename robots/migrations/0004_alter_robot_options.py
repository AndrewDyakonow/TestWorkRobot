# Generated by Django 4.2.5 on 2023-09-30 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0003_robot_in_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='robot',
            options={'ordering': ['id'], 'verbose_name': 'Робот', 'verbose_name_plural': 'Роботы'},
        ),
    ]
