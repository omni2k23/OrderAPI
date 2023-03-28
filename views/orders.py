import json
from datetime import datetime
from models.models import Orders
from django.db import connection
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods



@require_http_methods(["GET"])
def get_user_orders(request, user_id):
    # TODO: Check if user_id exist
    query = 'SELECT * FROM orders WHERE user_id = %s;'
    model = Orders.objects.raw(raw_query=query, params=[user_id])
    data = serializers.serialize("json", model)
    
    response = JsonResponse(data=json.loads(data), json_dumps_params={'indent': 2}, safe=False)
    return response

    
  

    