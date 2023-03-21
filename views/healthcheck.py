from datetime import datetime
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def healthcheck(request):
    """
    Returns status of the API
    """
    healthy = True
   
    response_data = {
        "status": "OK",
        "timestamp": datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
        "dependencies": {
            connection.settings_dict["NAME"]: {"status": "OK"},
        },
    }

    # Check if we are able to connectiong to database
    response_data["dependencies"][connection.settings_dict["NAME"]]["timestamp"] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    if connection.ensure_connection():
        response_data["dependencies"][connection.settings_dict["NAME"]]["status"] = "BAD"
        healthy = False

    response = JsonResponse(data=response_data, json_dumps_params={'indent': 2})
    response.status_code = 200 if healthy else 503
    return response

