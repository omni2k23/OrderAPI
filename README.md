# OrderAPI

Manages orders placed by users 

## Install

Before running the service, make sure you have the dependecies to run it. You can run this command:
`pip install djangorestframework markdown django-filter psycopg2 python-environ jsonschema`

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
```json
{
    "status": "OK",
    "timestamp": "03/21/2021 16:22:00",
    "dependencies": {
        "omniDB": {
            "status": "OK",
            "timestamp": "03/21/2021 16:22:00",
        }
    }
}
```

`GET /order/{order_id}`

### Response
```json
[
    {
        "order_number": 456,
        "order_datetime": "2022-12-31T23:59:59",
        "store_name": "Example Store",
        "customer_id": 789,
        "driver_id": 101,
        "item_name": "Example Item",
        "item_price": "9.990000000",
        "total": "19.98000000",
        "status": "Pending"
    }
]
```

`POST /order/{order_id}`

### Request
```json
{
    "order_id": 123,
    "order_number": 456,
    "order_datetime": "2022-12-31T23:59:59Z",
    "store_name": "Example Store",
    "customer_id": 789,
    "driver_id": 101,
    "item_name": "Example Item",
    "item_price": 9.99,
    "total": 19.98,
    "status": "Pending"
}