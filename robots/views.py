import json
from robots.models import Robot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


@csrf_exempt
def add_robo(request):

    if request.method == 'POST':
        new_robot = Robot(**json.loads(request.body))
        new_robot.clean_fields(exclude=['serial'])
        new_robot.save()
        return HttpResponse('Записано')

    else:
        data = serializers.serialize('json', Robot.objects.all())
        return HttpResponse(data, content_type='application/json')
