import random
class Employee:
    print("______Welcome Employee Wage Problem_______")
    def __init__(self, name, attendance, type_emp, hrs, days):
        self.name = name
        self.attendance = attendance
        self.wage = None
        self.hours = hrs
        self.days = days
        self.type_emp = type_emp
        self.working_days = 20
    
    def check_attendance(self):
        if self.attendance:
            return f"{self.name} is PRESENT"
        return f"{self.name} is ABSENT"
    
    def calculate(self):
        if self.type_emp.lower() == "part":
            if self.days <= 20 and self.hours <= 100:
                self.wage = self.hours * self.days * 15
                daily_wage = self.hours * 15
            else:
                return "Not Eligible"
        else:
            if self.days <= 20 and self.hours <= 100:
                self.wage = self.hours * self.days * 20
                daily_wage = self.hours * 20
            else:
                return "Not Eligible"
            
        return f"{self.name} earns {daily_wage}rs. daily"
    
    def monthly_wages(self):
        return f"{self.name} has monthly salary of {(self.wage)}"
    
emp1 = Employee("John", random.randint(0,1), "Part", 100, 20)
print(emp1.check_attendance())
print(emp1.calculate())
print(emp1.monthly_wages())
