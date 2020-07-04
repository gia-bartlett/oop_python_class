
class Employee:
    # pass # allows you to leave the function empty until you need to use it
    num_of_emp = 0 # class variable (each time we create a new employee this will increase by 1)
    raise_amount = 2 # declare a class variable up here

    def __init__(self, first, last, position, pay):
        self.first = first
        self.last = last
        self.position = position
        self.pay = float(pay)
        self.email = first + '.' + last + "@company.com"
        Employee.num_of_emp += 1


    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def annual_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee("Hector", "Bartlett", "DogCEO", 1400000000)
emp2 = Employee("Albert", "Palm", "PlantCPO", 11000001)


class Developer(Employee):  # subclass for devs
    raise_amount = 4

    def __init__(self, first, last, position, pay, prog_lang):
        super().__init__(first, last, position, pay) # copies the init code from above and allows it to handle the input
        self.prog_lang = prog_lang

dev1 = Developer("James", "Knight", "Sensei", 1000001, "SQL")
dev2 = Developer("Georgina", "Bartlett", "Kohai", 20, "Python")  # will try to init via Developer but as
# there is no init it will move up the chain til it finds what it is looking for

class Office_Plants(Employee):  # subclass for which office plant sits on whose desk

    def __init__(self, first, last, position, pay, employees = None):
        super().__init__(first, last, position, pay)
        if employees is None:  # is keyword is used to test if two variables refer to the same object (here testing if the object none)
            self.employees = [] # if none then equal to an empty list
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:  # if employee is not in employees list
            self.employees.append(emp)  # then add them to it

    def remove_employee(self, emp):
        if emp in self.employees:  # if employee is in employees list
            self.employees.remove(emp)  # then remove them from to it

    def print_on_desk(self):
        for emp in self.employees:  # iterate through the list of employees
            print("--> ", emp.full_name())  # referring back to method in Employees parent class



# print(dev1.email)
#
# #  print(help(Developer))
#
# print(dev1.pay)
# dev1.annual_raise()  # applied the class variable raise of 2 first time round and printed = 20 but then we added
# # a raise to the Developer class so it applies that one instead and printed = 80
# # it's still using the method from Employee to calculate
# print(dev1.pay)
# print(emp1.pay)  # = 140
#
# print(dev1.email)  # uses the super init to create the email
# print(dev1.prog_lang)  # SQL - found this in Developer init

plt1 = Office_Plants("Susan", "Spoder", "Spider Plant", 1, [dev1])
plt2 = Office_Plants("Penny", "Pacem", "Peace Lily", 2, [emp2])
plt3 = Office_Plants("Montgomery", "Fromage", "Monstera", 1, [emp1])
plt4 = Office_Plants("Gemma", "Geranium", "Pelargonium", 1, [dev2])

plt1.add_employee(dev2)
plt1.remove_employee(dev2)


# print(isinstance(plt1, Office_Plants))  # print True
# print(isinstance(plt1, Employee))  # print True
# print(isinstance(plt1, Developer))  # print False even though they both inherit from Employee
# plt does not link to Developer in any way
# print(issubclass(Developer, Employee)) # True
# print(issubclass(Office_Plants, Employee)) # False