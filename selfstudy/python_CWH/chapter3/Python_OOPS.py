# dry --> dont repeat yourself 
# PascalCase --> EmpName
# camelCase --> empName
# class name follows pascalcase

# class WkEmp:        #class declaration
#     name = "Niraj"      #variable initialization
#     surname = "Narwade"
#     def printData(self):        #method declaration
#         print(f"Name is {self.name}")
#         print(f"Surname is {self.surname}")

# emp1 = WkEmp()      #object instantiation
# # print(emp1.name)        
# emp1.surname = "NNN"        #
# # print(emp1.name)
# emp1.printData()

# emp1.name = "ND"        # only affected current instance
# emp1.printData()

# emp2 = WkEmp()
# emp2.printData()
# print("***",WkEmp.name)
# WkEmp.name = "Simba"        # affects all instances default value
# print("***",WkEmp.name)
# emp1.printData()
# emp2.printData()
# emp3 = WkEmp()
# emp3.printData()

# decorator 
# @staticmethod --> for passing more arguments other than self 


#constructor 
# __init__()
#  
# class Emp:
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal

# # niraj = Emp()       #error

# niraj = Emp("Niraj",50000)
# print(niraj.name,niraj.sal)

#create a class calculator capable to calculate square,cube,sqrt of number
# import math
# class Calculator:
#     def square(self,num):
#         return num*num
#     def cube(self,num):
#         return num*num*num
#     def sqrt(self,num):
#         return math.sqrt(num)


# cal = Calculator()
# print(cal.square(2),cal.cube(2),cal.sqrt(2))

#complete and working

