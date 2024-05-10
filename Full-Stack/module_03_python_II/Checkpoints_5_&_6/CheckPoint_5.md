# CHECKPOINT 5

## TAREA 1 - Preguntas teóricas
### Pregunta 1 - ¿Qué es un condicional?
En Python, los condicionales son una serie de instrucciones para que se ejecute un bloque de código u otro dependiendo de una serie de requisitos o condiciones.

Los condicionales se escriben utilizando la palabra clave `if` seguida de una expresion en paréntesis- Despues de dicha expresión se utilizan  los dos puntos `:` para indicar el inicio de un bloque de código que se ejecutará si la condicion es verdadera. Por otro lado, para indicar el final del bloque de código se usará la indentación. 

Además de ello, los condicionales hacen uso de operadores de comparación, que pueden ser los que se describen a continuación:
| Operadores | Signo | Función |
| ---------- | --------- | ------- |
| Igualdad | == | Se usa para comparar si dos elementos son del mismo tipo y tienen el mismo valor.|
| Desigualdad | != | Se usa para comparar si dos elmeentos son de diferente tipo o valor. |
| Mayor que | > | Se usa para comparar si un valor es mayor que otro.|
| Mayor o igual que| >= | Se usa para comparar si un valor es mayor o igual que otro|
| Menor de | < | Se usa para comparar si un valor es menor que otro.|
| Menor o igual que| <= | Se usa para comparar si un valor es menor o igual que otro.|

Estos operadores ayudan a establecer condiciones en los bloques de código que se pretenden ejecutar.

Existen varios tipos de condicionales en 
Python, entre los cuales están:

- `if` --> Es la forma más básica de condicional y se usa para ejecutar un bloque de código si la condición se cumple.
  
- `if-elif` --> Permite ejecutar un bloque de código si la condición se cumple (la condición es verdadera) y otro bloque de código si no se cumple (la condición es falsa).
  
- `if anidada` --> Este tipo de condicional consiste en anidar una condición dentro de otra lo que a su vez hace es evaluar múltiples condiciones de forma secuencial.
  
- `if-elif-else` --> Este condicional permite evaluar múltiples condiciones de forma ordenada, ejecutando el bloque de código a la condición que se cumple (que es verdadera).


Para la correcta comprensión del uso de los condicionales, se explican ejemplos a continuación:
- **Ejemplo 1**
 
En el primer ejemplo, se usa un condicional `if-elif-else` en el que se expone el caso de la cantidad de dinero a la hora de abrir una cuenta en un banco:
Los condicionales serán los siguientes:

Si tienes menos de 300€ NO puedes abrir una cuenta bancaria.

Si tienes hasta 10.000€ SI puedes abrir una cuenta bancaria.

Si tienes mas de 10.000€ no pueden ofrecerte este servicio, debes contratar otros servicios.

Suponiendo que tenemos 500€, creamos la variable `dinero = 500`.

Ahora los condicionales serian los siguientes, mediante el uso de operadores.
```python
if dinero < 300:
  print("Necesitas al menos 300€ para abrir una cuenta bancaria")
elif dinero < 10000:
  print("Puedes abrir una cuenta bancaria")
else:
  print("No podemos ofrecerte nuestros servicios")
```

De este modo, al tener `dinero = 500`, se cumpliría la primera condición y por tanto se imprimiría `Puedes abrir una cuenta bancaria`

- **Ejemplo 2**
  
En este caso se usan los condicionales anidados, con el ejemplo de la nota de un examen.
El condicional se divide en dos primeros bloques, si `nota` es mayor igual a 5 o si no.

```python
nota = 6.2
if nota >= 5:
  if nota > 9:
    print("Felicidades, sobresaliente!")
  elif nota > 7:
    print("Buen trabajo! Notable")
  elif nota > 6:
    print("Bien, aprobado")
  else:
    print("Aprobado, trabaja mas duro")
else:
  print("No has aprobado, sigue estudiando")
```
Si es menor de 5 se imprimirá `No has aprobado, sigue estudiando`. Del otro modo, si es mayor o igual a 5 se cumple el primer condicional y continúa con el siguiente bloque. Aquí hay mas condicionales, están anidados en el anterior. Depende de la nota que se haya sacado, se imprimirá un bloque de código.
Por ejemplo, si se saca un 6.2 en el examen, se recorre todo el condicional y se cumple por una parte el primero `if nota >= 5` y luego se cumple el `elif nota > 6` el cual imprime `Bien, aprobado` 

