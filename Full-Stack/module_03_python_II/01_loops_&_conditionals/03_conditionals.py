# CONDICIONALES

age = 15

if age < 25:
    print(f"I'm sorry, you need to be at least 25 years old.")
elif age > 100:
    print(f"I'm sorry, {age} is too old to rent a car.")
else:
    print(f"You're good to go, {age} fits in the range to rent a car.")




# TERNARY OPERATOR
""" SINTAXIS
<variable to store the result (optional)> = <result if True> if <condition> else <result if False>
"""
role = "guest"
auth = "can access" if role == "admin" else "cannot access"
print(auth)             # cannot access

# repeat but changing the value of "role"
role = "admin"
auth = "can access" if role == "admin" else "cannot access"
print(auth)             # can access

# another example
language = "python"
language_check = True if language == "python" else False
print(language_check)



# COMPARATIVE OPERATORS
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# <  Less than
# <= Less than or equal to

username = "jonsnow"

if username != "jonsnow":
    print("Welcome")
else:
    print("You should not pass!")



# WITH LISTS
user_list = ["Kristine", "Tiffany"]
second_list = ["Jordan", "Brayden"]

if user_list == second_list:
    print("They match")         # only will print when lists are equal




# Check if a Value is Included in a Python String or List

sentence = "The quick brown fox jumped over the lazy dog"
#word = "quick"                 # it is in the if
word = "Dog"                    # does not entry in the of if -> case-sensitive
# if we want to read the `dog`, we can put `.lower()` in the if

if word in sentence:
    print("The word was found in the sentence")
else:
    print("The word was not in the sentence")


# the same with lists
nums = [1, 2, 3, 4]

if 3 in nums:
    print("The number was found")       # 3 is on the list, so enters here
else:
    print("The number was not found")





# COMPOUND CONDITIONALS -> MULTIPLE CONDITIONALS
username = "jonsonow"
email = "jon@snow.com"
password = "asdfasdf"

if (username == "jonsnow" or email == "jon@snow.com") and password == "thenorth":
    print("Access permitted")
else:
    print("You shall not pass!")


# another example
logged_in = True
standard_user = True

if logged_in and not standard_user:     # to enter the 'if' logged_in must be True and standard_user needs to be False
    print("You can access the admin dashboard")
else:
    print("You can only access the standard dashboard")