
import fnmatch     # no need to install
import os

def list_files():
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files: ", file)

        if fnmatch.fnmatch(file, "*.rb"):
            print("Ruby files: ", file)

        if fnmatch.fnmatch(file, "*.yml"):
            print("Yaml files: ", file)

        if fnmatch.fnmatch(file, "*.py"):
            print("Python files: ", file)

#list_files()

from fnmatch import fnmatchcase     # filter down so if we find something we want and only grab these elements.

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

# only search for the players that finish with "2B"
second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print("Players that play in the second base: ", second_base_players)

#Players that play in the second base:  ['Jose Altuve 2B', 'Scooter Gennett 2B']






