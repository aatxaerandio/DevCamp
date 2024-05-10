# BUCLES FOR - WHILE

# FOR LOOP

# BUCLES on LISTS
players = ["Altuve", "Bregman", "Correa", "Gattis"]

for player in players:
  print(player)

"""
Altuve
Bregman
Correa
Gattis

player --> iterable variable. It does not matter the name.

the first player will be "Altuve·, in the second loop "Bregman", in the third loop "Correa" and in the last loop "Gattis". It finishes and gives all the results.

"""



# BUCLES on TUPLES
players = ("Altuve", "Bregman", "Correa", "Gattis")

for player in players:
  print(player)

#works the same way as the list, but the difference is that it is a tuple.



# BUCLES on DICTIONARIES
players = {
    "2b": "Altuve",
    "3b": "Bregman",
    "ss": "Correa",
    "dh": "Gattis"
}


# run key and value
for position, player in players.items():
  print('Position', position)
  print('Player Name', player)

"""
in the loop first takes the first print and then the second print. After that, first and second, again, first and second until it finishes.

Position 2b
Player Name Altuve
Position 3b
Player Name Bregman
Position ss
Player Name Correa
Position dh
Player Name Gattis
"""

#run only keys
for position in players:
  print("Position:", position)
  print("Player name:", players[position])

"""
Position: 2b
Player name: Altuve
Position: 3b
Player name: Bregman
Position: ss
Player name: Correa
Position: dh
Player name: Gattis
"""

#run on values
for player in players.values():
    print(player)
"""
Altuve
Bregman
Correa
Gattis
"""

#EXERCISE
#Create a list named my_list with 5 elements. Then loop over the list to print out each element.
def loop_over_list():
  my_list = ["red", "orange", "blue", "green", "purple"]
  for colour in my_list:
    print(colour)  
  return my_list


# BUCLES on STRINGS
alphabet = "abcdefg"
for letter in alphabet:
  print(letter)
"""
a
b
c
d
e
f
g
"""
#EXERCISE
#Create a variable called "name" and assign it your name as a string. Write a for in loop that iterates through the string and prints each character.
def loop_over_string():
    name = "Aitor"
    for letter in name:
        print(letter)
    return name



#BUCLES on RANGES

for num in range(1, 10):
  print(num)    #prints from 1 to 10.
for num in range(1, 11, 2):
  print(num)   # 1  3  5  7  9 

#EXERCISE
#Using a range, write a loop that prints out all the numbers from one through 10 (10 is included)
for num in range(1,11):
 print(num)



# CONTINUE Y BREAK
usernames = [
    "jon",
    "tyrion",
    "theon",
    "cersei",
    "sansa"
]

#continue  --> keep on goinf to the loop.
for username in usernames:
  if username == "cersei":
    print(f"Sorry, {username}, you are not allowed")
    continue
  else:
    print(f"{username} is allowed")

    """
    jon is allowed
    tyrion is allowed
    theon is allowed
    Sorry, cersei, you are not allowed
    sansa is allowed
    """

# break --> you do not want to go trough all the loop. When finds it, it stops! 
for username in usernames:
  if username == "cersei":
    print(f"{username} was found at index {usernames.index(username)}")
    break
  print(f"{username}")

"""
jon
tyrion
theon
cersei was found at index 3
"""




# WHILE LOOP

#for in  --> clear define when does it start and finish
#while loop --> will not stop when reacehes the end of the list. You have to tell while loop to stop. Because if not, will be an infinite loop.

nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())      #continuosly decrease tje length. So from 99 to 1.


# GUESSING GAME

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == "42":
      print("You correctly guessed it!")
      return False      # this is telling to the 'True' of the loop to stop (become a False)
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()



#MERGE LSIT

legacy_customers = ["Alice", "Bob"]
new_customers = ["Tiffany", "Kristine"]


for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)      # ['Tiffany', 'Kristine', 'Alice', 'Bob']




# LIST COMPREHENSION

num_list = range(1, 11)

# traditional way
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)
print(cubed_nums)      # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


#using list comprehension

cubed_nums = [num ** 3 for num in num_list]
print(cubed_nums)    # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# another example  --> We can also add a conditional statement
num_list = range(1, 11)

# traditional way
even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)
print(even_numbers)       # [2, 4, 6, 8, 10]

# list comprehension
even_numbers = [num for num in num_list if num % 2 == 0]
print(even_numbers)    # [2, 4, 6, 8, 10]
