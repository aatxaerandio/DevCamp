# INHERITANCE --> Class heritance / Herencia de clases

#PARENT class
class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f"Hi {self.first_name} {self.last_name}"

#CHILD class --> "User" is its parent!
class AdminUser(User):
    def active_users(self):
        return "500"

tiffany = AdminUser("email_tif.com", "Tiffany", "Hudgens")
kristine = User("email_kri.com", "Kristine", "Hudgens")

print(tiffany.active_users())        # 500
#print(kristine.active_users())        # Attribute Error --> 

print(tiffany.greeting())               # Hi Tiffany Hudgens
print(kristine.greeting())              # Hi Kristine Hudgens

"""
Child classes can access attributes and methods of parent classes, 
but not the other way around.

To create a child class, if the parent class had some type of constructor,
they need the attributes of the constructor to be created
"""