# LAMBDAS
#a tools that allos you to wrap up a function.

full_name = lambda first, last: f'{first} {last}'

print(full_name("Aitor", "Atxa"))      # Aitor Atxa


def greeting(name):
  print(f"Hi there {name}")

greeting(full_name("Aitor", "Atxa"))

"""
lambda = tool that allows you to collect a simple function in a variable 
and pass it very easily to other functions.

SINTAXIS:
lambda <arguments>: what_is_returned
"""


