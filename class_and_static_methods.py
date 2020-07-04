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

# Employee.set_raise_amt(1.05)  # automatically takes cls
# # this is the same as setting Employee.raise_amt = 1.05
# print(emp1.raise_amount)  # = 1.05
# print(emp2.raise_amount) # = 1.05

# import datetime
# my_date = datetime.date(2020, 7, 4)
# print(Employee.is_workday(my_date)) # this day is Saturday so it returns False
