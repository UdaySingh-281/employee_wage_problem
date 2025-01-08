import random
class Employee:
    print("______Welcome Employee Wage Problem_______")
    def __init__(self, name, attendance, type_emp):
        self.name = name
        self.attendance = attendance
        self.daily_wage = None
        self.type_emp = type_emp
    
    def check_attendance(self):
        if self.attendance:
            return f"{self.name} is PRESENT"
        return f"{self.name} is ABSENT"
    
    def calculate(self):
        if self.type_emp.lower() == "part":
            self.daily_wage = 15 * 8
        else: 
            self.daily_wage = 20 * 8
        return f"{self.name} earns {self.daily_wage}rs. daily"
    
emp1 = Employee("John", random.randint(0,1), "Part")
print(emp1.check_attendance())
print(emp1.calculate())