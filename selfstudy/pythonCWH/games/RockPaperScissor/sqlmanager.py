import sqlite3

conn = sqlite3.connect('selfstudy/pythonCWH/games/RockPaperScissor/userdb.db')


cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE users(
                    name text, 
                    score integer
                    )""")

def insert_user(user_u):
    with conn:
        cursor.execute("INSERT INTO users VALUES(:name, :score)",
                       {'name': user_u.name,
                        'score': 0})


def get_user_by_name(name):
    cursor.execute("SELECT * FROM users WHERE name=:name1", {'name1': name})
    return cursor.fetchall()


def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


def update_user_score(name, score):
    with conn:
        cursor.execute("""UPDATE users SET score = :score1 WHERE name = :name1 """,
                       {'name1': name, 'score1': score })


# def delete_patient(patient_id):
#     with conn:
#         cursor.execute("DELETE from patients WHERE patient_id = :patient_id",
#                        {'patient_id': patient_id})


# def delete_all_patient():
#     with conn:
#         cursor.execute("DELETE from patients ")