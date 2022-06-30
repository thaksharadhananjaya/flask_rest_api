from flask import Flask, request
import product
import category


app = Flask(__name__)

# Product get route
@app.route("/", methods = ["GET"])
def home():
    return "<center> <h1>Flask REST API</h1> </center>"

''' Product '''
# Product get route
@app.route("/getProduct", methods = ["GET"])
def getProduct():
    key = request.args.get('key')
    search = request.args.get('search')
    category = request.args.get('category')
    page = request.args.get('page')
    limit = request.args.get('limit')

    
    if key == "1234":
        return product.getProduct(search, category, page, limit)
    else:
        return app.send_static_file('403Error.html')

# Product insert route
@app.route("/insertProduct", methods = ['GET', 'POST'])
def insertProduct():
    if request.method == 'POST':
        key = request.form.get('key')
        name = request.form.get('name')
        category = request.form.get('category')
        price = request.form.get('price')
        qty = request.form.get('qty')
        unit = request.form.get('unit')
        discount = request.form.get('discount')
        if key == "1234":
            return product.insertProduct(name , qty, price, discount, unit, category)
        else:
            return app.send_static_file('403Error.html')
    else:
        return app.send_static_file('403Error.html')
    

# Product update route
@app.route("/updateProduct", methods = ['GET', 'POST'])
def updateProduct():
    if request.method == 'POST':
        key = request.form.get('key')
        id  = request.form.get('id')
        name = request.form.get('name')
        category = request.form.get('category')
        price = request.form.get('price')
        qty = request.form.get('qty')
        unit = request.form.get('unit')
        discount = request.form.get('discount')
        
        if key == "1234":
            return product.updateProduct(id, name, qty, price, discount, unit, category)
        else:
             return app.send_static_file('403Error.html')
    else:
        return app.send_static_file('403Error.html')


# Product delete route
@app.route("/deleteProduct", methods = ["GET","POST"])
def deleteProduct():

    if request.method == 'POST':
        key = request.form.get('key')
        id = request.form.get('id')
        
        if key == "1234":
            return product.deleteProduct(id)
        else:
            return app.send_static_file('403Error.html')
    else:
        return app.send_static_file('403Error.html')


''' Category '''

@app.route("/getCategory", methods = ["GET"])
def getCategory():
    key = request.args.get('key')
    page = request.args.get('page')
    limit = request.args.get('limit')

    if key == "1234":
        return category.getCategory(page, limit)
    else:
        return app.send_static_file('403Error.html')

app.run()
    