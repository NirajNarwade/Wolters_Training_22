class Emp:
    company = "wk"
    salary = 75000
    bonus = 15000

    @property
    # total salary is not function its a property
    def totalSalary(self):
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.bonus = val - self.salary


e = Emp()
print(e.totalSalary)
e.totalSalary = 120000
print(e.totalSalary)
print(e.bonus)
print(e.salary)
