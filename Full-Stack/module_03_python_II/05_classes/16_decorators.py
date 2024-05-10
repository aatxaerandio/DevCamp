# PROPERTIES AND DECORATORS
"""
to create PROTECTED attributes --> _
to create PRIVATE attributes --> __

If you want to have something protected we will put a _ (an underscore) before.
If you want to have something private we will put two __ before.
"""
"""
As they are protected attributes, we cannot access them 
from outside the class, but by doing this with @property,
we can create methods that have the name of the attribute
and obtain their values from outside (getters)
"""

class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property    # decorator = it wraps around the property.  # GETTER
    def client(self):
        return self._client

    @client.setter      # SETTER
    def client(self, client):
        self._client = client

    @property          # GETTER
    def total(self):
        return self._total

"""
GETTER SINTAXIS:
@property
def attribute(self):
    return self._attribute

SETTER SINTAXIS:
@attribute.setter
def attribute(self, attribute):
    self._attribute = attribute
"""

google = Invoice('Google', 100)
print(google.formatter())               # Google owes: $100

#Obtain the values of the protected attributes thanks to @property
print(google.client)    # Google
print(google.total)    # 100
#Modify the values with setter
google.client = 'Yahoo'     #modification
print(google.client)    # Yahoo







"""
CODING EXERCISE

We want to ensure that our size attribute can be retrieved, but not set.
Use the appropriate syntax to protect the size attribute. Then, use the
'property' decorator to build a getter to return the protected data. 
You do not need to instantiate the class.
"""
class Garage:
  def __init__(self, size):
    #   Protect the size attribute
    self._size = size
    self.cars = []

  # add decorator here
  @property
  def size(self):
    return self._size

  
  def open_door(self):
    return "The door opens"