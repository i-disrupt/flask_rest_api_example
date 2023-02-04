## Basic Flask REST API
This basic Flask REST API is meant to show a basic understanding of how building
APIs with Flask works. This Flask application defines two routes: /products and /products/(int:product_id) (dynamic). The first route returns a list of all products as a JSON object, while the second route returns a single product based on its ID. If the requested product ID is not found, the API returns a JSON object with an error message and a 404 status code.

- - -
## Run this project with the following command(s)
( requires Python 3.9.11+ )
```
git clone https://github.com/i-disrupt/flask_rest_api_example.git ./flask_api && cd ./flask_api
```
If `virtualenv` is installed:
```
virtualenv env && source env/Scripts/activate && python wsgi.py
```

or do it this way:
```
pip install -r requirements.txt && python wsgi.py
```

