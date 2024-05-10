# GENERATORS
"""
We are going to repeat the objective as in the previous file, 
but using other options provided by Python -> generators

using yield 'keeps' the value of the loop for when the function
is called again, having written 'yield' tells python that the
next function can be used to iterate through the list of names
"""

class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx]      #yielding to the generator
            else:
                idx = 0
                yield self.players[idx]
            idx += 1

# best practices to apply 

    def __repr__(self):
        return f"<InfiniteLineup({self.players})>"

    def __str__(self):
        return f"<InfiniteLineup with the players({self.players})>"
    
astros = [
    "Springer",
    "Bregman",
    "Altuve",
    "Correa",
    "Reddick",
    "Gonzalez",
    "McCann",
    "Davis",
    "Tucker"
]

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(next(astros_lineup))        # Springer
print(next(astros_lineup))        # Bregman
print(next(astros_lineup))        # Altuve

#print(repr(astros_lineup))
#print(repr(astros_lineup))
