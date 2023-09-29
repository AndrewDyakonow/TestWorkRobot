from robots.excel.config import FILENAME
from robots.excel.excel_work import ExcelDistributor
from robots.models import Robot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


@csrf_exempt
def add_robo(request):
    """Добавить/Читать роботов"""
    if request.method == 'POST':
        new_robot = Robot(**json.loads(request.body))
        new_robot.clean_fields(exclude=['serial'])
        new_robot.save()
        return HttpResponse('Записано')

    else:
        data = serializers.serialize('json', Robot.objects.all())
        return HttpResponse(data, content_type='application/json')


@csrf_exempt
def get_excel(request):
    ExcelDistributor.read_robot()
    with open(FILENAME, 'rb') as f:
        file = f.read()
    response = HttpResponse(file, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xls"'
    return response
