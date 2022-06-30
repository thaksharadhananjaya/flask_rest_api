
import conn
from flask import jsonify

# Insert new Customer


def insertCustomer(name, phone, email, city, address, district, postalCode, isMember):

    if name == None or phone == None or email == None or address == None or city == None or district == None or postalCode == None or isMember == None:
        return "Invalid Input !"
    else:
        if email == None:
            discount = ""
        if unit == None:
            unit = ""
        if category == None:
            category = ""
        try:
            sql = '''INSERT INTO `customer` 
                (
                `customer_name`,
                `phone`,
                `email`,
                `city`,
                `address`, 
                `districtt`,
                `postalcode`,
                `isMember`
                ) 
                VALUES(% s, % s, % s, % s, % s, % s, % s, % s)'''
            conn.cursor.execute(
                sql, (name, phone, email, city, address, district, postalCode, isMember))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'


# Update Customer
def updateCustomer(id, name, qty, price, discount, unit, category):

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
            sql = '''UPDATE `customer` SET
                (
                `Customer_name` = % s,
                `Customer_price` = % s,
                `category` = % s,
                `quantity` = % s,
                `unit` = % s, 
                `Customer_discount` = % s
                ) 
                WHERE Customer_id = % s'''
            conn.cursor.execute(
                sql, (name, price, category, qty,  unit,  discount, id))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'


# Get Customers
def getCustomer(search, category):

    sql = None

    # Get all Customers
    if search == None and category == None:
        sql = "SELECT * FROM customer"
    # Search Customer by name
    elif category == None:
        sql = "SELECT * FROM customer WHERE customer_name LIKE '%" + search + "%'"
    # Filtter Customer by category
    elif search == None:
        sql = "SELECT * FROM customer WHERE category = '" + category + "'"
    # Search & filtter Customer by name & category
    else:
        sql = "SELECT * FROM customer WHERE customer_name LIKE '%" + \
            search + "%' AND category = '" + category + "'"

    try:
        conn.cursor.execute(sql)
        row_headers = [x[0] for x in conn.cursor.description]
        results = conn.cursor.fetchall()
        conn.conn.close()
        json_data = []
        for row in results:
            json_data.append(dict(zip(row_headers, row)))
        return jsonify(json_data)
    except:
        return '0'


# Delete Customer
def deleteCustomer(id):

    if id == None:
        return "Invalid Input !"
    else:
        try:
            sql = 'DELETE FROM `customer` WHERE customer_id = % s'
            conn.cursor.execute(sql, (id))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'
