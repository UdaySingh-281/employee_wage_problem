import random
class Employee:
    print("______Welcome Employee Wage Problem_______")
    def __init__(self, name, attendance):
        self.name = name
        self.attendance = attendance
    
    def check_attendance(self):
        if self.attendance:
            return f"{self.name} is PRESENT"
        return f"{self.name} is ABSENT"
    
emp1 = Employee("John", random.randint(0,1))
print(emp1.check_attendance())