# INDENTATION

def sum(num_one, num_two):
    print(num_one + num_two)

sum(2, 4)

# if we do not use indentation, python will show a IndentationError
# It can be 2/4 whitespaces. DO NOT USE TABS, as in other languages can lead to other behaviours and to bugs


# MATRIX IN PYTHON 

#Be able to produce a matrix that has this output:
[
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8]
]

#May be called:
#    manual_incrementing_matrix(5)

#SOLUTION

def manual_incrementing_matrix(n):
    # matrix n x n


    matrix = [ [None for y in range(n)] for x in range(n)] # crea una matriz llena de None de dimensión n x n
    
    counter = 0

    for idx, element in enumerate(matrix):
        for nested_idx, nested_element in enumerate(element):
            matrix[idx][nested_idx] = counter + nested_idx
        counter += 1
        
    return matrix

print(manual_incrementing_matrix(5))

# VARIABLES

name = 'Kristine'

# use SNAKE CASE to type variable's names
#In order to know if they are classes or variables
post_count = 42 

#better to avoid using names that are not descriptive:
x = 10
y = 12
#better to do:
num_one = 10
num_two = 12

