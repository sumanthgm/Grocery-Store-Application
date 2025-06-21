from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
# import mysql.connector
import json
#
# import products_dao
# import orders_dao
import uom_dao

connection = get_sql_connection()

app = Flask(__name__)

import products_dao

@app.route('/getProducts')
def hello():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response=uom_dao.get_uom(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['POST'])
def insert_products():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_products(connection, request_payload)
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product(connection, product_id):
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting python flask server from growswery store management system")
    app.run(port=5000)

