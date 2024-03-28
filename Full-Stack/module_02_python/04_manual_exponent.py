# USING ITERACTION


def manual_exponent(num, exp):
    counter = exp - 1           #by default is -1; because total is set to num. 
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))
print(manual_exponent(3, 3))
print(manual_exponent(10, 5))

"""
2 ^ 3 
2 x 2 x 2  
"""




# USING REDUCE FUNCTION

from functools import reduce

def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2, 3))    # 8
print(manual_exponent(10, 2))   # 10
"""
reduce takes a fnction as an arguiment and then takes a list. 
Every time you call on every element in our computed list, take the total  and multiple by the element.
"""

#####

#Lambda function works
#it is a function withou name.
def some_func(total, element):
        return total * element

[2, 2, 2]
some_func(2, 1)
some_func(4, 2)
8