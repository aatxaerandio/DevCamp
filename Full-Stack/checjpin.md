# CHECKPOINT 5

## TAREA 1 - Preguntas teóricas
### Pregunta 1 - ¿Qué es un condicional?
En Python, los condicionales son una serie de instrucciones para que se ejecute un bloque de código u otro dependiendo de una serie de requisitos o condiciones.
En cuanto a la sintaxis, se utilizan:
-	`if` --> Que ejecuta el código si se cumple la condición.
-	`elif` --> Cuando hay mas de una condición.
-	`else` --> Cuando no se cumple ninguna de las anteriores condiciones.
  
```python
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
En este caso, al establecer `edad = 12`; se cumple el primer condicional, y por tanto se imprime ```"No puedes sacarte el carnet de conducir, eres muy joven aun"```.

Ademas, también se pueden combinar, en este caso con `and`:
```python
edad = 12
if edad >= 18 and edad <= 65:
    print("Tienes la edad adecuada")
else:
    print("No tienes la edad adecuada")
```
```python
import math from numpy
```
En este caso, se usa and para combinar ambas edades y acortar el codigo.
Sigue siendo util, legible y mas compacto.


### Pregunta 2 - 	¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En Python se distinguen dos tipos de bucles, los bucles `for` y los bucles `while`. La gran diferencia entre ellos reside, entre otras, en que el el bucle `for` se sabe cual es el inicio y el final del mismo, mientras que los bucles  `while` pueden dar lugar a bucles infinitos si no se definen bien.

El bucle `for` se utiliza para iterar sobre una lista o cadena, y se usa para realizar una operación en cada elementos de esa lista o cadena.
La sintasis de este bucle esta compuesta por el siguiente código:
```python
lista = ["elemento_1", "elemento_2"]
for elemento_de_la_lista in lista:
    print("Codigo a ejecutarse")
```
Utilizando un ejemplo:
```python
nombres = ["Hector", "Pedro", "Jose", "Miguel"]
for nombre in nombres:
  print(nombre)
```

Por el contrario, el bucle `while` se usa para ejecutar código repetidamente mientras se cumple una condición. 
La sintasix de este bucle esta compuesta por el siguiente codigo:
```python
while la_condicion:
    codigo_a_ejecutarse
```
Un ejemplo seria:
```python
x = 5
while x < 10:
  x += 1
  print("You´re right")
```
De este modo, si `x` es inferior a 10 (es decir, cumple el condicional)
Se ejecuta el codigo que le sigue, se imprimer `You´re rigth`.
Ademas, se le suma 1 a la x; siendo en el siguiente bucle 6 y en el siguiente 7.
El bucle finalizará cuando el valor de x no cumpla la condicion, es decir, al quinto bucle el valor será 10 y por tanto parará.



### Pregunta 3 - ¿Qué es una lista por comprensión en Python?
Una lista por comprensión es una lista que permite crear listas de manera concisa y rápida.
La particularidad de estas listas es que permite definir la lista y sus elementos en una sola linea de codigo.

En siguiente ejemplo, se pretende obtener los numeros que son multiplos de 2.
De forma tradicional se realizaría de este modo; utilizando un bucle `for` y una condición `if` para verificar si el numero es multiplo de 2. Se crea una lista vacia `lista_multiplos`que a medida que el bucle vaya corriendo se vayan añadiendo los multiplos de 2.
```python
lista_multiplos = []
multiplos_2 = range(1, 24)

for num in multiplos_2:
  if num % 2 == 0:
    lista_multiplos.append(num)

print(lista_multiplos) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
```
Utilizando lista por comprensión se puede simplificar mucho, de este modo:
```python
multiplos_2 = range(1, 24)

lista_multiplos = [num for num in multiplos_2 if num % 2 == 0]
print(multiplos_2)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
```
Aqui se pretende obtener los numeros que son multiplos de 2 usando un bucle dentro de una lista. Para cada numero en el rango de 1 a 24, se verifica si es multiplo de 2 y se guarda en la lista `lista_multiplos`. De este modo se consigue el mismo resutlado pero con un codigo mas limpio.

### Pregunta 4 - ¿Qué es un argumento en Python?

En Python, un argumento es un elemento que se usa dentro de las funciones,
siendo el objetivo del argumento, proveer de un valor para que la funcion 
ejecute determinado codigo. 

Hay que destacar la diferencia entre ```parametros``` y ```argumentos```, ya que el primero
son las variables que se especifican dentro de los parentesis cuando se define 
una funcion (por ejemplo, ```arg_1``` es parametro), mientras que lo segundo son los 
valores que se pasan a esos parametros cuando llamas a una funncion (en el ejemplo 
de abajo el argumento seria "Miguel").

Hay diferentes tipos de argumentos:

- **Argumentos por defecto:**  Estos son argumentos que tienen un valor predeterminado 
y se usan si no se provee a la funcion de otro argumento. Se asignan con =.
```python
def funcion_defecto(arg_1 = "Pedro"):
  print(arg_1 + " quiere comprarse un coche")

