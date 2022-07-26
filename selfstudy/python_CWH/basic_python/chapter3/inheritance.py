# Inheritance
# single level
# multiple
# multilevel

# single inheritance
# class Emp:
#     company="WK"

#     def showDetails(self):
#         print("this is an employee")

# class Programmer(Emp):
#     lang = "Python"
#     def getLang(self):
#         print(f"language is {self.lang}")

#     def showDetails(self):
#         print("this is a programmer")

# e = Emp()
# e.showDetails()
# p=Programmer()
# p.getLang()
# p.showDetails()
# print(p.company)

# multiple inheritance
# class Employee:
#     comp = "Wolters Kluwer"

# class Freelancer:
#     comp = "Google"
#     level = 3

#     def upgradeLevel(self):
#         self.level = self.level + 1

# class Programmer(Employee, Freelancer):
#     name = "Niraj"

# p = Programmer()
# print(p.comp)
# print(p.level)
# p.upgradeLevel()
# print(p.level)
# print(p.name)

# multilevel inheritance
class Person:
    pname = "Niraj"

    def eat(self):
        print(f"{self.pname} is eating")


class Employee1(Person):
    org = "WK"
    salary = 75000

    def getSalary(self):
        print(f"salary of {self.pname} is {self.salary}")

    def getOrg(self):
        print(self.org)
# e = Employee1()
# e.eat()
# e.getSalary()


class Programmer(Employee1):
    id = 1
    org = "Microsoft"

    def getOrg(self):
        print(self.org, super().org)

    def getSalary(self):
        return super().getSalary()

    # def changeSalary(self,amt):       #changes only instance attribute
    #     self.salary = amt

    # def changeSalary(self,amt):       #now changes class attribute also
    #     self.__class__.salary = amt

    @classmethod  # deorator
    def changeSalary(cls, amt):  # alternative
        cls.salary = amt


p = Programmer()
p.eat()
p.getSalary()
p.getOrg()
p.changeSalary(90000)
p.getSalary()
print(Programmer.salary)
# class methods
