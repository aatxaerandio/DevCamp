#EXERCISE 1 - Create a string, number, list, and boolean, each stored in their own variable.

var_string = "Buenas tardes"
var_number = 2024
var_list = ["Pablo", 12, "arquitectura", 109.2, True]
var_boolean = False


#EXERCISE 2 - Use an index to grab the first 3 letters in your string, store that in a variable.

var_grab_three = var_string[:3]
print(var_grab_three)


#EXERCISE 3 - Use an index to grab the first element from your list.

print(var_list[0])


#EXERCISE 4 - Create a new number variable that adds 10 to your original number.

var_sum = var_number + 10
print(var_sum)


#EXERCISE 5 - Use an index to get the last element in your list.

print(var_list[-1])


#EXERCISE 6 - Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
list_names = names.split(",")
print(list_names)


#EXERCISE 7 
"""
Get the first word from your string using indexes. 
Use the upper function to transform the letters into uppercase.
Create a new string that takes the uppercase word and the rest of the original string.
"""

first_word = var_string[0:6]
var_string_new = first_word.upper() + var_string[6:]
print(var_string_new)


#EXERCISE 8 - Use string interpolation to print out a sentence that contains your number variable.

var_new = f"Happy new year {var_number}"
print(var_new)


#EXERCISE 9 - Print “hello world”.

print("Hello world")



# EXERCISE 10 
"""
Además necesito que me crees una cadena que contenga la palabra "Hola".
Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. 
Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
"""

my_string = "Hola, este ejercicio es el ultimo del checkpoint 3"
print(my_string.index("Hola"))

my_string_new = my_string.replace("Hola", "adiós")
print(my_string_new)