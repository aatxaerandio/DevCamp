#Ejercicio 1 - Cree un bucle For de Python.

my_numbers = [1, 2, 3, 4, 5, 6]

for num in my_numbers:
  print(num)


#Ejercicio 2 - Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(arg_1, arg_2, arg_3):
  return arg_1 + arg_2 + arg_3

print(suma(1,1,1))    # 3


#Ejercicio 3 - Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda arg_1, arg_2, arg_3: arg_1 + arg_2 + arg_3

print(suma(1, 1, 1))


#Ejercicio 4 - Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
  print("Este nombre esta en la lista")
else:
  print("Este nombre NO esta en la lista")