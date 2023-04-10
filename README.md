# OrderAPI

Manages orders placed by users 

## Install

Before running the service, make sure you have the dependecies to run it. You can run this command:
`pip install djangorestframework markdown django-filter psycopg2 python-environ`

Create a `.env` file in `OrderAPI/` and add the following environment variables
````
DB_NAME= name
DB_USER= username
DB_PASSWORD= password
DB_HOST= host
DB_PORT= port
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
            "omniDB": {
                status: "OK",
                timestamp: 03/21/2021 16:22:00,
            }
        }
    }