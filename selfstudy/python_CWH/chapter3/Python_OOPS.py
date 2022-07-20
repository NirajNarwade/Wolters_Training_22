# dry --> dont repeat yourself 
# PascalCase --> EmpName
# camelCase --> empName
# class name follows pascalcase

class WkEmp:        #class declaration
    name = "Niraj"      #variable initialization

    def printData(self):        #method declaration
        print(f"Name is {self.surname}")

emp1 = WkEmp()      #object instantiation
print(emp1.name)        
emp1.surname = "Narwade"        #
print(emp1.name)
emp1.printData()