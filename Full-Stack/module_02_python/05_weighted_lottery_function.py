"""
In a given dictionary, we pretend the function
 to answer the name of the probability

For instance, if the function is:
    weights = {
            'winning': 1,
            'losing': 1000
        }

for each 1001 times, 1000 will print 'losing' and 1 'winning'


For instance, if the function is:

    other_weights = {
            'winning': 1,
            'break_even': 2,
            'losing': 3
        }

the probability to print 'losing' will be 3 times higher than 'winning', and 2 times 'break_even'

"""


import numpy as np


def weighted_lottery(weights):
  container_list = []
  
  for (name, weight) in weights.items():    # wrap the iteration values in a list.
    #loop 1 times / loop 1000 times
    for _ in range(weight):           # Nested loop: _ is not going to be used, it is just a counter. 
      container_list.append(name)

  return np.random.choice(container_list)  #choiche a random sample



other_weights = {
        'winning': 1,
        'break_even': 2,
        'losing': 3
    }

print(weighted_lottery(other_weights))
