from app import app
from flask import *
from passlib.hash import pbkdf2_sha256
from models import user
import datetime
import jwt


@app.route('/login', methods=['POST'])
def login():
    if (request.method == 'POST'):
        loginApi = request.get_json()
        username = loginApi['username']
        email = loginApi['email']
        password = loginApi['password']
        if not username:
            return 'Missing username', 400
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        user = signup.query.filter(signup.email == email).all()
        if not user:
            return 'User Not Found!', 404
        for i in user:
            idd = i.id
            passs = i.password
            name = i.username
            emaill = i.email
            role = i.role
        if pbkdf2_sha256.verify(password, passs):
            session['logged in'] = True
            data = {
                'id': idd,
                'username': name,
                'email': emaill,
                'role': role,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            token = (jwt.encode(data, app.config['SECRET_KEY']))
            temp = [token]
            obj = json.dumps(temp)
            return obj
        else:
            return 'Invalid Login Info!', 400

