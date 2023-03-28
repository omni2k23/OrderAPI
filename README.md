# OrderAPI

Manages orders placed by users 

## Install

Before running the service, make sure you have the dependecies to run it. You can run this command:
`pip install djangorestframework markdown django-filter python-dotenv cx_Oracle`

Create a `.env` file in `OrderAPI/` and follow this template
````
DB_USERNAME= your oracle db username
DB_PASSWORD= your oracle db password
````

You need this so the service can access the database.
## Run the app

    python manage.py runserver

# REST API

The REST API to the example app is described below.

## Get list of Things

### Request

`GET /healthcheck/`


### Response

    {
        "status": "OK",
        "timestamp": 03/21/2021 16:22:00,
        "dependencies": {
            "xe": {
                status: "OK",
                timestamp: 03/21/2021 16:22:00,
            }
        }
    }