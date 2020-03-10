from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create a new instance of Flask and store it in app 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.33.97/flask1'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

# import the ./application/routes.py file
from application import routes
