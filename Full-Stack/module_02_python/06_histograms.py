# Histogram --> type of chart for statistics, see patterns and basic types of trends with data.

# The objective is to print the histopgram using the learnt in dictionaries.

"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales = {
  'google': 20,
  'facebook': 42,
  'twitter': 10,
  'offline': 12,
}

print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')


#Another more advanced option would be:

for (name, qty) in sales.items():
    print(f"{name[0]} {'$' * qty}")