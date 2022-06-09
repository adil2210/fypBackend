import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
pymysql.install_as_MySQLdb()

app = Flask(__name__)

db=SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:adil2210@localhost:3307/fyp_pdp'
import models
db.create_all()




from api.signup import *
