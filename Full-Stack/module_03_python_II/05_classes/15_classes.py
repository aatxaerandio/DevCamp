# CLASSES
"""
We use classes to encapsulate data (attributes) and funcitons (methods) that have a close
relationship between them in an object.

In python is really usefull to use the first letter as a capital letter
to diferentiate and to see that it is a CLASS.

class Name:
    some_code

    def method(self):
        more_code

classes can have data or funciton inside them.
"""


class Invoice:
    def greetings(self):   #method of the class --> always pass 'self' to the methods
        return "Hi there"
    
"""
We need the "instantiation"  --> Create and object with the class
"""

inv_one = Invoice()
print(inv_one)

#If we run python invoice.py it will output --> <__main__.Invoice object at 0x00000167F5F0B460> -> pointer to the object created

inv_two = Invoice()
print(inv_two)     # <__main__.Invoice object at 0x0000023C92A2B430>

print(inv_two.greeting())


"""
CODING EXERCISE

Create a class named Garage. Add a method to the Garage class named open_door that returns a string 
(EX: "The door opens").
Finally, instantiate a new object named home. You do not need to print anything.
"""
class Garage:
  def open_door(self):
    return "The door opens"

home = Garage()


# CONSTRUCTOR __init__

# __init__ --> special reserved function inside of the python language. Automatically called when ever you instantiate. Process everything inside of it. The very argument is self and then others.
#After add the data to the class

class Invoice:
  def __init__(self, client, total):
    self.client = client    #create variables related directly to the instance
    self.total = total

  def formatter(self):
    return f"{self.client} owes: ${self.total}"

google = Invoice("Google", 100)
snapchat = Invoice("Snapchat", 200)

print(google.formatter())    # Google owes: $100
print(snapchat.formatter())    # Snapchat owes: $200

""""
CODING EXERCISE

Using our Garage class from the previous guide, add a constructor method 
that builds a property named size, which will represent how many cars will 
fit in the garage as an integer. Instantiate the home object to be a 2 car
garage.
"""
class Garage:
  def __init__(self, size):
    self.size = size

  def open_door(self):
    return "The door opens"

home = Garage(2)


# GETTER and SETTER functions
"""
This functions are by own, you do not have to worry about creating them.
"""
class Invoice3:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def formatter(self):
    return f"{self.client} owes: ${self.total}"


google = Invoice3("Google", 100)

# get the data -> getter
print(google.client)            # Google
print(google.total)             # 100

# modify the data -> setter
google.client = "Yahoo"
print(google.client)            # Yahoo
print(google.total)             # 100


""""
CODING EXERCISE

We've added an array of cars to our garage. All of the vehicles 
are out for the day, and we need to update the array. Now that 
you've seen getters and setters, use a setter to update the cars
 array to reflect all cars being gone. Then, in the get_cars 
 variable, get the cars data from the home object.
"""
# Starter code
class Garage:
  def __init__(self, size):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"

home = Garage(2)
# End of starter code

# Setter goes here
home.cars = []

get_cars = home.cars


