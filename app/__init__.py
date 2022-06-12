import pymysql
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'images'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app = Flask(__name__, static_url_path='',
            static_folder='images')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:adil2210@localhost:3307/fyp_pdp'
app.config['SECRET_KEY'] = 'iamsecret'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
CORS(app)
from models import *

db.create_all()

from api.signup import *
from api.login import *
from api.docProfile.docProfileSetting import *
from api.uploadImage.imageApi import *
