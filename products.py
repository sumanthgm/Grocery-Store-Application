import mysql.connector

def get_all_products():
    cnx = mysql.connector.connect(user='root', password='Sumu@777',
                                  host='127.0.0.1',
                                  database='grocery_store')


    cursor = cnx.cursor()
    query= ("SELECT * FROM grocery_store.products")

    cursor.execute(query)



    for (product_id, name, uom_id, price_per_unit) in cursor:
        print(product_id, name, uom_id, price_per_unit)
        pass



    response=[]
    for (product_id, name, uom_id, price_per_unit) in cursor:
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit
        })
        pass
    cnx.close()
    return response

if __name__ == '__main__':
    print(get_all_products())


    sumanth