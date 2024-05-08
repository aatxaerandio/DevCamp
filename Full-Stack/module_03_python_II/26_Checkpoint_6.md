# Clases en Python


Entre las diferentes tipos de elementos en Python, se encuentran un tipo de estrucutra que se utiliza para definir un nuevo tipo de objeto, llamadas **clases**.

Principalmente, las clases en Python sirven para agrupar datos (que son los atributos) y funciones (que son los metodos) que estan relacionados en un solo objeto. Esta agrupación permite la creacion de instancias de objetos que comparten caracreristicas comunes definidas en la clase.

Las clases permiten la creación de objetos con propiedades y comportamientos especificos, lo que ayud a organizar y modular el código, mejorar la legibilidad, facilitar la reutilización del codigo y mantener un codigo mas limpio y estructurado.

En cúanto a la sintaxis, simpre debe hacerse escribiendo class y luego el nombre de la clase con la primera letra en mayúscula. Por defecto, el primer atributo en las clases siempre está denominado como self. A parte de self, se pueden añadir mas atributos y funciones a la clase. Para entender mejor el uso de las clases, a continuación se expone un ejemplo:

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


## Decoradores en Python

Otro elemento particular de las clases de Python son los decoradores. Estos elementos permites modificar el comportamiento de las funciones sin cambiar su código, y su uso se basa en tomar otra funcion como argumento, agragandole funcionalidad adciional y devolviendo una nueva función. 
En cuanto a la sintaxis, se usa "@nombre_decorador" y se usan de la siguiente manera:














































Dentro de la clase creada, utilizaremos un metodo (funcion) y un atributo, que al ser solo uno siempre será self.
