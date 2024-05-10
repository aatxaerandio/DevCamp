# DEFAULT ARGUMENTS
#
def greeting(name = "Guest"):
    print(f"Hi {name}!")


greeting()             # Hi Guest!
greeting("Cris")       # Hi Crist!

"""
NEVER use a list as the default value in a function, because it saves the reference
to that list in memory and if you call the function from two different places in
the program (even from another file), you will be calling the same list as before, 
so you will think it is an empty list, but you had already used it before, it will 
already have the data stored from the first time you called it.
"""



# NAMED FUNCTION ARGUMENTS
def full_name(first, last):
    print(f"{first} {last}")


full_name("Pedro", "Garcia")                     # Pedro Garcia
full_name(last="Garcia", first="Pedro")          # Pedro Garcia
full_name(first="Pedro", last="Garcia")          # Pedro Garcia

"""
Whenever the function has more than 2 arguments, it is recommended to use named 
arguments, to ensure that they are not accidentally sent to another argument.
"""



# FUNCTION ARGUMENT UNPACKING
def greeting2(time_of_day, *args):          # first argument = time_of_day, the rest of the arguments = args
    print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting2("Morning", "Tiffany", "Hudgens")
# Hi Tiffany Hudgens, I hope that you're having a good Morning
greeting2("Afternoon", "Kristine", "M", "Hudgens")
# Hi Kristine M Hudgens, I hope that you're having a good Afternoon

"""
No matter how many arguments we pass to the function, it will always take them all 
and put them together, separating them by a space

functions that have * in an argument will cause that argument to behave like a tuple

The argument can be called in any way with *, but as a general rule in Python, it 
is usually called 'args'
"""



# KEYWORD ARGUMENTS IN FUNCTIONS -> combination between arg. unpacking and named arg.
def greeting3(**kwargs):
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
    else:
        print("Hi Guest, have a great day!")


greeting3(first_name = "Kristine", last_name = "Hudgens")
# Hi Kristine Hudgens, have a great day!
greeting3()
# Hi Guest, have a great day!

"""
Functions that have ** in an argument will make that argument behave like a dictionary. 
When the function is called, names are assigned to the variables, and these are treated 
as keys of the dictionary.

example:

greeting3(first_name = "Kristine", last_name = "Hudgens")

causes the following to happen inside the function:

kwargs = {
    'first_name': 'Kristine',
    'last_name': 'Hudgens'
}

The argument can take any name, but as a conventional rule in Python, this type of 
'keyword argument' is usually called 'kwargs'
"""



# COMBINE ALL TYPE OF ARGUMENTS IN FUNCTIONS
def greeting4(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope that you're having a great {time_of_day}")

    if kwargs:
        print("\nYour tasks for the day are:")
        for key, val in kwargs.items():
            print(f"\t- {key} => {val}")


greeting4(
    "Morning",                          # time_of_day -> because it is in the first position
    "Kristine", "Hudgens",              # *args -> take the rest of the arguments
    # these arguments have name, so they are taken in '**kwargs' as a dictionary:
    first = "Empty dishwasher",
    second = "Take pupper outside",
    third = "Math homework"
)

""" this functions prints:
Hi Kristine Hudgens, I hope that you're having a great Morning

Your tasks for the day are:
    - first => Empty dishwasher
    - second => Take pupper outside
    - third => Math homework
"""