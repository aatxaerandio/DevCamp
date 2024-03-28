#DATA TYPES

# 01 BOOLEANS --> if TRUE or FALSE

meal_completed = True



# 02 NUMBERS 
 
# integers, floats or complex numbers

sub_total = 100
tip = sub_total * 0.2
print (tip)
total = sub_total +  tip

receipt = "Your total is" +  total #this will make an error, we cannot combine a number with a variable.

#to convert one data type to other, we use str.
receipt = "Your total is " + str(total)




#Integer --> numero entero 
product_id = 123

#Float --> It is NOT a decimal
sale_price = 14.99

#Complex numbers
tip_percentaje = 1/5
print(tip_percentage)               # 0.2

#Integer and Float numbers can work together
print(product_id + sale_price)      #137.99



# addition --> +
addition_value = 100 + 42
print(addition_value)               # 142
# subtraction -> -
subtraction_value = 100 - 42.3
print(subtraction_value)            # 57.7
# division -> /
print(100 / 42.3)                   # 2.364066193853428
# floor division -> //
print(100 // 42)                    # 2 -> rounds the value to smallest.
# multiplication -> *
print(100 * 38)                     # 3800
# modulus -> %
print(10 % 2)                       # 0 -> even numbers always return a 0 when calculating %2
print(11 % 2)                       # 1 -> odd numbers always return a 1 when calculating %2
print(10 % 3)                       # 1
# exponents -> **
print(11 ** 2)                      # 121


# ORDER OF OPERATIONS
calculation = 8 + 2 * 5 - (9  + 2) ** 2
print(calculation)       # -103

"""
Please -> Parans ()
Excuse -> Exponents **
My -> Multiplication *
Dear -> Division /
Aunt -> Addition +
Sally -> Subtraction -

8 + 2 * 5 - (9 + 2) ** 2
8 + 2 * 5 - 11 ** 2
8 + 2 * 5 - 121
8 + 10 - 121
-103
"""

# ASSIGNMENT OPERATOR

total = 100
total = total + 10
print(total)  #110

total += 10
print(total)  # 110

total -= 10
print(total)  # 90

total *= 2
print(total)  # 200

total /= 10
print(total)  # 10

total //= 10
print(total)  # 10

total **= 2
print(total)  #100 * 100 = 10000

total %= 2
print(total)  # 0  (el resto de la división)

product_two = 120
print(total)

product_three = 10
print(total)

total += product_two
total += product_three
print(total)  # 230


# DECIMALS vs FLOAT
product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty)  # 42962.4

#Now with decimals, importing the Decimal library from decimal
from decimal import Decimal

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty)  # 42962.40000000000282883716451

# decimals outputs much more accurary.
#This is MANDATORY when is realted to FINANCE aplications


# CONVERTION BETWEEN NUMERIC DATA TYPES.
product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost))    # 88 -> ignores whatever is not the integer number part
print(float(qty))    # 450.0

from decimal import Decimal

print(Decimal(product_cost))     # 88.799999999997157
print(complex(commission_rate))  # (0.08 + 0j)



# FUNCTIONS FOR NUMBER DATA TYPES
import math

loss = -20.25
product_cost = 89.99

print(abs(loss))  # 20.25  --> absolute value of loss, the pure value and remove the negative value.
print(math.floor(product_cost))  # 89 --> Pick the floor value of product_cost. I want the rounded value to down od that value. "Redondear hacia abajo.""
print(math.ceil(product_cost))     # 90 --> Pick the ceil value of product_cost. I want the rounded value to up of that value. "Redondear hacia arriba.""
print(abs(math.floor(loss)))  # --> 21
print(round(product_cost))  # round to the near (up or down) whole number. #90
print(math.sqrt(product_cost))  # Square root of product_cost. #9.486305919582677
print(math.pow(5, 2))  # 5 to the power of 2. #25.0
print(5**2)  # 5 to the power of 2. #25














# 03 STRINGS

#can be created with '' or double "" --> both give us the same output

sentence = "the quick brown fox jumped over the lazy dog"

sentence_two = 'That is my dog's bowl''  #This will NOT WORK
sentence_two = 'That is my dog\'s bowl'  #This will WORK
sentence_three = "That is my dog's bowl"  #This will WORK
sentence_four = "Tiffany said, \"That is my dog's bowl\""  #This will WORK