Además de lo comentado hasta ahora, los condicionales se pueden combinar dando lugar a muchas utilidades. Mediante el uso de `and`, `or`, `not` y también de `in`, se pueden ver si cierto elemento está dentro de otros, etc. En el siguiente caso, se quiere ver si el nombre `Pablo` está en la lista de nombres para ser mesa electoral. Se usa `in` del siguiente modo para ver si dicho nombre esta `in = dentro de` la `lista_electoral`.
```python
lista_electoral = ["Pedro", "Pablo", "Juan", "Maria", "Jose", "Luis", "Carlos",]

nombre = "Pablo"

if nombre in lista_electoral:
  print("Desafortunadamente, te toca mesa electoral")
else:
  print("Has tenido suerte, no te toca mesa electoral")
``` 
En este caso, el `nombre` Pablo está dentro de la `lista_electoral`por lo que le tocará estar en la mesa electoral.

También se pueden usar los condicionales múltiples para, por ejemplo, acceder a un servidor.
Para entrar a ese servidor, solo determinados usuarios con sus respectivas credenciales podrán entrar.
```python
usuario = "administrador"
email = "administrador@administrador.com"
contraseña = "12345"

if (usuario == "administrador" or email == "administrador@administrador.com" and contraseña == 12345):
  print("Credenciales correctas, bienvenido")
else:
  print("Credenciales incorrectas, intente de nuevo")
```
Si el usuario es "administrador" o el email es "administrador@administrador.com", y la contraseña es "12345", entonces se cumple el condicional y se imprime `Credenciales correctas, bienvenido`.
En el caso de que alguno de los valores sea diferente, no se cumple el condicional y por tanto imprime `Credenciales incorrectas, intente de nuevo`.


### Pregunta 2 - 	¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En Python, los bucles son una serie de instrucciones que se ejecutan hasta que se cumple una determinada condición.
Se distinguen dos tipos de bucles, los bucles `for` y los bucles `while`. La gran diferencia entre ellos reside, entre otras, en que el el bucle `for` se sabe cual es el inicio y el final del mismo, es decir, sabemos ya de antemano cuantas veces se va a repetir dicho bucle. Mientras tanto, los bucles  `while` se usan cuando no se sabe el numero determinado de veces que se va a repetir ese bucle, lo cual pueden dar lugar a bucles infinitos si no se definen bien.
Ambos tipos de bucles se pueden usar con listas, tuplas o diccionarios.

El bucle `for` se utiliza para iterar sobre una lista o cadena, y se usa para realizar una operación en cada elementos de esa lista o cadena.
La sintaxis de este bucle esta compuesta por el siguiente código:
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
La sintasix de este bucle esta compuesta por el siguiente código:
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
Se ejecuta el código que le sigue, se imprime `You´re rigth`.
Ademas, se le suma 1 a la x; siendo en el siguiente bucle 6 y en el siguiente 7. Esto se hace ya que sino daría lugar a un bucle infinito y haria que el sistema lo ejecutase una y otra vez hasta el infinito.
El bucle finalizará cuando el valor de x no cumpla la condición, es decir, al quinto bucle el valor será 10 y por tanto parará.


Además de ello, se pueden utilizar instrucciones `break`, `continue` y `pass`entre otras para crear diferentes funcionalidades dentro de los bucles Python. Estas instrucciones se ponen dentro del código bajo la instrucción de su bucle, después de `if`.
```
- `break`--> esta instrucción se usa para cerrar un bucle. 
- `continue`--> esta instrucción se usa para omitir la parte del bucle en la que se activa, y continua para acabar con el resto del bucle. En resumen, la iteración de interrumpe pero con `continue` hará que vuelva a la parte superior del bucle.  
- `pass` --> esta instrucción permite manejar la condición sin que el bucle se vea afectado, leyéndose el código de forma correcta y continuada. 
```

