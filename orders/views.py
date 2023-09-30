import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from orders.logics.processing import add_customer, add_order


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        order_data = json.loads(request.body)
        add_customer(order_data['email'])
        response = add_order(order_data['email'], order_data['robot_serial'])

        return HttpResponse(response)
    else:
        return HttpResponse('гет')