# A CASE-FUNCTIONS

sentence = 'The quick brown fox jumped'

sentence = 'The quick brown fox jumped' .upper()

print(sentence)
print(sentence.upper())          #
print(sentence.capitalize())     # first letter of the string in uppercase
print(sentence.title())          # first letter of every word from the string in uppercase
print(sentence.lower())          #

# B ACCESS TO PART OF THE STRING
#Each letter has an index

#The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# '' => 3
starter_sentence = 'The quick brown fox jumped'
print(starter_sentence[12])  #Will print letter o.
print(starter_sentence[0])   #Will print letter T 

#Ranges are a way to access more than 1 value.

print(starter_sentence[0:2])   #Will stop just before the range. Print "Th"

new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)    #Thy quick brown fox jumped.

##-----
#We can used negative index; that start fromt he end of the senten

print(starter_sentence[-3])   # 3



# C HEREDOC = multiline strin

content = """
Nullam id dolor id nibh ultricies vehivula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis partutient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()        # .strip() deletes the whitespaces at the end and beginning of the string

print(content)



# performs some tasks and then it returns a different type of process.
# the same as before, but not using .strip(), so it adds \n at the beginning and at the end.
# how to write the same in a single line:

content = "\nNullam id dolor id nibh ultricies vehivula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis partutient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n"
# gives us ore of the computed based representation, greste to see new line characters, etc.

print(repr(content)) 



# D STRING INTERPOLATIONS
"""
Process python code inside strings.
REMEMBER to PUT F letter!!!
This kind of strings cannot avoid special characters with "\", so may use diferent ways:
"""

name = 'Kristine'
greeting = f'Hi {name}'
print(greeting)    #Hi Kristine

# this kind of strings can't scape special chars with "\", this is the way it should be done:
sentence = f"this is my {{bracket}} blog post"
# it prints: this is my {bracket} blog post
#
# this would return an error: f"this is my \{bracket\} blog post"

# it is a great way to create a dynami email!
name = 'Kristine'
product = 'Python elearning course'

email_content = f"""

Hi {name}
Thak you for purchasing {product}

