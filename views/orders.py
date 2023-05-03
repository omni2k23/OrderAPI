import json
import jsonschema
from datetime import datetime
from models.models import Order, Customer, Driver
from django.db import connection
from django.core import serializers
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def handle_order(request: HttpRequest, customer_id: int):
    
    response_body = {}
    status_code = 200
    
    if request.method == 'GET':
        # Check if customer exist
        if not Customer.objects.filter(pk=customer_id).exists():
            status_code = 404
            response_body["status"] = "Error"
            response_body["description"] = "Customer does not exist"
            response_body["error"] = ""
        else:
            query = 'SELECT * FROM public.order WHERE customer_id = %s;'
            model = Order.objects.raw(raw_query=query, params=[customer_id])
            data = serializers.serialize("json", model)

            result = json.loads(data)
            response_body = [order["fields"] for order in result]
    
    elif request.method == 'POST':
        # Create dict from request
        payload = json.loads(request.body)
        
        # Validate payload
        with open('schemas\order.json', 'r') as f:
            schema = json.load(f)
        
        try:
            jsonschema.validate(payload, schema)
        except jsonschema.ValidationError as error:
            status_code = 400
            response_body["status"] = "Error"
            response_body["description"] = "Could not validate request payload"
            response_body["error"] = str(error)
            return JsonResponse(data=response_body, json_dumps_params={'indent': 2})
        
        # Creating the Order
        order = Order()
        
        customer = Customer()
        customer.customer_id = int(payload["customer_id"])
        customer.save()
        
        driver = Driver()
        driver.driver_id = int(payload["driver_id"])
        driver.save()
        
        # This will always create an order_id +1 from the latest order entry
        order.order_id = Order.objects.order_by('order_id').first().order_id + 1
        order.order_number = int(payload["order_number"])
        order.order_datetime = payload["order_datetime"]
        order.store_name = payload["store_name"]
        order.customer_id = customer
        order.driver_id = driver
        order.item_name = payload["item_name"]
        order.item_price = float(payload["item_price"])
        order.item_picture = payload["item_picture"]
        order.total = float(payload["total"])
        order.status = payload["status"]
        
        # Posting order to DB
        order.save()
        status_code = 200
    elif request.method == "PATCH":
        # The only thing that can be changed is status and driver_id
        payload = json.loads(request.body)
        if not payload["order_id"]:
            status_code = 400
            response_body["status"] = "Error"
            response_body["description"] = "Failed to update order"
            response_body["error"] = "The order_id is missing"
            return JsonResponse(data=response_body, json_dumps_params={'indent': 2})
        
        order = Order.objects.get(int(payload["order_id"]))
        if payload["driver_id"]:
            order.driver_id = int(payload["driver_id"])
        if payload["status"]:
            order.status = payload["status"]
    
    response = JsonResponse(data=response_body, json_dumps_params={'indent': 2}, safe=False)
    response.status_code = status_code
    return response