
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
emp2 = Employee("Albert", "Palm", "PlantCTO", 11000001)


class Developer(Employee):
    raise_amount = 4

    def __init__(self, first, last, position, pay, prog_lang):
        super().__init__(first, last, position, pay) # copies the init code from above


dev1 = Developer("James", "Knight", "Sensei", 1000001)
dev2 = Developer("Georgina", "Bartlett", "Kohai", 20)  # will try to init via Developer but as
# there is no init it will move up the chain til it finds what it is looking for
print(dev1.email)

#  print(help(Developer))

print(dev1.pay)
dev1.annual_raise()  # applied the class variable raise of 2 first time round and printed = 28 but then we added
# a raise to the Developer class so it applies that one instead and printed = 56
# it's still using the method from Employee to calculate
print(dev1.pay)
print(emp1.pay) = 20