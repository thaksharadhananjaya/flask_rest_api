from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'coop'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'test'

mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()