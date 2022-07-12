# 28-06-2022
# import json 
#           filename --> json file
#           mode --> read-r,write-w,execute-e
# def function():
    # with open("filename", mode(r)) as file_handle:
    #     json_data = json.load(file_handle)
    #     return json_data

# data = function()
# print(data)

# use this in other functions to update data in json

# def save_data(data):
# with open("filename",mode(w)) as json_file_handle:
#   json.dump(data,json_file_handle, indent=number) 

import json

def load_data() -> dict:
    with open('resources\patient_data.json', 'r') as patient_data_file:
        pdata = json.load(patient_data_file)
        # print(pdata)
        return pdata

def update_data(id, name, pdata):
    for patient in pdata["patients_list"]:
        print(type(patient['patient_id']))
        if patient['patient_id'] == id:
            patient["firstName"] = name

def save_data(pdata):
    with open('resources\patient_data.json', 'w') as patient_data_file:
        json.dump(pdata, patient_data_file, indent=4)

patient_data = load_data()
print(patient_data)
update_data(2, "Jill", patient_data)
print(patient_data)
save_data(patient_data)