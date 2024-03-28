
"""
We have to import:
-operators
-reduce from functools library --> reduce(function, iterable)

"""

import operator
from functools import reduce

"""
operator.add(a, b)
operator.sub(a, b)
operator.null(a, b)
operator.truediv(a, b)
"""

def dynamic_reducer(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)


#  the reduce function takes two arguments. A lamba function that has a total and an element.
"""
we are calling directly to the function througth Lambda, as operators [op] containers operator.add (for instance),
therefore making 'operators[op](total, element)' is the same as making 'operator.add(total, element)'.
"""
print(dynamic_reducer([1, 2, 3], "+"))    # 6
print(dynamic_reducer([1, 2, 3], "-"))    # -4
print(dynamic_reducer([1, 2, 3], "*"))    # 6
print(dynamic_reducer([1, 2, 3], "/"))    # 0.166
