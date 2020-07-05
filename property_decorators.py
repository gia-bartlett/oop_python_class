class Employee:

    def __init__(self, first, last, position, pay):
        self.first = first
        self.last = last
        self.position = position
        self.pay = float(pay)

    @property  # allows us to define the class like it is a method but access it like an attribute
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
        # adding in a email method would mess up everyone else's code

    @property
    def full_name(self):  # can't be edited like emp1.first as it depends on the initial entries
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):  # name value is the value we want to set
        first, last = name.split(" ")  # part before the split will be first and part after split will be last
        self.first = first
        self.last = last

    @full_name.deleter  # this will print Delete name! and set the name values to None
    # (effectively deleting that instance)
    def full_name(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp1 = Employee("Georgina", "Bartlett", "Kohai", 20)
emp2 = Employee("James", "Knight", "Sensei", 1000001)

emp1.first = "George"  # will print first and full name as George but not email

emp1.full_name = "George Bartlett" # this won't work because full_name is a method that relies on the init'