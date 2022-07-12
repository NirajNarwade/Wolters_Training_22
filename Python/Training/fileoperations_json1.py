import json

def show_main_menu():
	print('Choose 1 for Patient menu')
	print('Choose 2 for Appointment menu')
	choice = int(input())
	match choice:
		case 1:
			show_patient_menu()
		case 2:
			show_appointment_menu()

def show_patient_menu():
	print('Choose 1 to add a new Patient')
	print('Choose 2 to update an existing patient')
	print('Choose 3 to delete an existing patient')
	choice = int(input())
	match choice:
		case 1:
			patient_data = load_data()
			add_patient(patient_data)
			save_data(patient_data)
		case 2:
			edit_patient()
		case 3:
			delete_patient()
		case default:
			print("Incorrect Input.")

def show_appointment_menu():
	pass

def add_patient(pdata):
	patient_id = 3
	firstName =  "Thomas"
	lastName = "Jackson"
	gender = "male"
	age = 28

	patient = {}
	patient["patient_id"] = patient_id
	patient["firstName"] = firstName
	patient["lastName"] = lastName
	patient["gender"] = gender
	patient["age"] = age

	pdata["patients_list"].append(patient)

def display_patient_data(pdata):
	plist = pdata["patients_list"]
	for p in plist:
		print(f"Patient ID: {p['patient_id']}")
		print(f"Patient Name: {p['firstName']}")

def edit_patient():
	pdata = load_data()
	display_patient_data(pdata)
	pid = int(input("Enter the ID of the patient to be edited: "))
	confirmation = input(f"Are you sure you want to edit the info of patient with ID {pid} (yes/ no)?")
	if confirmation == "yes":
		print("Editing info.")

def delete_patient():
	pass

def load_data():
	with open("resources\patient_data.json", 'r') as json_file_handle:
		json_data = json.load(json_file_handle)
	return json_data

def update_data(id, name, pdata):
	for patient in pdata["patients_list"]:
		if patient["patient_id"] == id:
			patient["firstName"] = name

def save_data(pdata):
	with open("resources\patient_data_new.json", 'w') as json_file_handle:
		json.dump(pdata, json_file_handle, indent=8)

show_main_menu()

# patient_data = load_data()
# display_patient_data(patient_data)
# print(patient_data)
# # print(patient_data["patients_list"][0])
# update_data(1, "Thomas", patient_data)
# print(patient_data)
# save_data(patient_data)