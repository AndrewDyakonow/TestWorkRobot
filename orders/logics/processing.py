from customers.models import Customer
from django.db.utils import IntegrityError

from orders.models import Order
from robots.models import Robot


def add_customer(email):
    """Проверить или добавить заказчика"""
    try:
        Customer.objects.create(email=email)
    except IntegrityError:
        print('С этим заказчиком мы уже работали')


def add_order(email, robot_serial):
    """Создать заказ"""
    customer = Customer.objects.get(email=email)
    current_order = Order(customer=customer, robot_serial=robot_serial)

    return check_robots(robot_serial, current_order)


def check_robots(robot_serial, current_order):
    """Проверка заказанного робота в наличии"""
    robots = Robot.objects.filter(serial=robot_serial, in_stock=True)
    if robots.exists():
        robot = robots.first()
        robot.in_stock = False
        robot.save()
        current_order.is_done = True
        current_order.save()
        return 'Заказ оформлен, забирайте'
    elif Robot.objects.filter(serial=robot_serial, in_stock=False).exists():
        current_order.save()
        return 'Нет в наличии, мы Вас уведомим о поступлении'
    else:
        return 'Такой модели мы не производим'
