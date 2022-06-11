import pymysql
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
pymysql.install_as_MySQLdb()

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:badar@localhost/fyp'
app.config['SECRET_KEY'] = 'iamsecret'
db=SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
from models import *
db.create_all()


from api.signup import *
from api.login import *
from api.docProfile.docProfileSetting import *