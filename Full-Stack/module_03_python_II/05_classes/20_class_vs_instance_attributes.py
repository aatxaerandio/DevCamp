# CLASS VS INSTANCE ATTRIBUTES

#Instance attributes

"""
They are attributes of each instance
In the next example, "title" is an instance atribute, 
for all the instances it can be changed.
"""

class Website:
    def __init__(self, title):
        self.title = title
    
ws = Website("My website title")

#instance attribute -->  specific attribute of the instance itself
print(ws.__dict__)              # {"title": "My website title"}

# another example of instance attribute
ws_two = Website("Second title")    #change the attribute as the first was specific for the instance
print(ws_two.__dict__)          # {"title": "Second title"}

"""
__dict__ -> creates a dictionary with the instance attributes, in this case 
the unique attirubte is "title"
"""



#Class attributes
"""
They are attributes of the class, they are 'hard coded',
and they will have the same value for each of the instances
"""
class DifferentWebsite:
    title = "My class title"


dw = DifferentWebsite()
print(dw.__dict__)              # {}
print(dw.title)                 # My class title

dw_two = DifferentWebsite()
print(dw_two.title)             # My class title