import sqlite3

conn = sqlite3.connect('.\Python\Assignments\patientapp\patient.db')

cursor = conn.cursor()


def create_table():
    cursor.execute("""CREATE TABLE patients(
                    patient_id integer, 
                    firstname text, 
                    lastname text, 
                    gender text, 
                    age integer
                    )""")


def insert_patient(patient_p):
    with conn:
        cursor.execute("INSERT INTO patients VALUES(:patient_id, :firstname, :lastname, :gender, :age)",
                       {'patient_id': patient_p.patient_id, 'firstname': patient_p.firstName,
                        'lastname': patient_p.lastName,
                        'gender': patient_p.gender, 'age': patient_p.age})


def get_patient_by_name(name):
    cursor.execute("SELECT * FROM patients WHERE firstname=:firstname", {'firstname': name})
    return cursor.fetchall()


def get_all_patients():
    cursor.execute("SELECT * FROM patients")
    return cursor.fetchall()


def update_patient_age(patient_id, age):
    with conn:
        cursor.execute("""UPDATE patients SET age = :age WHERE patient_id = :patient_id """,
                       {'patient_id': patient_id, 'age': age, })


def delete_patient(patient_id):
    with conn:
        cursor.execute("DELETE from patients WHERE patient_id = :patient_id",
                       {'patient_id': patient_id})


def delete_all_patient():
    with conn:
        cursor.execute("DELETE from patients ")