Regards, 
Sales Team
"""
print(email_content)

# Implement Index Based String Interpolations // Prerferred string literal with the f letter as above.
name = 'Kristine'
age = 12
product = 'Python elearning course'

greeting = "Hi {0}, you are listed as {1} years old and you have purchased: {2}...".format(name, age, product)

print(greeting)

"""
.format(a, b, c) 
go into the string and it is going to map to each one of these values.
So name is going to be mapped to the very first element which is 0.
Age is going to be mapped to the second element which has the index 1
and then product is going to be mapped right here. 
"""



#FIND A SUBSTRING IN PYTHON: 3 MODES.
sentence = "The quick brown fox jumped over the lazy dog"

print(sentence.find("quick"))   #4 --> index where 'quick' starts.
print(sentence.find("oops"))    #-1 --> it does not exist in the sentence.

#2st option --> .index()
print(sentence.index("quick"))  #4 
print(sentence.index("opps"))   #error --> throws an ERROR.

#3st option --> 'in' orperator
print("quick" in sentence)  #True
print("oops" in sentence)   #False



# REPLACE FUNCTION --> Find and Replace String Values

sentence = 'The quick brown fox jumped over the lazy dog'

sentence = sentence.replace('quick', 'slow')

print(sentence)          # The slow brown fox jumped over the lazy dog



#STRIP STRINGS

url = 'https://google.com'

print(url.strip('https://'))

print(url.strip())   #removes whitespaces
url = url.lstrip('https://')   #remove 'https://' from the left' 
url = url.rstrip('.com')      #remove '.com' from the right
url = url.capitalize()        #capitalize

print(url)


# PARTITION -> returns a tuple with 3 elements

heading = "Python: An Introduction, and Python: Advanced"

header, _, subheader = heading.partition(': ')

#It will partition and have header, the partition element and the subheaders.
print(header)                   # Python
print(_)                        # ': ' -> data we don't want (we save it into variable called "_")
print(subheader)                # An Introduction


#You can chenage the names, it does not matter.
first, second, third = heading.partition(': ')
print(first)
print(second)
print(third)

# -> if there is another match, the seoncd value will only be the first partition match
heading = "Python: An Introduction, and Python: Advanced"
header, _, subheader = heading.partition(": ")
print(header)                   # Python
print(_)                        # ': '
print(subheader)                # An Introduction, and Python: advanced



# SPLIT in different portions

#Partiton return a TUPLE vs Split returns a LIST

tags = 'python,coding,programming,development'

list_of_tags = tags.split(',')   # ["python", "coding", "programming", "development"] --> Each has an element. 
list_of_tags = tags.split()      # ["python","coding","programming","development"] It is a singles string object

print(list_of_tags)



#CHECK IF YOU HAVE NUMBERS

api_data = '5'
greeting = 'Hi'

# check if is alphanumeric    #The whitespace IS NOT ALPHANUMERIC --> so will give NO.
print(api_data.isalpha())        # False
print(greeting.isalpha())        # True
print("Hi there". isalpha())     # False

# check if is numeric         #It is better to see if it numeric or not
print(api_data.isnumeric())     # True
print(greeting.isnumeric())     # False













# 04 Bytes and byte arrays



# 05 None









#From here onwards, collections

# COLLECTIONS

# 06 Lists --> always between []

"""
It is a list of elements.
They are great to store multiple data types with an order
"""

users = ['Kristine', 'Tiffany', 'Jordan']


print(users)        # ['Kristine', 'Tiffany', 'Jordan']

# INSERT NEW ELEMENTS // Need to put the index where you want to put and then the name
users.insert(0, 'Anthony')
print(users)        # ['Anthony', 'Kristine', 'Tiffany', 'Jordan']   #You may use INSERT

users.append("Thom")
print(users)        # ['Anthony', 'Kristine', 'Tiffany', 'Jordan', 'Thom']  #You may use APPEND

# ACCESS ELEMENTS
print(users[2])        # Jordan
print([users[2]])      # ['Jordan']


# EDIT VALUES
users[4] = 'Brayden'
print(users)    # ['Anthony', 'Kristine', 'Tiffany', 'Jordan', 'Brayden']

# REMOVE ELEMENTS FROM THE LIST
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']
# .remove() --> when you KNOW the value to remove
users.remove('Jordan')
print(users)        # ['Kristine', 'Tiffany', 'Leann']
# .pop() --> when you want to remove the very last element. Return the last element and store in the variable.
popped_user = users.pop()
print(popped_user)      # Leann
print(users)        #['Kristine', 'Tiffany']
# del -> when you know the index of the element
del users[0] 
print(users)        # ['Tiffany']

#MIXED LISTS
users = ["Kristine", "Tiffany", "Jordan", "Leann"]
ids = [1, 2, 3, 4]
mixed_list = [42, 10.3, "Altuve", users]        # nested list -> list inside list
print(mixed_list)                               # [42, 10.3, 'Altuve', ['Kristine', 'Tiffany', 'Jordan', 'Leann']]
user_list = mixed_list.pop()
print(user_list)                                # ['Kristine', 'Tiffany', 'Jordan', 'Leann']
print(mixed_list)                               # [42, 10.3, 'Altuve']

#NESTED LISTS
nested_lits = [[123], [234], [345]]

#LENGHT OF A LIST
tags = ["python", "development", "tutorials", "code"]
print(len(tags))                            # 4


#INDEX OF AN ELEMENT
tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)                      print(number_of_tags)       # 4
last_item = tags[-1]                            print(last_item)            # code
index_of_last_item = tags.index(last_item)      print(index_of_last_item)   # 3


# SORT LISTS
tags = ['python', 'development', 'tutorials', 'code']
print(tags)             # ['python', 'development', 'tutorials', 'code']

tags.sort()  #Alphabetically ordered  
print(tags)             # ['code', 'development', 'python', 'tutorials']

tags.sort(reverse=True)     #with dates by deafult the older; put like that to reverse.
print(tags)             # ['tutorials', 'python', 'development', 'code']

totals = [234, 1, 543, 2345]
print(totals)           # [234, 1, 543, 2345]

totals.sort()
print(totals)           # [1, 234, 543, 2345]

totals.sort(reverse=True)
print(totals)           # [2345, 543, 234, 1]


# SORT WITHOUT CHANGING ORIGINAL LIST -> sorted()

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]


print(sale_prices)     # [100, 83, 220, 40, 100, 400, 10, 1, 3]

sale_prices.sort()
print(sale_prices)     # [1, 3, 10, 40, 83, 100, 100, 220, 400]

sorted_list = sale_prices.sort()
print(sorted_list)   # None

"""
sort() doesn't return anything and modifies the original list, but sometimes
we don't want that
"""

sorted_list = sorted(sale_prices)
print(sorted_list)     #[1, 3, 10, 40, 83, 100, 100, 220, 400]

sorted_list = sorted(sale_prices, reverse=True)
print(sorted_list)    # [400, 220, 100, 100, 83, 40, 10, 3, 1]









# JOIN
uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)   # I want to join all the element and the delimiter for each element is "+"
query_uri = f'{uri}{formatted_tags}'

print(formatted_tags)     # python+development+tutorial
print(query_uri)          # https://www.google.com/search?q=python+development+tutorial


# RANGES    -   Acess more than one element
tags = ['pyton', 'development', 'tutorials', 'code']

tag_range = tags[1:2]   #remember the second index is not included.
print(tag_range)        #['development']

tag_range = tags[1:]   #from index to the end 
print(tag_range)       # ['development', 'tutorials', 'code']

tag_range = tags[:2]  # from the beginning to index 2
print(tag_range)       # ['pyton', 'development']

tag_range = tags[:-1]   #all except the last one.
print(tag_range)        # ['pyton', 'development', 'tutorials']

tag_range = tags[:]   #all items in the list
print(tag_range)       # ['pyton', 'development', 'tutorials', 'code']


# ADVANCED RANGES AND SLICES

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]


tag_range = tags[1:-1]
print(tag_range)  # ['development', 'tutorials', 'code', 'programming']

tag_range = tags[:-1:2]   # the third element is the interval.
print(tag_range)    # ['python', 'tutorials', 'programming']

tag_range = tags[::-1] #Flip the entire order of the list
print(tag_range)   # ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

#It could be similar to sort, but we have to take into account that SORT applies the criteria of alphabeticall order!!

tags.sort(reverse=True)
print(tags) # ['tutorials', 'python', 'programming', 'development', 'computer science', 'code']




# FIND THE STATISTICAL MEDIAN
"""
1. sort the list
2. split the list in two to grab righ and left 
3. 
4. 
tools:
- math library
- sorted function
- list slicing
- computations
"""
sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

import math

sorted_list = sorted(sale_prices)
print(sorted_list)  # [1, 3, 10, 40, 83, 100, 100, 220, 400]

num_of_sales = len(sorted_list)
print(num_of_sales)     # 9

first_sale_items = sorted_list[:math.floor(num_of_sales/2)]  #Take from the beggining of the list to the middle of the list. 
print(first_sale_items)     # [1, 3, 10, 40]

last_sale_items = sorted_list[-(math.floor(num_of_sales/2)):] # Takes from the end to tje middle
print(last_sale_items)     # [100, 100, 220, 400]

median = sorted_list[math.floor(num_of_sales/2):(math.floor(num_of_sales/2)) + 1]
print(median)  # [83]

# CLEAN
half_slice = math.floor(num_of_sales/2)     #Modify with half_slice and do the same, in order to not duplicate code.



# SLICE CLASS

tags = [
    "python",
    "development",
    "tutorials",
    "code",
    "programming"
]

print(tags[:2])    # ['python', 'development']
    #But sometime we do not want the slice range.

slice_obj = slice(2)    # We can use the slice object to create a new list
print(slice_obj)     # slice(None, 2, None)  # start point (None), end point (2) and the interval (None). 

print(tags[slice_obj])    # ['python', 'development']

# example 01
slice_obj = slice(1, 4, 2)   # Basically start in the 1 (development), to the 4 (programming), in intervals of 2. That means that will take 1 (develpoment) and 3 (code).
print(tags[1:4:2])          # ['development', 'code']
print(tags[slice_obj])      # ['development', 'code']

# we can know where the slice object starts, stops or its step
print(slice_obj.start)  # 1
print(slice_obj.stop)   # 4
print(slice_obj.step)   # 2
# this is great to don't repeat code when slicing in different lists using the same pattern


# ADD TO A LIST WITH PLACE AND COPY PROCESSES

tags = ["python", "development", "tutorials", "code"]

# wrong way to add an element
tags[-1] = 'Programming'      # replaces code, not adding elements
print(tags)
tags.extend("programming")  
print(tags)                 # ['python', 'development', 'tutorials', 'programming', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

# correct way  --> PUT BETWEEN BRACKETS!!
tags = ["python", "development", "tutorials", "code"]
tags.extend(["programming"])
print(tags)                     # ['python', 'development', 'tutorials', 'code', 'programming']

# without modifying the original list
tags = ["python", "development", "tutorials", "code"]
new_tags = tags + ["programming"]
print(new_tags)                 # ['python', 'development', 'tutorials', 'code', 'programming']










# 07 Tuples  --> ()


"""
List []
Dictionary: {}
Tuple: ()

