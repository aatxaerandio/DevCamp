# CHECKPOINT 5



## TAREA 1 - Preguntas teóricas
### Pregunta 1 - ¿Qué es un condicional?
En Python, los condicionales son una serie de instrucciones para que se ejecute un bloque de código u otro dependiendo de una serie de requisitos o condiciones.
En cuanto a la sintaxis, se utilizan:
-	`if` --> Que ejecuta el código si se cumple la condición
-	`elif` --> Cuando hay mas de una condición
-	`else` --> Cuando no se cumple ninguna de las anteriores condiciones
  
```
edad = 12
if edad < 18:
    print("No puedes sacarte el carnet de conducir, eres muy joven aun")
elif edad > 18:
    print("Puedes sacarte el carnet")
else:
    print("No cumples con los criterios establecidos")
```
Este es un ejemplo de condicional con la variable edad.
Al ejecutarse, se recorren todos los condicionales y se imprimirá algo dependiendo del valor que se le de a la variable edad.
En este caso, al establecer `edad = 12`; se cumple el primer condicional, y por tanto se imprime "No puedes sacarte el carnet de conducir, eres muy joven aun".

Ademas, también se pueden combinar, en este caso con `and`:
```
edad = 12
if edad >= 18 and edad <= 65:
    print("Tienes la edad adecuada")
else:
    print("No tienes la edad adecuada")
```
```
import math from numpy
```
En este caso, se usa and para combinar ambas edades y acortar el codigo.
Sigue siendo util, legible y mas compacto.


### Pregunta 2 - 	¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En Python se distinguen dos tipos de bucles, los bucles `for` y los bucles `while`. La gran diferencia entre ellos reside, entre otras, en que el el bucle `for` se sabe cual es el inicio y el final del mismo, mientras que los bucles  `while` pueden dar lugar a bucles infinitos si no se definen bien.

El bucle `for` se utiliza para iterar sobre una lista o cadena, y se usa para realizar una operación en cada elementos de esa lista o cadena.
La sintasis de este bucle esta compuesta por el siguiente código:
```lista = ["elemento_1", "elemento_2"]
for elemento_de_la_lista in lista:
    print("Codigo a ejecutarse")
```
Utilizando un ejemplo:
```
nombres = ["Hector", "Pedro", "Jose", "Miguel"]
for nombre in nombres:
  print(nombre)
```

Por el contrario, el bucle `while` se usa para ejecutar código repetidamente mientras se cumple una condición. 
La sintasix de este bucle esta compuesta por el siguiente codigo:
```
while la_condicion:
    codigo_a_ejecutarse
```
Un ejemplo seria:
```
x = 5
while x < 10:
  x += 1
  print("You´re right")
```
De este modo, si `x` es inferior a 10 (es decir, cumple el condicional)
Se ejecuta el codigo que le sigue, se imprimer `You´re rigth`
Ademas, se le suma 1 a la x; siendo en el siguiente bucle 6 y en el siguiente 7.
El bucle finalizará cuando el valor de x no cumpla la condicion, es decir, al quinto bucle el valor será 10 y por tanto parará.



### Pregunta 3 - ¿Qué es una lista por comprensión en Python?
En este ejemplo, se pretende obtener los numeros que son multiplos de 2.
De forma tradicional se realizaría de este modo; utilizando un bucle `for` y una condición `if` para verificar si el numero es multiplo de 2. Se crea una lista vacia `lista_multiplos`que a medida que el bucle vaya corriendo se vayan añadiendo los multiplos de 2.
```
lista_multiplos = []
multiplos_2 = range(1, 24)

for num in multiplos_2:
  if num % 2 == 0:
    lista_multiplos.append(num)
print(lista_multiplos) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
```
Utilizando lista por comprension se puede simplificar mucho, de este modo:
```
multiplos_2 = range(1, 24)

lista_multiplos = [num for num in multiplos_2 if num % 2 == 0]
print(multiplos_2)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
```
Aqui se pretende obtener los numeros que son multiplos de 2 usando un bucle dentro de una lista. Para cada numero en el rango de 1 a 24, se verifica si es multiplo de 2 y se guarda en la lista `lista_multiplos`. De este modo se consigue el mismo resutlado pero con un codigo mas limpio.
















### Pregunta 4 - ¿Qué es un argumento en Python?
### Pregunta 5 - ¿Qué es una función Lambda en Python?
### Pregunta 6 - ¿Qué es un paquete pip?































## TAREA 2 - Ejercicios prácticos
### Ejercicio 1 - Cree un bucle For de Python.

Se crea una lista de numeros y con el bucle ```for``` se imprime cada numero de la lista.
my_numbers = [1, 2, 3, 4, 5, 6]

for num in my_numbers:
  print(num)




### Ejercicio 2 - Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(arg_1, arg_2, arg_3):
  suma = arg_1 + arg_2 + arg_3
  print(suma)

suma(1,2,3)

def suma(arg_1, arg_2, arg_3):
  return arg_1 + arg_2 + arg_3
print(suma(1,1,1))



### Ejercicio 3 - Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
### Ejercicio 4 - Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
```
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'
Esta es toda la asignación, ¡mucha suerte!
```


