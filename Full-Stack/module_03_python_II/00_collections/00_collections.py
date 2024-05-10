# TUPLES AS DICTIONARY KEYS

priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(priority_index)   
#Combining the three data structures. Dictionary + Tuple + List

print(list(priority_index.keys()))    # [(1, 'premier'), (1, 'mvp'), (2, 'standard')]

"""
this is usually done because is a great way to add some extra 
information to the dictionary key

For example, following the above example, we can use those tuple keys to
indicate if they are courses of 1 or 2 parts, and using a loop we could select
only those items with 2 parts
"""


# MERGE LISTS IN ONE TUPLE -> zip()

# this is a way of combining data from different lists into one tuple

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
#Take into account the sort of your list.
#Zip allows to merge all.

scoreboard = zip(positions, players)
print(scoreboard)    # <zip object at 0x7030809bb000>
print(list(scoreboard))   # [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]



# SETS (data type)

#Merging of dictionary + list.
# Data MUST NOT be duplicated, data may be UNIQUE.
tags = {
  'python',
  'coding',
  'tutorials',
  'coding',
}

print(tags)    # {'coding', 'python', 'tutorials'}  / No order.

#ACCESS ELEMENTS
print(tags[0])     # error.
query_one = 'python' in tags
query_two = 'ruby' in tags
print(query_one)    # True
print(query_two)    # False 

#First we have to check if the element is in the set and then print it.


#MERGE SETS // See they have unique items

tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}
tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# Merged tags  --> Take all the elements of the sets and merge then in a single set. It removes the duplicated items.
merged_tags = tags_one | tags_two
print(merged_tags)     # {'coding', 'python', 'tutorials', 'ruby', 'development'}

## tags in tags_one but not in tags_two  // Only bring elements that are unique in tags_one.
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)      # {'python'}

# tags in tags_two but not in tags_one
exclusive_to_tag_two =  tags_two - tags_one
print(exclusive_to_tag_two)    # {'ruby', 'development'}

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)   # {'coding', 'tutorials'}

