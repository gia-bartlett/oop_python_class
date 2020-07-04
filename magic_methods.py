
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

    #  print(emp1) = <__main__.Employee object at 0x00000218B2BC2190> this is a bit vague and unhelpful
    #  you should always include a repr
    def __repr__(self):  # unambiguous representation of the object
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay) # creating something that can be pasted back into Python
        # a string the we can use to recreate the object
    #  if you don't have a repr then Python will default to repr
    def __str__(self):  # readable representation of the object
        return '{} - {}'. format(self.full_name(), self.email)

    def __add__(self, other):  # self on one side of the add and other on the other
        return self.pay + other.pay

    def __len__(self):  # len(emp1) to call
        return len(self.full_name())


emp1 = Employee("Hector", "Bartlett", "DogCEO", 1400000000)
emp2 = Employee("Albert", "Palm", "PlantCPO", 11000001)

#  repr(emp1) - "Employee('Hector', 'Bartlett', 1400000000.0)" this can be copied back to recreate the object
#  str(emp1) - 'Hector Bartlett - Hector.Bartlett@company.com' this is readable to the end user
# print(emp1 + emp2) - 1411000001.0
# print(len("test")) = 4 is the same as print("test".__len__())