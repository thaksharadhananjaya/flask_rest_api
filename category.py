
import conn
from flask import jsonify

# Insert new product
def insertCategory(category):

    if category == None:
        return "Invalid Input !"
    else:

        try:
            sql = 'INSERT INTO `category` VALUES(% s)'
            conn.cursor.execute(sql, (category))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'


# Get products
def getCategory(page, limit):
    if (page == None):
        page = 0
    if (limit == None):
        limit = 1000
    # Get all products
    sql = "SELECT * FROM category LIMIT % s, % s"

    try:
        conn.cursor.execute(sql, (int(page), int(limit)))
        row_headers = [x[0] for x in conn.cursor.description]
        results = conn.cursor.fetchall()
        #conn.conn.close()
        json_data = []
        for row in results:
            json_data.append(dict(zip(row_headers, row)))
        return jsonify(json_data)
    except :
        return '0'


# Delete category
def deleteCategory(category):

    if id == None:
        return "Invalid Input !"
    else:
        try:
            sql = 'DELETE FROM `category` WHERE category_name = % s'
            conn.cursor.execute(sql, (category))
            conn.conn.commit()
            conn.conn.close()
            return '1'
        except:
            return '0'
