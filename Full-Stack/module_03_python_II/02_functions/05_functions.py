# FUNCIONES

""" WHAT ARE THEY FOR
- we have an input
- the function does what it needs to do
- we get an output

This process can be called later from any part of the program, 
which prevents us from having code repeated several times

SYNTAX for function that receives arguments (inputs) and returns 
data (outputs):

def function_name(inputs):
 return output

receiving and returning data is optional, but it is most common
"""

def full_name(first, last):
    print(f"{first} {last}")

full_name("Pedro", "Garcia")
full_name("Pedro", "Francés")


# another example
def auth(email, password):
    if email == "kristine@hudgens.com" and password == "secret":
        print("Authorized")
    else:
        print("Not authorized")


auth("kristine@hudgens.com", "secret")


# another example
def hundred():
    for num in range(1, 101):
        print(num)

hundred()


# another example
def counter(max):
    for num in range(1, max):
        print(num)

counter(50)



# RETURN DATA FROM A FUNCTION -> return
# this would be the actual workflow:
def return_full_name(first, last):
    return f"{first} {last}"

kristine = return_full_name("Kristine", "Hudgens")

def greeting(name):
    print(f"Hi {name}!")

greeting(kristine)