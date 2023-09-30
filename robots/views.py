from datetime import datetime
from robots.excel.config import FILENAME
from robots.excel.excel_work import ExcelDistributor
from robots.models import Robot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils.timezone import make_aware
import json


@csrf_exempt
def add_robo(request):
    """Добавить/Читать роботов"""
    if request.method == 'POST':
        data_robot = json.loads(request.body)
        date_created = data_robot['created']
        data_robot['created'] = make_aware(datetime.strptime(date_created,"%Y-%m-%d %H:%M:%S"))
        new_robot = Robot(**data_robot)
        new_robot.clean_fields(exclude=['serial'])
        new_robot.save()
        return HttpResponse('Запись')
    else:
        data = serializers.serialize('json', Robot.objects.all())
        return HttpResponse(data, content_type='application/json')


@csrf_exempt
def get_excel(request):
    try:
        ExcelDistributor.read_robot()
        with open(FILENAME, 'rb') as f:
            file = f.read()
        response = HttpResponse(file, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="report.xls"'
    except IndexError:
        return HttpResponse('Нет данных за неделю')
    return response
