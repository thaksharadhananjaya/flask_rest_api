
import conn
from flask import jsonify

# Insert new product


def insertProduct(name, qty, price, discount, unit, category):

    if name == None or qty == None or price == None:
        return "Invalid Input !"
    else:
        if discount == None:
            discount = "0"
        if unit == None:
            unit = ""
        if category == None:
            category = ""
        try:
            sql = '''INSERT INTO `product_inventory` 
                (
                `product_name`,
                `product_price`,
                `category`,
                `quantity`,
                `unit`, 
                `product_discount`
                ) 
                VALUES(% s, % s, % s, % s, % s, % s)'''
            conn.cursor.execute(
                sql, (name, price, category, qty,  unit,  discount))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'


# Update product
def updateProduct(id, name, qty, price, discount, unit, category):

    if name == None or qty == None or price == None:
        return "Invalid Input !"
    else:
        if discount == None:
            discount = "0"
        if unit == None:
            unit = ""
        if category == None:
            category = ""
        try:
            sql = '''UPDATE `product_inventory` SET
                (
                `product_name` = % s,
                `product_price` = % s,
                `category` = % s,
                `quantity` = % s,
                `unit` = % s, 
                `product_discount` = % s
                ) 
                WHERE product_id = % s'''
            conn.cursor.execute(
                sql, (name, price, category, qty,  unit,  discount, id))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'


# Get products
def getProduct(search, category, page, limit):
    cur = conn.cursor
    if (page == None):
        page = 0
    if (limit == None):
        limit = 1000

    # Get all products
    if search == None and category == None:
        sql = "SELECT * FROM product_inventory LIMIT %s, %s"
        cur.execute(sql, (int(page), int(limit)))
        
    # Search product by name
    elif category == None:
        print(search)
        sql = "SELECT * FROM product_inventory WHERE product_name LIKE  % s LIMIT %s, %s"
        cur.execute(sql, ('%'+search+'%', int(page), int(limit)))
    # Filter product by category
    elif search == None:
        sql = "SELECT * FROM product_inventory WHERE category = %s LIMIT %s, %s"
        cur.execute(sql, (category, int(page), int(limit)))
    # Search & filter product by name & category
    else:
        sql = "SELECT * FROM product_inventory WHERE product_name LIKE %s AND category = %s LIMIT %s, %s"
        cur.execute(sql, ('%'+search+'%', category, int(page), int(limit)))

    try:
        row_headers = [x[0] for x in conn.cursor.description]
        results = cur.fetchall()
        #cur.close()
        json_data = []
        for row in results:
            json_data.append(dict(zip(row_headers, row)))
        return jsonify(json_data)
    except Exception as e:
        return str(e)


# Delete product
def deleteProduct(id):

    if id == None:
        return "Invalid Input !"
    else:
        try:
            sql = 'DELETE FROM `product_inventory` WHERE product_id = % s'
            conn.cursor.execute(sql, (id))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'
