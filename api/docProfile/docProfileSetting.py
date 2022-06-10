from flask import *
from models.docProfileSetting import profile, service
from models import *
from sqlalchemy import and_, or_, not_, update, func, delete


@app.route('/docProfile', methods=['POST'])
def docProfileSettings():
    if (request.method == 'POST'):
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
        getData = profile.query.filter(profile.phoneNo == phoneNo).first()

        if getData != None:
            return make_response("Record already added!")
        else:
            stmt = (update(user).where(user.id == docProfileApi['id']).values(role="Doctor", isProfileCompleted=True))
            db.session.execute(stmt)
            db.session.commit()
            addData = profile(firstName=firstName, lastName=lastName, phoneNo=phoneNo, gender=gender, dob=dob,
                              biography=biography,
                              address=address, city=city, state=state, country=country, postalCode=postalCode,
                              pricing=pricing)
            db.session.add(addData)
            db.session.commit()

        for i in services:
            addDataServ = service(services=services)
            db.session.add(addDataServ)
            db.session.commit()

        for i in specialization:
            addDataSpecia = specialization(specialization=specialization)
            db.session.add(addDataSpecia)
            db.session.commit()

        for i in education:
            addDataEdu = education(degree=('degree'), institute=('institute'), yearOfCompletion=('yearOfCompletion'))
            db.session.add(addDataEdu)
            db.session.commit()

        for i in experience:
            addDataExp = experience(hospitalName=('hospitalName'), start=('start'), end=('end'),
                                    designation=('designation'))
            db.session.add(addDataExp)
            db.session.commit()
