import sqlmanager as DbManager
from patient import patient

# DbManager.create_table()


def show_main_menu():
    print("1: Patient menu")
    # print("2: Appointment menu")
    choice = int(input())
    match choice:
        case 1:
            show_patient_menu()
        case 2:
            show_appointment_menu()
        case default:
            print("Incorrect Input.")


def show_patient_menu():
    print('1: Add a new Patient')
    print('2: Update an existing patient')
    print('3: Delete an existing patient')
    print('4: Delete all patients')
    print('5: View by name')
    print('6: View all patients')
    print('7: Exit')
    choice = int(input())
    match choice:
        case 1:
            print("Enter patient id: ")
            p_id = int(input())
            print("Enter first name: ")
            fname = input()
            print("Enter last name: ")
            lname = input()
            print("Enter Gender: ")
            gender = input()
            print("Enter age: ")
            age = int(input())
            patient_p = patient(p_id, fname, lname, gender, age)
            DbManager.insert_patient(patient_p)
            show_patient_menu()
        case 2:
            print(DbManager.get_all_patients())
            print("Enter patient id to update patient age: ")
            patient_id = int(input())
            print("Enter new age: ")
            age = int(input())
            DbManager.update_patient_age(patient_id, age)
            show_patient_menu()
        case 3:
            print(DbManager.get_all_patients())
            print("Enter patient id to delete patient: ")
            patient_id = int(input())
            DbManager.delete_patient(patient_id)
            show_patient_menu()

        case 4:
            print("Are you sure you want to delete all patients (y/n): ")
            decision = input()

            if decision == 'y':
                DbManager.delete_all_patient()
            elif decision == 'n':
                show_patient_menu()
            else:
                print("Wrong choice!")

            show_patient_menu()
        case 5:
            print("Enter name to view patient details: ")
            name = input()
            print(DbManager.get_patient_by_name(name))
            show_patient_menu()
        case 6:
            print(DbManager.get_all_patients())
            show_patient_menu()
        case 7:
            print("Thank You for Using This App")
            pass

        case default:
            print("Incorrect Input.")


def show_appointment_menu():
    pass


show_main_menu()