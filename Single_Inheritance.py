class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)

class Salary(Employee):
    def calculate_salary(self, basic):
        print("Salary:", basic + 5000)

emp = Salary("Amit")
emp.show()
emp.calculate_salary(15000)