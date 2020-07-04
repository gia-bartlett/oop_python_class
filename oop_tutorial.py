
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
        Employee.num_of_emp += 1  # set in the init because the init runs each instance
        # Employee is used instead of self because we are never going ot want/need to override this


    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def annual_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        # by referencing the class variable (raise_amount) this will ALWAYS reference
        # that even if the instance has been changed
        self.pay = int(self.pay * self.raise_amount)
        # If this isn't otherwise set it will default to the class but can be set individually
    @classmethod  # altering the functioinality of the method to receive class (cls) as first argument
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # Monday = 0 in Python
            return False
        return True


#print(Employee.num_of_emp)  # = 0
emp1 = Employee("Georgina", "Bartlett", "Kohai", 20)
emp2 = Employee("James", "Knight", "Sensei", 1000001)
#print(Employee.num_of_emp)  # = 2
# each instance of Employee will take a different piece of memory

# writing out each employee would take a long time

#print(emp1.email)
#print(emp2.email)

# print("{} {}".format(emp1.first, emp1.last))
# this is a lot of code to write each time you want to print your employees' full name
# what if you have 10,000 employees?
# so we'll create a method

#print(emp2.full_name())  # if calling the method when using an instance it doesn't need an argument
#print(Employee.full_name(emp1))  # calling the method on the class it needs the instance entering

#print(emp1.raise_amount)  # set at 2
#print(emp1.pay)  # current pay = 20
#emp1.annual_raise()  # apply raise class variable
#print(emp1.pay)  # new pay = 40

#lets give George a massive payrise!

#emp1.raise_amount = 10000  # overriding the class set value
#print(emp1.raise_amount)  # = now set at 10000 but this will only work if self.raise_amount is used in class
#print(emp2.raise_amount)  # = still set at default which is 2

#emp1.annual_raise()

#print(emp1.pay)

#print(emp1.__dict__) # namespace
# {'first': 'Georgina', 'last': 'Bartlett', 'position': 'Kohai', 'pay': 40, 'email': 'Georgina.Bartlett@company.com'}

# Employee.set_raise_amt(1.05)  # automatically takes cls
# # this is the same as setting Employee.raise_amt = 1.05
# print(emp1.raise_amount)  # = 1.05
# print(emp2.raise_amount) # = 1.05

# import datetime
# my_date = datetime.date(2020, 7, 4)
# print(Employee.is_workday(my_date)) # this day is Saturday so it returns False


class Developer(Employee):
    pass

dev1 = Developer("Hector", "Bartlett", "Dog", 1400000000)
print(dev1.email)