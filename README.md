# iShop

Abstract: This application is a web service for departmental store application

## Installation Instructions

- Clone this repository
- Setup Virtual Environment and activate it

```
virtualenv venv
source venv/Scripts/activate
```

- Install the dependencies

```
pip install -r requirements.txt
```

- Run the application to setup the database. Check iShop/setup/populate_data.py for details

```
uvicorn server:app --port 8000
OR
python server.py
```

Visit http://localhost:8000/docs to view the documentation and interact with the swagger UI

## Code Details

Implementation using FastAPI, Pydantics and SQLite3

## Directory Hierarchy

```
|—— .gitignore
|—— ishop
|    |—— constants
|        |—— global_constants.py
|        |—— queries.py
|        |—— __init__.py
|
|    |—— exceptions
|        |—— IshopExceptions.py
|        |—— __init__.py
|    |—— repository
|        |—— product.py
|        |—— sales.py
|        |—— user.py
|        |—— __init__.py
|
|    |—— routers
|        |—— product_router.py
|        |—— sales_router.py
|        |—— user_router.py
|        |—— __init__.py
|
|    |—— schema
|        |—— schemas.py
|        |—— __init__.py
|
|    |—— service
|        |—— product_service.py
|        |—— sales_service.py
|        |—— user_service.py
|        |—— __init__.py
|
|    |—— setup
|        |—— populate_data.py
|        |—— __init__.py
|
|    |—— utils
|        |—— auth_utils.py
|        |—— connection.py
|        |—— utils.py
|        |—— __init__.py
|
|    |—— __init__.py
|
|—— requirements.py
|—— server.py

```
