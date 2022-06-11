from models import Profile, User, Services, Education, Experience, Specialization
from app import app, db
from sqlalchemy import and_, or_, not_, update, func, delete
from flask_login import current_user
from flask import request, make_response


@app.route('/docProfile', methods=['POST'])
def docProfileSettings():
    if request.method == 'POST':
        docProfileApi = request.get_json()
        firstName = docProfileApi['firstName']
        lastName = docProfileApi['lastName']
        phoneNo = docProfileApi['phoneNo']
        gender = docProfileApi['gender']
        dob = docProfileApi['dob']
        biography = docProfileApi['biography']
        address = docProfileApi['address']
        city = docProfileApi['city']
        state = docProfileApi['state']
        country = docProfileApi['country']
        postalCode = docProfileApi['postalCode']
        pricing = docProfileApi['pricing']
        services = docProfileApi['services']
        specialization = docProfileApi['specialization']
        education = docProfileApi['education']
        experience = docProfileApi['experience']

        getData = Profile.query.filter(Profile.phoneNo == phoneNo).first()
        print(current_user.id)
        user = User.query.filter(User.id == current_user.id).first()

        if getData != None:
            return make_response("Record already added!")
        else:
            user.isProfileCompleted = True
            user.role = None
            db.session.add(user)
            db.session.commit()
            profile_data = Profile(user_id=current_user.id, firstName=firstName, lastName=lastName, phoneNo=phoneNo,
                              gender=gender, dob=dob, biography=biography,
                              address=address, city=city, state=state, country=country, postalCode=postalCode,
                              pricing=pricing)
            db.session.add(profile_data)
            db.session.commit()


        for i in services:
            addDataServ = Services(pid=profile_data.id ,services=i)
            db.session.add(addDataServ)
            db.session.commit()

        for i in specialization:
            addDataSpecia = specialization(pid=profile_data, specialization=i)
            db.session.add(addDataSpecia)
            db.session.commit()
        for i in education:
            addDataEdu = education(pid=profile_data,degree=i['degree'], institute=i['institute'], yearOfCompletion=i['yearOfCompletion'])
            db.session.add(addDataEdu)
            db.session.commit()

        for i in experience:
            addDataExp = experience(pid=profile_data,hospitalName=i['hospitalName'], start=i['start'], end=i['end'],
                                    designation=i['designation'])
            db.session.add(addDataExp)
            db.session.commit()
