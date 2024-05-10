# NESTED FUNCTIONS -> a function inside another function

def greeting(first, last):
    # the 'child' function can access the variables of the 'parent' function
    def full_name():
        return f"{first} {last}"
    
    print(f"Hi {full_name()}!")


greeting("Aitor", "Atxa")      # Hi Aitor Atxa!

""" WHEN TO USE NESTED FUNCTIONS?
If you create a program with a function that will have to be called 
at some other time throughout the program, it is best not to use 
nested functions

If you are only going to use that function to be called from a single
function, then it should be a nested function (as in the example)
"""