Ejemplo de uso:
Se pretende hacer un sorteo y hay 10 números. Si se obtiene el número 7 se obtiene el premio.
Usando la instrucción `break`, podemos iterar y que pare justo cuando saque el numero 7. El bucle itera y cuando llega a 7 se cierra, y tras impimir `PREMIO!`, imprime `Se acabó el sorteo`. 
```python
for premio in range(10):
  if premio == 7:
    print("PREMIO!")
    break
  print("El numero es " + str(premio))
print('Se acabó el sorteo')
``` 
```python
El numero es 0
El numero es 1
El numero es 2
El numero es 3
El numero es 4
El numero es 5
El numero es 6
PREMIO!
Se acabó el sorteo
```


Por otro lado, si usamos `continue` y la condición premio == 7 es cierta, la instrucción `continue`se activa y el código en el bucle se omite para esta iteración. Por tanto, en lo que se imprime no se verá `El numero es 7`. Después de ello continuarán las iteraciones hasta el final del bucle.
```python
for premio in range(10):
  if premio == 7:
    print("PREMIO!")
    continue
  print("El numero es " + str(premio))
print('Se acabó el sorteo')
```
```python
El numero es 0
El numero es 1
El numero es 2
El numero es 3
El numero es 4
El numero es 5
El numero es 6
PREMIO!
El numero es 8
El numero es 9
Se acabó el sorteo
```

Por ultimo, su usamos `pass`, y aunque la condición premio == 7 sea cierta, la instrucción `pass` hace que no se interrumpa la iteración y el bucle diga adelante, imprimiendo:

```python
for premio in range(10):
  if premio == 7:
    print("PREMIO!")
    pass
  print("El numero es " + str(premio))
print('Se acabó el sorteo')
```
```python
El numero es 0
El numero es 1
El numero es 2
El numero es 3
El numero es 4
El numero es 5
El numero es 6
PREMIO!
El numero es 7
El numero es 8
El numero es 9
Se acabó el sorteo
```

### Pregunta 3 - ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es una lista que permite crear listas de manera concisa y rápida.
La particularidad de estas listas es que permite definir la lista y sus elementos en una sola linea de código.

Para comprender mejor las listas de comprensión, se describe a continuación un breve ejemplo, en el que se  pretende obtener los números que son múltiplos de 2.
De forma tradicional se realizaría de este modo; utilizando un bucle `for` y una condición `if` para verificar si el numero es múltiplo de 2. Se crea una lista vacía `lista_multiplos`que a medida que el bucle vaya corriendo se vayan añadiendo con `append()` los múltiplos de 2.

```python
lista_multiplos = []
multiplos_2 = range(1, 24)

for num in multiplos_2:
  if num % 2 == 0:
    lista_multiplos.append(num)

print(lista_multiplos) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
```

Este mismo proceso se puede simplificar utilizando las listas por comprensión, de este modo:
```python
multiplos_2 = range(1, 24)

lista_multiplos = [num for num in multiplos_2 if num % 2 == 0]
print(lista_multiplos)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
```
Aquí se pretende obtener los números que son múltiplos de 2 usando un bucle dentro de una lista.  Se crea la lista `lista_mulitplos` en la que se se guardan los números si se cumplen unas condiciones. Estas condiciones son, que se guarda cada número que está en la lista `multiplos_2` si su división entre 2 es división exacta, es decir, que da 0. De este modo, todos los números que son divisibles de forma exacta con 2 se cumplen el condicional y se guardan en la nueva lista. 
En las listas de comprensión se pueden usar cualquier operador de Python y también los condicionales que se usan en Python.


### Pregunta 4 - ¿Qué es un argumento en Python?

En Python, un argumento es un elemento que se usa dentro de las funciones,
siendo el objetivo del argumento, proveer de un valor para que la función 
ejecute determinado código. 

Hay que destacar la diferencia entre ```parametros``` y ```argumentos```, ya que el primero
son las variables que se especifican dentro de los paréntesis cuando se define 
una función (por ejemplo, ```arg_1``` es parámetro), mientras que lo segundo son los 
valores que se pasan a esos parámetros cuando llamas a una función (en el ejemplo 
de abajo el argumento seria "Miguel").

Hay diferentes tipos de argumentos:

- **Argumentos por defecto:**  Estos son argumentos que tienen un valor predeterminado 
y se usan si no se provee a la función de otro argumento. Se asignan con =.
```python
def funcion_defecto(arg_1 = "Pedro"):
  print(arg_1 + " quiere comprarse un coche")

funcion_defecto()     # Pedro quiere comprarse un coche
funcion_defecto("Miguel")     # Miguel quiere comprarse un coche
```