"""

#Tuple VS List. 
#List --> mutable
#Tuple --> immutable (much more control).

post = ("Python Basics", "Intro guide to Python", "Some cool python content")

title, sub_heading, content = post  #will treat treat each one of these items as a query engine

tittle = post[0]
sub_heading = post[1]
content = post[2]

print(title)    #Python Basics
print(sub_heading)    #Intro guide to Python
print(content)        #Some cool python content

#When to use Tuples and when lists?

post = ["Python Basics", "Intro guide to Python", "Some cool python content"]

post.sort()

title, sub_heading, content = post  #will treat treat each one of these items as a query engine


print(title)     #Intro guide to Python
print(sub_heading)   #Python Basics
print(content)        #Some cool python content
#Data is not correct!!
#With lists --> If the order of the element change, then the unpacking may give unexpected behaviour

# but if we .sort() a tuple, that would be an error, because tuples are immutable



# ADD ELEMENTS TO TUPLES

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')
#post = post + ('published')  # this is gonna be treated as a mathematical operation
#to solve this issue, we have to add a COMMA at the end of the tuple.

post += ('published', )  # The same as post = post + ( 'published',)

print(post)  # ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')

title, sub_heading, content, status = post

print(title)  #Python Basics
print(sub_heading)  # Intro guide to python
print(content)  # Some cool python content
print(status)  #published

# ID FUNCTION
#gives a reference and a unique ID for each element
post = ("Python Basics", "Intro guide to python", "Some cool python content")
print(id(post))     # 2037450353792 -> give us the id of the object

post+= ('published',)
print(id(post))      # 2037450600144 -> we can see that now, post object has changed, it's not the same as before



# LISTS NESTED IN TUPLES

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')
tags = ['python', 'coding', 'tutorial']
post += (tags,)

print(post)   #('Python Basics', 'Intro guide to Python', 'Some cool python content', ['python', 'coding', 'tutorial'])
print(post[1])    # Intro guide to Python
print(post[-1][1]) # coding


# SLICES

post = ("Python Basics", "Intro guide to python", "Some cool python content", "published")
print(post[:2])             # ('Python Basics', 'Intro guide to python')
print(post[1:])             # ('Intro guide to python', 'Some cool python content', 'published')
print(post[1::2])           # ('Intro guide to python', 'published')


# REMOVE ELEMENTS FROM TUPLES -> tuples are immutable -> need to slice

post = ("Python Basics", "Intro guide to python", "Some cool python content", "published")

# remove from end
post = post[:-1]
print(post)    # ('Python Basics', 'Intro guide to python', 'Some cool python content')

# remove from beggining
post = post[1:]
print(post)    #('Intro guide to python', 'Some cool python content', 'published')

# remove specific element (messy/not recommended)

post = list(post)  #you change in list, but later not into a tuple, so that can lead to erros.
post.remove("published")
post = tuple(post)    #Asign back to become a Tuple again.
print(post)


# 08 Sets

# similar to lists, but their elements don't follow any order, and values can't be repeated




# 09 Dictionaries  --> {}


# the key-value data is stored here
players = {
    "ss": "Correa"  
}
print(players)   # {'ss': 'Correa'}
#Another example
players = {
    "ss": "Correa",
    "2b": "Altuve",
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer"
}
# now, instead of working with indexes, we'll work with key-value structures
second_base = players["2b"]
print(second_base)     #Altuve
other_base = players["asdf"]
print(other_base)      # error
designated_hitter = players["DH"]
print(designated_hitter)                # Gattis


# NESTED COLLECTIONS
# lists as dictionary values

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

print(teams["astros"])              # ['Altuve', 'Correa', 'Bregman']
print(teams["astros"][1])               # Correa
print(teams["astros"][:2])              # ['Altuve', 'Correa']

#You can save the vbalues (lists) in variables
astros = teams['astros']     
print(astros)


# ADD NEW KEY-VALUE PAIRS

teams["red sox"] = ["Price", "Betts"]   # keys are strings, can have whitespaces, but not recommended
print(teams)

""" print(teams) -->
{
    'astros': ['Altuve', 'Correa', 'Bregman'],
    'angels': ['Trout', 'Pujols'],
    'yankees': ['Judge', 'Stanton'],
    'red sox': ['Price', 'Betts']
}
"""



# GET    --> Configure Fallback Lookup Values

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('yankees', 'No featured team')
print(featured_team)     #['Judge', 'Stanton']

featured_team_new = teams.get('player_not_appearting', 'No featured team')
print(featured_team_new)      # No featured team

# Fallback is a message when the key you want is not available.
# If you want to use a fallback, you must add a default value to the dictionary.
#If 'yankees' is not there, iw will print 'No featured team'



# DICTIONARY VIEW OBJECT
players = {
    "ss": "Correa",
    "2b": "Altuve",
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer"
}
teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"]
}
# GRAB ONLY THE KEYS, VALUES OR BOTH
print(players.keys())                   # dict_keys(['ss', '2b', '3b', 'DH', 'OF']) -> it is an object, not a list
print(players.values())                 # dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])
print(players.items())                  # dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])
# view objects are not lists, we can not use them as lists, but we can convert the view objects into lists
print(list(players.values()))           # ['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer']
print(list(players.values())[1])           # Altuve

"""
The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
They provide a dynamic view on the dictionary’s entries, 
which means that when the dictionary changes, the view reflects these changes.
"""

# THREAT SAVE -> COPY THE LIST
player_names = list(players.copy().values())
print(player_names)


# NESTED ITEMS

team_grouping = teams.items()
print(team_grouping)      #prints all the teams and players
print(len(team_grouping))     # 4
print(list(team_grouping))   
"""
[
('astros', ['Altuve', 'Correa', 'Bregman']),
('angels', ['Trout', 'Pujols']), 
('yankees', ['Judge', 'Stanton']), 
('red sox', ['Price', 'Betts'])]
"""
# they are tupples -> can use them almost like lists

print(list(team_grouping)[1])     # ('angels', ['Trout', 'Pujols'])
print(list(team_grouping)[1][1])  # ['Trout', 'Pujols']
print(list(team_grouping)[1][1][0])  # Trout



# REMOVE ELEMENTS FROM DICTIONARIES

teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"]
}

# 'del' keyword -> useful when we know that the key exists
#del name_dictionary ['Key']
del teams['astros']

#if the key does not exist, will print and error
del teams['mets']
print(teams)     #Error

# .pop() -> like .get(), we give to it a second argument, if the first doesn't exist, returns the message

print(teams.get('mets', 'No team found in that name'))
print(teams)    #No team found in that name

removed_team = teams.pop('tems', 'No team found in that name'')
print(removed_team)    # No team found by that name.

removed_team = teams.pop('yankees', 'No team found in that name')
print(removed_team)    # ['Judge', 'Stanton'] -> the value of the removed item




# LISTS OF NESTED DICTIONARIES

#A list that contains multiple dictionaries and each one containes a single skey value pair there the key is the name and contains elements.

teams = [
  {
    'astros':{
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
    
  },
  {
    'angels':{
    'OF': 'Trout',
    'DH': 'Pujols',
  }
  },  
]

print(teams)
"""
[{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}, {'angels': {'OF': 'Trout', 'DH': 'Pujols'}}]
"""

print(teams[0])
"""
{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}
"""


angels = teams[1].get('angels', 'Team not found')
print(angels)                       # {'OF': 'Trout', 'DH': 'Pujols'}

print(angels.values())     # dict_values(['Trout', 'Pujols'])  // Put List!

print(list(angels.values()))        # ['Trout', 'Pujols']

print(list(angels.values())[1])     # Pujols





lista_ordenada = sorted(lista_clase)
print(lista_ordenada) # ['Alejandro', 'Juanjo', 'Miguel']

print(lista_clase) # ['Miguel', 'Juanjo', 'Alejandro']


