# 27-06-2022
# functional programming --> capable to accept and return functions

# first class function --> treated as variables / objects

# def fnc1(fnc2,fnc3):             def fnc2():             def fnc3():
#     logic                             logic                   logic
#     return fnc4                       

# function1 = fnc1(fnc2,fnc3)
# function1 --> is higher order function

students_dobs = ['21-05-1992', '05-08-1995', '14-12-2021']
curr_yr = 2022

def get_yob(dob):
    students_yob = []
    for bdate in dob:
        students_yob.append(int(bdate.split('-')[2]))
        # print(type(bdate.split('-')[2]))
    return students_yob

def get_age(age):
    ages = []
    for yr in age:
        ages.append(curr_yr - yr)
    return ages

def get_details(get_yob,get_age,dobs):
    is_major = []
    ages = get_age(get_yob(dobs))
    for age in ages:
        if(age>=18):
            is_major.append(True)
        else:
            is_major.append(False)
    return is_major

print(get_details(get_yob,get_age,students_dobs))


# map()    filter()    reduce()

# file operations

# loads()       dumps()     
#   

# functions as objects
def add(a, b):
    return a + b
plus = add
print(plus(2, 3))

# higher order functions
# passing functions as arguments
def total(list_of_num):
    return sum(list_of_num, 0)

def divide(num1, num2):
    return num1 / num2

marks = [23, 56, 89, 45, 78]

def avg(mysum, mydiv, list_of_values):
    return mydiv(mysum(list_of_values), len(list_of_values))

print(avg(total, divide, marks))


# returning functions from other functions and lambda functions
def get_marks_and_avg_fn():
    marks = [34, 56, 78, 90, 54]
    return marks, lambda marks: sum(marks)/ len(marks)

marks_list, avg_fn = get_marks_and_avg_fn()
print(avg_fn(marks_list))
print(marks_list,avg_fn(marks_list))

# higher order functions

patient_dobs = ['21-02-1981', '03-02-2006', '12-01-1950']
curr_yr = 2022

def get_yob(dobs):
    yobs = []
    for dob in dobs:
        yobs.append(int(dob.split('-')[2]))
    return yobs

def get_ages(yobs):
    ages = []
    for yr in yobs:
        ages.append(curr_yr - yr)
    return ages

def get_patient_status(get_yob, get_ages, dobs):
    is_major = []
    # yobs = get_yob(dobs)
    ages = get_ages(get_yob(dobs))
    for age in ages:
        if age >= 18:
            is_major.append(age)
    return is_major

print(get_patient_status(get_yob, get_ages, patient_dobs))