- **Argumentos posicionales:** En los que los cuales los valores son asignados en base a
su posición cuando la función es llamada. 

En el ejemplo de a continuación, son 3 valores que se pasan a los argumentos en el 
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

- **Argumentos arbitrarios:** Se utilizan para pasar un numero variable de argumentos sin palabras 
clave a la función. Usando el asterisco ```*``` hará que ese argumento se comporte como un tupla.
```python
def refrescos(*args):
  for arg in args:
    print(arg)    

refrescos("cola", "pepsi", "fanta", "sprite")
```

- **Argumentos arbitrarios de palabras clave:** Se utilizan al mismo modo que los anteriores, pero 
se usan dos asteriscos en lugar de uno (**). Las funciones que tengan ** en un argumento, harán
que ese argumento se comporte como un diccionario, y al llamar la función se le asignan nombres 
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

La función lambda en Python es una función rápida para realizar operaciones simples  y no es necesario definir una función completa. Se utilizan para hacer mas sencillo y legible el código.
La sintaxis de esta función se hace mediante la creación de una variable que contiene dicha función. La función lambda le siguen los argumentos y dos puntos. Tras ello, una expresión.
En el siguiente ejemplo se quiere preguntar si se han cogido las llaves y las gafas.
Mediante una función tradicional se realizaría del siguiente modo:
```python
def pregunta(elemento_1, elemento_2):
  return f"¿Has cogido las {elemento_1} y las {elemento_2}?"

print(pregunta("llaves", "gafas"))    # ¿Has cogido las llaves y las gafas?
```

Mediante la función lambda, se acortaría la sintaxis para que fuese mas concisa:

```python
pregunta = lambda elemento_1, elemento_2: f"¿Has cogido las {elemento_1} y las {elemento_2}?"

print(pregunta("llaves", "gafas"))    # ¿Has cogido las llaves y las gafas?
```

La función lambda comparte muchas funcionalidades con las funciones tradicionales pero tiene ciertas limitaciones, asi como la imposibilidad de contener sentencias como `if` o `for`. 


Las funciones lambda pueden contener múltiples condicionales incluso contener listas de comprensión como las indicadas anteriormente. En el ejemplo de a continuación, se pretende que la función devuelva los múltiplos de 3 de una lista que tiene números del 0 al 30.

De forma tradicional sería:
```python
numeros = list(range(0, 31))
def multiplos_3(numeros):
    return [num for num in numeros if num % 3 == 0]

print(multiplos_3(numeros))   # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

Utilizando la función lambda, esta función es la que va a tomar la lista `numeros` y la expresión será una lista de comprensión. Esta ultima será que devuelva para cada número en `numeros` si se cumple que el numero es múltiplo de 3 exacto. 

```python
numeros = list(range(0, 31))
multiplos_3 = lambda numeros: [num for num in numeros if num % 3 == 0]

print(multiplos_3(numeros))      # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```


### Pregunta 6 - ¿Qué es un paquete pip?

Los paquetes de pip son colecciones de módulos y bibliotecas que proporcionan funcionalidades que van desde operaciones matemáticas hasta acceso a bases de datos, etc. Pip es el acrónimo de Pip Install Packages, que es el sistema de administración de paquetes. y su uso simplifica y facilita  el proceso de instalación y actualización de paquetes, asi como la gestion de dependencias entre ellas.

La instalación de los paquetes se realiza mediante `pip install nombre_del_paquete`. En el caso de que el paquete necesite de otras dependencias asi como de bibliotecas determinadas, pip se encarga de instalar todas esas dependencias de forma automática.

Una vez instalados se pueden importar al código para importar dicha funcionalidad de determinado modulo o biblioteca y usarlo.

Por ejemplo, para importar un modulo determinado se utiliza ```import```.
```python
import math
```

Además, se podría importar solo una función de cierto módulo, por ejemplo, la función ```sqrt``` del módulo ```math``` para poder realizar raíces cuadradas. En este breve ejemplo, se importa ```sqrt``` y se hace la raiz cuadrada de 144, que da 12.

```python
from math import sqrt
print(sqrt(144))      # 12
```

