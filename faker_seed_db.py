from faker import Faker

#  creation of faker profile helper function
def getProfile():
    fake = Faker()
    return fake.profile()

# gather data and place inside of database
import os
from second_employee_flask_api.models import Patient
from fsecond_employee_lask_api import db

def seedData():
    for seed_num in range(10):
        data = getProfile()
        employee = Employee(data['name'],\
        data['sex'],data['address'], data['ssn'], data['blood_group'],data['mail'] )

        db.session.add(employee)
        db.session.commit()
seedData()

