import smtplib

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

from R4C.settings import EMAIL_HOST_USER
from orders.models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def send_mails(created, **kwargs):
    """Сигнал отправки сообщения о поступлении"""
    if created:
        outstanding_orders = Order.objects.filter(is_done=False)
        last_robot = Robot.objects.last()

        for order in outstanding_orders.order_by('-id'):
            if order.robot_serial == last_robot.serial:

                send_mail(
                    "Поступление Товара",
                    f"""
                        Добрый день!
                    Недавно вы интересовались нашим роботом модели {last_robot.model}, версии {last_robot.version}.
                    Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами
                    """,
                    EMAIL_HOST_USER,
                    recipient_list=[order.customer.email],
                )
                last_robot.in_stock = False
                last_robot.save()
                order.is_done = True
                order.save()
                break


