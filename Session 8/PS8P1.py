# comment - Lilien Yousefi

# employee class:
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.annual_salary

    def get_bonus(self):
        return 0.10 * self.annual_salary

# derived manager class:
class Manager(Employee):
    def get_bonus(self):
        return 0.20 * self.annual_salary

    def get_long_term_bonus(self):
        return 0.50 * self.annual_salary


def main():
    role = input("Are you an employee or manager? ").strip().lower()
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    salary = float(input("Enter your annual salary: "))


    if role == "manager":
        person = Manager(first_name, last_name, salary)
        print("Name:", person.get_full_name())
        print("Annual Salary:", person.get_annual_salary())
        print("Bonus (20%):", person.get_bonus())
        print("Long-Term Bonus (50%):", person.get_long_term_bonus())
    else:
        person = Employee(first_name, last_name, salary)
        print("Name:", person.get_full_name())
        print("Annual Salary:", person.get_annual_salary())
        print("Bonus (10%):", person.get_bonus())

if __name__ == "__main__":
    main()
