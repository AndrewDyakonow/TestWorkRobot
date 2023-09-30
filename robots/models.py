from datetime import timezone
from django.db import models
from django.core.validators import ValidationError
from django.utils.timezone import now
import re

NOTHING = {'blank': False, 'null': False}


class Robot(models.Model):
    """Модель 'Робот'"""
    serial = models.CharField(max_length=5, **NOTHING, verbose_name='Серия')
    model = models.CharField(max_length=2, **NOTHING, verbose_name='Модель')
    version = models.CharField(max_length=2, **NOTHING, verbose_name='Версия')
    created = models.DateTimeField(default=now, **NOTHING, verbose_name='Дата создания')

    def clean_fields(self, **kwargs):
        """Валидация"""
        super().clean_fields(**kwargs)

        if re.match("^[A-Z0-9]{2}$", str(self.model)) is None:
            raise ValidationError('Недопустимое имя модели')
        if re.match("^[A-Z0-9]{2}$", str(self.version)) is None:
            raise ValidationError('Недопустимое имя версии')
        if self.created.astimezone(timezone.utc) > now():
            raise ValidationError('Нельзя указывать будущее время')

    def save(self, **kwargs):
        self.serial = self.model + '-' + self.version
        super().save(**kwargs)

    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'
        ordering = ['pk']

    def __str__(self):
        return f'{self.serial}, {self.model}, {self.version}, {self.created}'
