from flask import *
from passlib.hash import pbkdf2_sha256
from app import db


@app.route('/signup' ,methods=['GET','POST'])
def signup():
    if (request.method == 'POST'):
        signupAPI = request.get_json()
        userName = signupAPI['firstName'] + " " + signupAPI['lastName']
        email = signupAPI['email']
        password = signupAPI['password']
        hashed = pbkdf2_sha256.hash(password)
        phoneNo = signupAPI['phone']
        role = signupAPI['role']
        checkEmail = signup.query.filter_by(email=email).first()
        checkphone = signup.query.filter_by(phoneno=phoneNo).first()

        if checkEmail!=None and checkphone!=None:
            return make_response("Email or PhoneNo already exists!"),400
        else:
            if checkEmail == None:
                if checkphone == None:
                    newUser = signup(userName=userName, email=email,
                                     password=hashed, phoneNo=phoneNo, role=role)
                    db.session.add(newUser)
                    db.session.commit()
                    return make_response("added"),200
                else:
                    return make_response("phone no already exists"),400
            else:
                return make_response("email already exists"),400

