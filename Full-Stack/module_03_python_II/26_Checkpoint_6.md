# Clases en Python


Entre las diferentes tipos de elementos en Python, se encuentran un tipo de estrucutra que se utiliza para definir un nuevo tipo de objeto, llamadas **clases**.

Principalmente, las clases en Python sirven para agrupar datos (que son los atributos) y funciones (que son los metodos) que estan relacionados en un solo objeto. Esta agrupación permite la creacion de instancias de objetos que comparten caracreristicas comunes definidas en la clase.

Las clases permiten la creación de objetos con propiedades y comportamientos especificos, lo que ayud a organizar y modular el código, mejorar la legibilidad, facilitar la reutilización del codigo y mantener un codigo mas limpio y estructurado.

En cuanto a la sintaxis, siempre debe hacerse escribiendo class y luego el nombre de la clase con la primera letra en mayúscula. Por defecto, el primer atributo en las clases siempre está denominado como self. A parte de self, se pueden añadir mas atributos y funciones a la clase. Para entender mejor el uso de las clases, a continuación se expone un ejemplo:

Ejemplo: Se pretende crear una clase que se llame Usuario, y se le añadirán dos funciones saludos_1 y saludos_2. En este caso, solo se usa un atributo, por defecto, self.

```python
class Usuario:
  def saludos_1(self):
    return "Eres un usuario nuevo"

  def saludos_2(Self):
    return "No eres un usuario nuevo"
```

Además de ello, se crea una instancia, es decir, se crea un objeto a partir de la clase. Esto se realiza utilizando el nombre de la clase seguido de parentesis.

```python
persona_1 = Usuario()   # Creación de la instancia.
```

Para acceder a los atributos y los métodos, se utiliza la notación ".", poniendo primero la instancia y luego el metodo que se quiere acceder. En el ejemplo de acontinuación, se accede con la misma instancia a metodos diferentes, resultado en diferentes respuestas:
 
```python
print(persona_1.saludos_1())
print(persona_1.saludos_2())
```


## Metodo constructor

En las clases, también se pueden utilizar métodos específicos como el método constructor.
En este caso, el método constructor tiene la particularidad que se llama por __init__ y se ejecuta **automáticamente** cuando se crea una instancia de la clase. Este método siempre se usa para inicializar los atributos de la clase.
Para entenderlo mejor, se expone el siguiente ejemplo:

```python
class Factura:
  def __init__(self, nombre, apellidos, importe):
    self.nombre = nombre
    self.apellidos = apellidos
    self.importe = importe

  def saludos(self):
    return f"Hola {self.nombre} {self.apellidos}, su compra total asciende a un total de {self.importe}€."

cliente_1 = Factura("Aitor", "Atxaerandio", 100)
```
En este caso, solo hemos accedido al segundo metodo, pero como el primero __init__ siempre se ejecuta automaticamente, tendremos el siguiente resultado:

```python
print(cliente_1.saludos())    # Hola Aitor Atxaerandio, su compra total asciende a un total de 100€.
```

## Funciones Setter y Getter
Antes de saber que son los metodos getter y setter, hay que saber la sintaxis de los atributos de python.
Con el fin de no reescribir y eliminar atributos, en Python se utilizan las barra-bajas para determinar si un atributo es privado y/o protegido.
 - Para crear atributos protegidos se usa _ .
 - Para crear atributos privados se usan __ .

Estos atributos, al ser privados o protegidos, no pueden modificarse por si solos, y se necesita de metodos especiales para poder acceder a ellos. Aqui es donde entra en juego los metodos Setter y Getter, que son parte fundamental de python y se usan para modificar los atributos de una clase de manera controlada.

En el caso del método **getter**, se emplea para obtener el valor de un atribulo privado, permitiendo una lectura segura de los datos almacenados en una clase. Para los metodos getter, se usa la sintaxis **@property** para obetenre el valor de un atributo privado, ubicandolo delante del metodo que queremos que devuelva el valor.
En el caso de **setter**, se usa para asignar un valor a un atribulo privado, lo que posibilidad la modificación controlada de dicho atributo. En este caso, la sintaxis a utilizar es **@nombre_metodo.setter** delante del metodo que queremos mopdificar.

Para explicarlo mejor, se describe un ejemplo a continuación:

```python
class Factura:

    def __init__(self, cliente, total):
        self._cliente = cliente
        self._total = total

    def texto(self):
        return f'{self._cliente} owes: ${self._total}'

    @property          # Metodo Getter
    def client(self):
        return self._cliente

    @client.setter      # Metodo Setter
    def cliente(self, cliente):
        self._client = cliente

    @property          # Metodo Getter
    def total(self):
        return self._total

```

En esta clase llamada factura tiene como ibjetivo representar una factura con informacion sobre un cliente y el total de la factura.
1. Metodo __init__ --> Es un constructor de la clase, y se ejectua automaticamente e inicializa los atributos de la clase, que son cliente y total. Cliente almacena el nombre del cliente y total almacena el total de la factura.
2. Metodfo texto --> Este metodo devuelce un string mostrando el texto de la factura.
3. Decorador @property y metodos cliente y totalc.
   - Decorador @property: se usa para crear un metodo **getter** que permite acceder al valor del atributo como si fuera un atributo de lectura.
      - Metodo cliente: es un getter que devuelve el valor del atributo cliente.
      - Metodo total: es otro getter que devuelve el valor del atributo total.
   - Decorador @cliente.setter: se usa para crear un metodo **setter** asignando un nuevo valor al atributo cliente.








## Propiedades y decoradores de las clases en Python

Las propiedades de las clases en Python son atributos especiales que permiten controlan el acceso a los datos de una clase y automatizar la llamada a metodos getter y setter. al utilizar las propiedades, se garantiza un acceso mas intuitivo a los atributos de la clase y se elimina la necesidad de llamar explícitamente a métodos setter y getter.
las

## Decoradores en Python

Otro elemento particular de las clases de Python son los decoradores. Estos elementos permites modificar el comportamiento de las funciones sin cambiar su código, y su uso se basa en tomar otra función como argumento, agregándole funcionalidad adicional y devolviendo una nueva función. 
En cuanto a la sintaxis, se usa "@nombre_decorador" y se usan de la siguiente manera:














































Dentro de la clase creada, utilizaremos un metodo (funcion) y un atributo, que al ser solo uno siempre será self.
