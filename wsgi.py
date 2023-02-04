from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the example products API"

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {'id': 1, 'name': 'Product 1'},
        {'id': 2, 'name': 'Product 2'},
        {'id': 3, 'name': 'Product 3'},
    ]
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    products = [
        {'id': 1, 'name': 'Product 1'},
        {'id': 2, 'name': 'Product 2'},
        {'id': 3, 'name': 'Product 3'},
    ]
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'error': 'product not found'}), 404
    return jsonify(product[0])

if __name__ == '__main__':
    app.run(debug=True)