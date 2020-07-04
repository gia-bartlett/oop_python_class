Welcome to my in depth study of OOP Python classes!  
Massive thanks to Corey Schafer on Youtube for his incredibly clear and in-depth tutorials!  
https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

Why do we use classes:  
* logically group data and functions in a way that is easy to reuse.  
* Logical blocks of code are easy to build upon.  
* DRY - don't repeat yourself!  
* saves time - where code would be repeated it is imply reused.  

Terminology:  
* class = blueprint for creating instances  
* method = function within a class  
* instance = each unique instantiation (use) of the class  
* instance variables = certain data unique to each instance  
* class variables should be the same for each instance  
* print(help(arg)) - very useful for seeing chain (method resolution order)  

init method  
initialize (constructor) puts together the data you input  
self = used to refer to each instance
```
def __init__(self, first, last):
    self.first = first
    self.last = last
    self.email = first + '.' + last + "@company.com"
```

oop_tutorial.py:  
wrote a simple class allowing us to compile initial employee data instead of writing it out each time  
covered init method to take first and last names, position and pay  
also created an email within init  
created a method to create the full name of each employee  
created a method to handle annual raises with options for setting adn overriding  
played around with namespace  
created class variable to set employee numbers and created an init using the class to increse by 1 everytime a new init is run  

class_and_static_methods.py:  
added to our Employee class:  
class method to handle raises  
class methods take the class as the first argument  
```
@classmethod  # altering the functioinality of the method to receive class (cls) as first argument
    def set_raise_amt(cls, amount):
    cls.raise_amount = amount
```
static method to handle what day of the week en employee was hired  
class methods take neither the instance nor the class as the first argument  
nothing is passed automatically - included because they have a logical connection to the class  
```
@staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # Monday = 0 in Python
            return False
        return True
```

inheritance.py:  
used print(help(<'classname>)) to examine what we inherited and look at chain  
```
print(help(Developer))
``` 
edited the raise amount within Developer class to affect only the developers  

added an init so that we can add some more attributes that are relevant only to Developers  
We keep the inits from the Employee and add to it using two options  
```
super().__init__(everything except self)
Employee.__init__(everything including self)
```
SUPER.init is used for single inheritance  
CLASS.init is used for multiple inheritance

created another class for Office Plants:  
played with is and not  
```
if employees is None:
    self.employees = []
```
__IS__ keyword is used to test if two variables refer to the same object  
(here testing if the object none)  

Test class of code
* isinstance  
* issubclass  
```
print(isinstance(plt1, Office_Plants))  
# print True because plt1 is created by Office Plants class
print(isinstance(plt1, Employee))  
# print True because plt1 inherited from Parent class Employee
print(isinstance(plt1, Developer))  
# print False even though they both inherit from Employee plt does not inherit from Developer in any way
print(issubclass(Developer, Employee))  
# True because Developer class inherits from Parent Employee class
print(issubclass(Office_Plants, Developer))  
# False because Oppice Plants does not inherit from Developer
```
__Magic Methods__  
```
print(1 + 2) = 3
print("a" + "b") = ab
print(emp1) = <__main__.Employee object at 0x00000218B2BC2190>
```
using + actually uses a built in magic method that we don't have to type out each time  
dunder add
```
# print(len("test")) = 4
is the same as:
print("test".__len__()) = 4
```
* repr  
is an unambiguous representation of the object  
should be used for debugging and logging  
designed to be seen by other developers  


```
def __repr__(self):
```

* str
is a readable representation of the object  
should be used as a display to the end user
```
def __str__(self):
```
then when you use print(object)  
it will default to the str version you set in the code  
each can still be accessed using repr(object) and str(object) to directly call the special method  
