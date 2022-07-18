import sqlmanager as DbManager
from patient import patient

# DbManager.create_table()


def show_main_menu():
    print("Choose 1 for patient menu")
    print("Choose 2 for Appointment menu")
    choice = int(input())
    match choice:
        case 1:
            show_patient_menu()
        case 2:
            show_appointment_menu()
        case default:
            print("Incorrect Input.")


def show_patient_menu():
    print('Choose 1 to add a new Patient')
    print('Choose 2 to update an existing patient')
    print('Choose 3 to delete an existing patient')
    print('Choose 4 to delete all patients')
    print('Choose 5 to view by name')
    print('Choose 6 to view all patients')
    print('Choose 7 to exit')
    choice = int(input())
    match choice:
        case 1:
            print("Enter patient id")
            p_id = int(input())
            print("Enter first name: ")
            fname = input()
            print("Enter last name : ")
            lname = input()
            print("Enter Gender : ")
            gender = input()
            print("Enter age :")
            age = int(input())
            patient_p = patient(p_id, fname, lname, gender, age)
            DbManager.insert_patient(patient_p)
            show_patient_menu()
        case 2:
            print(DbManager.get_all_patients())
            print("Enter patient id to update patient age :")
            patient_id = int(input())
            print("Enter new age : ")
            age = int(input())
            DbManager.update_patient_age(patient_id, age)
            show_patient_menu()
        case 3:
            print(DbManager.get_all_patients())
            print("Enter patient id to delete patient :")
            patient_id = int(input())
            DbManager.delete_patient(patient_id)
            show_patient_menu()

        case 4:
            print("Are you sure you want to delete all patients (y/n): ")
            decision = input()

            if decision == 'y':
                DbManager.delete_all_patient()
            else:
                show_patient_menu()

            show_patient_menu()
        case 5:
            print("Enter name to view patient details:")
            name = input()
            print(DbManager.get_patient_by_name(name))
            show_patient_menu()
        case 6:
            print(DbManager.get_all_patients())
            show_patient_menu()
        case 7:
            pass

        case default:
            print("Incorrect Input.")


def show_appointment_menu():
    pass


show_main_menu()