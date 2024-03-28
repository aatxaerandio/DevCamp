# EXERCISE 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list = ["Alejandro", "Gabriel", "Jose", "Juanjo", "Daniel"]

my_tuple = ("apples", "pears", "pranges", "bananas")

my_float = 36.66

my_integer = 89

from decimal import Decimal
my_decimal = Decimal(123.45)

my_dictionary = {
  "name": "Sofia",
  "surname": "Garcia",
  "age": "28",
  "country": "España"
}



# EXERCISE 2: Round your float up.

my_float = 36.66

import math

print(math.ceil(my_float))    # 37




# EXERCISE 3: Get the square root of your float.

my_float = 36.66

import math

print(math.sqrt(my_float))    # 6.0547502012882415




# EXERCISE 4: Select the first element from your dictionary.

my_dictionary = {
  "name": "Sofia",
  "surname": "Garcia",
  "age": "28",
  "country": "España"
}

"""
In this exercise we assume that "the first element" makes 
reference to the ITEM. In any case, I performed for ITEMS, 
KEY and VALUE.
"""

# Obtain the first element (ITEM) from the dictionary
first_item = my_dictionary.items() 
print(list(first_item)[0])         # ('name', 'Sofia')

# Obtain the first element (KEY) from the dictionary
first_key = my_dictionary.keys()
print(list(first_key)[0])   # name

# Obtain the first element (VALUES) from the dictionary
first_value = my_dictionary.values()
print(list(first_value)[0])     # Sofia




# EXERCISE 5: Select the second element from your tuple.

my_tuple = ("apples", "pears", "pranges", "bananas")
print(my_tuple[1])         # pears




# EXERCISE 6: Add an element to the end of your list.

my_list = ["Alejandro", "Gabriel", "Jose", "Juanjo", "Daniel"]

my_list.append("Mariano")
print(my_list)   # ['Alejandro', 'Gabriel', 'Jose', 'Juanjo', 'Daniel', 'Mariano']




# EXERCISE 7: Replace the first element in your list.

my_list = ['Alejandro', 'Gabriel', 'Jose', 'Juanjo', 'Daniel', 'Mariano']

my_list[0] = "Miguel"
print(my_list)  # ['Miguel', 'Gabriel', 'Jose', 'Juanjo', 'Daniel', 'Mariano']




# EXERCISE 8: Sort your list alphabetically.

my_list = ['Miguel', 'Gabriel', 'Jose', 'Juanjo', 'Daniel', 'Mariano']

my_list.sort()
print(my_list)  # ['Daniel', 'Gabriel', 'Jose', 'Juanjo', 'Mariano', 'Miguel']




# EXERCISE 9: Use reassignment to add an element to your tuple.

my_tuple = ("apples", "pears", "pranges", "bananas")

my_tuple += ("pineapple",)
print(my_tuple)     # ('apples', 'pears', 'pranges', 'bananas', 'pineapple')