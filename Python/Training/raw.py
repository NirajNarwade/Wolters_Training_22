# 27-06-2022
# functional programming --> capable to accept and return functions

# first class function --> treated as variables / objects

# def fnc1(fnc2,fnc3):             def fnc2():             def fnc3():
#     logic                             logic                   logic
#     return fnc4                       

# function1 = fnc1(fnc2,fnc3)
# function1 --> is higher order function

# students_dobs = ['21-05-1992', '05-08-1995', '14-12-2021']
# curr_yr = 2022

# def get_yob(dob):
#     students_yob = []
#     for bdate in dob:
#         students_yob.append(int(bdate.split('-')[2]))
#         # print(type(bdate.split('-')[2]))
#     return students_yob

# def get_age(age):
#     ages = []
#     for yr in age:
#         ages.append(curr_yr - yr)
#     return ages

# def get_details(get_yob,get_age,dobs):
#     is_major = []
#     ages = get_age(get_yob(dobs))
#     for age in ages:
#         if(age>=18):
#             is_major.append(True)
#         else:
#             is_major.append(False)
#     return is_major

# print(get_details(get_yob,get_age,students_dobs))


# map()    filter()    reduce()

# file operations

# loads()       dumps()     
#                           
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
# 
#  
