
class patient(object):
    def __init__(self, patient_id, firstName, lastName, gender, age):
        self.age = age
        self.gender = gender
        self.lastName = lastName
        self.firstName = firstName
        self.patient_id = patient_id