funcion_defecto()     # Pedro quiere comprarse un coche
funcion_defecto("Miguel")     # Miguel quiere comprarse un coche
```

- **Argumentos posicionales:** En los que los cuales los valores son asignados en base a
su posicion cuando la funcion es llamada. 

En el ejemplo de acontinuacion, son 3 valores que se pasan a los argumentos en el 
mismo orden, siendo ```a=2, b=1 y c=3.```
```python
def funcion_pos(a, b, c):
  print((a-b)*c)

funcion_pos(2, 1, 3)    # 3. 
```
- **Argumentos keyword:** son muy similares a los argumentos por defecto, ya que se designan
con un signo igual =. Cierto valor se le asigna a un keyword, en este caso "Juan" a ```nombre```
y 25 a ```edad```.
```python
def estudiante(nombre, edad):
  print("Detalles del estudiante:", nombre, edad)

estudiante(nombre="Juan", edad=25)
```

- **Argumentos arbitrarios:** Se utilizan para pasar un numero varibale de argumentos sin palabras 
clave a la funcion. Usando el asterisco ```*``` hará que ese argumento se comporte como un tupla.
```python
def refrescos(*args):
  for arg in args:
    print(arg)    

refrescos("cola", "pepsi", "fanta", "sprite")
```

- **Argumentos arbitrarios de palabras clave:** Se utilizan al mismo modo que los anteriores, pero 
se usan dos asteriscos en lugar de uno (**). Las funciones que tengan ** en un argumento, harán
que ese argumento se comporte como un diccionario, y al llamar la funcion se le asignan nombres 
a las variables y estas son tratadas como claves del diccionario. 
```python
def pedir(**kwargs):
    if kwargs:
        print(f"Buenas, quiero un kilo de {kwargs['fruta_1']} y medio de {kwargs['fruta_2']}")
    else:
        print("No quiero nada mas, gracias")

pedir(fruta_1 = "peras", fruta_2 = "manzanas")
```

### Pregunta 5 - ¿Qué es una función Lambda en Python?

La funcion lambda en Python es una funcion rápida para realizar operaciones simples  y no es 
necesario definir una funcion completa. Se utilizan para hacer mas sencillo y legible el codigo.
La sintaxis de esta funcion se hace mediante la creación de una variable que contiene dicha funcion:
```python
pregunta = lambda elemento_1, elemento_2: f"¿Has cogido las {elemento_1} y las {elemento_2}?"

print(pregunta("llaves", "gafas"))
```
De este modo imprimirá ¿Has cogido las llaves y las gafas?

### Pregunta 6 - ¿Qué es un paquete pip?

Un paquete pip es una coleccion de modulos y bibliotecas que proporcionan funcionalidades en Python.
Pip es el acronimo de Pip Install Packages, que es el sistema de administracion de paquetes que se usa para 
instalar y administrar los paquetes en Python.

Una vez instalados se pueden importar al codigo para importar dicha funcionalidad de determinado modulo o
biblioteca y usarlo.

## TAREA 2 - Ejercicios prácticos
### Ejercicio 1 - Cree un bucle For de Python.
Se crea una lista de numeros y con el bucle ```for``` se imprime cada numero de la lista.
```python
my_numbers = [1, 2, 3, 4, 5, 6]

for num in my_numbers:
  print(num)
```
### Ejercicio 2 - Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
```python
def suma(arg_1, arg_2, arg_3):
  return arg_1 + arg_2 + arg_3

print(suma(1,1,1))    # 3
```
### Ejercicio 3 - Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
```python
suma = lambda arg_1, arg_2, arg_3: arg_1 + arg_2 + arg_3

print(suma(1, 1, 1))  # 3
```
### Ejercicio 4 - Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
```python
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'
```

Se podria realizar de dos formas:

**1º Caso**
```python
for nombre in lista_nombre:
  if nombre == "Enrique":
    print("Este nombre está en la lista")
else:
    print("Este nombre NO está en la lista")
```
De otro modo, se podria realizar también de esta manera:

**2º Caso**
```python
if nombre in lista_nombre:
  print("Este nombre esta en la lista")
else:
  print("Este nombre NO esta en la lista")
```

