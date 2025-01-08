import random

class Employee:

    company = {
        "JPS": {
            "Parttime": {"Wage": 10, "days": 18, "hours": 60},
            "Fulltime": {"Wage": 20, "days": 18, "hours": 60}
        },
        "KITS": {
            "Parttime": {"Wage": 30, "days": 19, "hours": 90},
            "Fulltime": {"Wage": 50, "days": 19, "hours": 90}
        },
        "AOPS": {
            "Parttime": {"Wage": 25, "days": 16, "hours": 70},
            "Fulltime": {"Wage": 40, "days": 16, "hours": 70}
        },
        "ITYS": {
            "Parttime": {"Wage": 20, "days": 20, "hours": 50},
            "Fulltime": {"Wage": 30, "days": 20, "hours": 50}
        }
    }
    
    print("______Welcome Employee Wage Problem_______")
    
    def __init__(self, name, company, attendance, type_emp, days, hours):
        self.name = name
        self.attendance = attendance
        self.company = company
        self.type_emp = type_emp
        
        self.key = Employee.get_company_info(self.company, self.type_emp)  # Using class method here
        
        while self.key["hours"] < hours or self.key["days"] < days:
            print("Error: Working days or hours exceed the company's limits.")
            print(f"Allowed Days: {self.key['days']}, Allowed Hours: {self.key['hours']}")
            days = int(input("Re-enter working days: "))
            hours = int(input("Re-enter working hours: "))
        
        # Set the valid days and hours
        self.days = days
        self.hours = hours
        print(f"Employee {self.name} registered successfully at {self.company} as {self.type_emp}.")
    
    @classmethod
    def get_company_info(cls, company, type_emp):
        """Class method to get company wage info."""
        return cls.company.get(company, {}).get(type_emp, {})
    
    def check_attendance(self):
        if self.attendance:
            return f"{self.name} is PRESENT"
        return f"{self.name} is ABSENT"
    
    def daily_wage(self):
        daily_wage = self.key["Wage"] * self.hours
        return f"Hello {self.name}, your daily wage is {daily_wage} INR based on {self.hours} hours worked."
    
    def monthly_wages(self):
        self.wage = self.key["Wage"] * self.hours * self.days
        return f"{self.name} has monthly salary of {self.wage} INR."
    
def display_menu():
    print("\n------ Employee Wage Management System ------")
    print("1. Add Employee")
    print("2. Check Attendance")
    print("3. Calculate Daily Wage")
    print("4. Calculate Monthly Wage")
    print("5. Exit")
    
def main():
    employees = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter Employee Name: ")
            company = input("Enter Company Name (JPS, KITS, AOPS, ITYS): ")
            attendance = random.randint(0, 1)  # Random attendance status
            type_emp = input("Enter Employee Type (Parttime, Fulltime): ")
            days = int(input("Enter working days: "))
            hours = int(input("Enter working hours: "))
            
            emp = Employee(name, company, attendance, type_emp, days, hours)
            employees.append(emp)
            
        elif choice == "2":
            if not employees:
                print("No employees registered yet.")
            else:
                name = input("Enter Employee Name to check attendance: ")
                found = False
                for emp in employees:
                    if emp.name == name:
                        print(emp.check_attendance())
                        found = True
                        break
                if not found:
                    print(f"No employee found with the name {name}.")
        
        elif choice == "3":
            if not employees:
                print("No employees registered yet.")
            else:
                name = input("Enter Employee Name to calculate daily wage: ")
                found = False
                for emp in employees:
                    if emp.name == name:
                        print(emp.daily_wage())
                        found = True
                        break
                if not found:
                    print(f"No employee found with the name {name}.")
        
        elif choice == "4":
            if not employees:
                print("No employees registered yet.")
            else:
                name = input("Enter Employee Name to calculate monthly wage: ")
                found = False
                for emp in employees:
                    if emp.name == name:
                        print(emp.monthly_wages())
                        found = True
                        break
                if not found:
                    print(f"No employee found with the name {name}.")
        
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
