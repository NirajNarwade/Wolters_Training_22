from functools import reduce

patient_dobs = ['21-02-1981', '03-02-2006', '12-01-1950']
curr_yr = 2022

def get_yob(dob):
    return int(dob.split('-')[2])

patient_yobs = list(map(get_yob, patient_dobs))
print(patient_yobs)

def get_age(yob):
    return curr_yr - yob

patient_ages = list(map(get_age, patient_yobs))
print(patient_ages)

def get_adult_age(age):
    return age >= 18

# nameless or anonymous functions also known as lambda functions
# lambda <arguments> : <expression>
status = lambda age: age >= 18
print(status(36))

# adult_patient_ages = list(filter(get_adult_age, patient_ages))
adult_patient_ages = list(filter(lambda age: age >= 18, patient_ages))
print(adult_patient_ages)

# find average age of patient using reduce
# def add(age1, age2):
#     return age1 + age2

avg_patient_age = reduce(lambda age1, age2 : age1 + age2, patient_ages) / len(patient_ages)
print(avg_patient_age)


'''
from functools import reduce
# iterable
patients_dob = ['23-03-1981', '12-12-2005', '03-06-1950']
curr_yr = 2022

# function that works on a single item
def get_yob(dob):
    return dob.split('-')[2]

# map function takes the above function and applies it to each item i the iterable
patients_yob = list(map(get_yob, patients_dob))
print(patients_yob)

def find_age(yob):
    return curr_yr - int(yob)

ages = list(map(find_age, patients_yob))
print(ages)

def is_major(age):
    return age >= 18

age_status = list(map(is_major, ages))
print(age_status)

adult_patients_ages = list(filter(is_major, ages))
print(adult_patients_ages)

# reduce example
age_list = [23, 34, 45, 56]
def add(a, b):
    return a+b
age_sum = reduce(add, age_list)
print(age_sum)

def average_age1(ages):
    return reduce(add, ages) / len(ages)

def average_age2(ages):
    return reduce(lambda age1, age2: age1 + age2, ages) / len(ages)

print(average_age1(age_list))
print(average_age2(age_list))
'''