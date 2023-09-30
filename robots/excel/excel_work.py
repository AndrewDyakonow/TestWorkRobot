from django.utils.timezone import now
from django.db.models import Count

from robots.excel.config import FILENAME
from robots.models import Robot

from openpyxl import Workbook
from datetime import timedelta


class ExcelDistributor:
    robots = None
    models = None

    @classmethod
    def read_robot(cls):
        """Читать базу"""
        cls.robots = ((Robot.objects.values('model', 'version').annotate(quantity=Count('serial')).filter(
            created__gt=now() - timedelta(days=7))).order_by('model'))

        cls.models = cls.robots.values('model').distinct()

        cls.create_report()

    @classmethod
    def create_report(cls):
        """Создать отчёт"""
        work_book = Workbook()
        sheet_list = [work_book.create_sheet(model.get('model')) for model in cls.models]
        del work_book['Sheet']

        for sheet in sheet_list:
            cls.write_sheet(sheet)

        work_book.save(FILENAME)

    @classmethod
    def write_sheet(cls, sheet):
        """Заполнить лист"""
        sheet.append([])
        sheet.append([' ', 'Модель', 'Версия', 'Количество за неделю'])
        for i in cls.robots:
            if i['model'] == sheet.title:
                sheet.append([' ', i['model'], i['version'], i['quantity']])
