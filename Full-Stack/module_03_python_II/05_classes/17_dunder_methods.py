# DUNDER METHODS
"""
Are the methods that have double - in each site. 
Example:  __init__
They serve to diferentiate the methods given directly by python from 
these methods defined by us.
"""
# __str__
"""
They are usually used for debugging, as they allow us to see the differences  
between the values of the attributes from the different instances of a same class
--> For nice output, easy to read.
"""
# __repr__
"""
similar to __str__, it is used to show the raw output, but it is more used to show
directly the values, with a more "object" form.
--> For raw output, not really easy to read.
"""

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f"Infoice from {self.client} for {self.total}"

    def __repr__(self):
        return f"Invoice <value: client: {self.client}, total: {self.total}>"


inv = Invoice("Google", 100)

print(str(inv))     # Infoice from Google for 100
print(repr(inv))    # Invoice <value: client: Google, total: 100>