# Bucles en JavaScript

Al igual que en otros lenguajes de programación, en JavaScript podemos utilizar bucles o "loops" para hacer algo repetidamente de forma rápida y sencilla.

Hay muchos tipos de bucles pero esencialmente todos hacen lo mismo; repiten una accion varias veces. 

Los diversos mecanismos de bucle ofrecen diferentes formas de determinar los puntos de inicio y terminación del bucle. Hay varias situaciones que son fácilmente atendidas por un tipo de bucle que por otros.

Para explicar correctamente el uso de bucles en JavaScript, se utilizará la siguiente variable como ejemplo util para todos los bucles.

```javascript
var players = [
	'Altuve',
	'Bregman',
	'Correa',
	'Springer'
];
```

Las declaraciones para bucles proporcionadas en JavaScript son:


**1. Declaracion `for`**

Un ciclo for se repite hasta que una condición especificada se evalúe como false. 

**La sintaxis es:**
```javascript
for ([expresiónInicial]; [expresiónCondicional]; [expresiónDeActualización])
  instrucción
```

- Se ejecuta la expresión de iniciación expresión Inicial, si existe. Esta expresión normalmente inicia uno o más contadores de bucle, pero la sintaxis permite una expresión de cualquier grado de complejidad. Esta expresión también puede declarar variables.
- Se evalúa la expresión expresión Condicional. Si el valor de expresión Condicional es verdadero, se ejecutan las instrucciones del bucle. Si el valor de condición es falso, el bucle for termina. (Si la expresión condición se omite por completo, se supone que la condición es verdadera).
- Se ejecuta la instrucción. Para ejecutar varias instrucciones, usa una declaración de bloque ({ ... }) para agrupar esas declaraciones.
- Si está presente, se ejecuta la expresión de actualización expresiónDeActualización.
- El control regresa al paso 2.

**Ejemplo:**
```javascript
for(let i=0; i<players.length; i++){
	console.log(players[i]);
	/* imprime:
		Altuve
		Bregman
		Correa
		Springer
	*/
}
```
- Se crea la variable `i` que es igual a `0`.
- Se establece el condicional que dice que si `i` es menor que la longitud de la variable `players` que sabemos que su valor es 3.
- Al final de cada bucle o iteración, se le añade 1 al valor de `i`.
- De este modo, en la primera iteración se imprimirá `Altuve` y se le añadirá 1 a `i`. En la siguiente iteración se imprimirá `Bregman`y se le volverá a añadir 1 a `i`. El bucle finalizará despues de haber impreso todos los nombres y al no cumplirse de nuevo la condición, ya que `i` será mayor a la longitud de la variable `players`. <br>


**2. Declaración `for...in`**

La instrucción for...in itera una variable especificada sobre todas las propiedades enumerables de un objeto. Para cada propiedad distinta, JavaScript ejecuta las instrucciones especificadas. Una declaración for...in tiene el siguiente aspecto:

**La sintaxis es:**
```javascript
for (variable in objeto)
  instrucción
```

**Ejemplo:**

```javascript
for(let player in players){
    console.log(player)
    /* imprime:
    0
    1
    2
    3 */
}
```
- Mediante este bucle queremos iterar sobre las propiedades ENUMERABLES de un objeto, es decir, estamos iterando sobre `players`.
- `let player in players`: Esta es la parte que define la variable de iteración. En este caso, `player` es una variable que se asignará sucesivamente a cada una de las propiedades enumerables del objeto players.
- El bucle continúa mientras haya propiedades enumerables en el objeto players que no se hayan recorrido. 
-  En este caso, se imprime el valor de la variable player en la consola.
- Después de cada iteración, el bucle pasa a la siguiente propiedad enumerable del objeto players.
- En resumen, este bucle for...in recorre todas las propiedades enumerables del objeto players y muestra el nombre de cada propiedad en la consola.

En el caso de que queramos imprimir los nombres de los jugadores, tendriamos que usar `player` en corchetes, ya que de este modo, `player`representa al `indice`, y no el valor.

```javascript
for(var player in players){
	// 'player' representa el índice, no el valor
	console.log(players[player]);
	/* imrpime:
		Altuve
		Bregman
		Correa
		Springer
	*/
}
```
- En este caso, en cada iteraccion del bucle se imprime el valor asociado a la propiedad actual (`player`) del objeto `players`. El valor se obtiene mediante `players[player]`. <br>


**3. Declaración `for...of`**

La declaración for...of crea un bucle que se repite sobre objetos iterables, invocando un bucle de iteración personalizado con declaraciones que se ejecutarán para el valor de cada distinta propiedad.

**La sintaxis es:**
```javascript
for (variable of objeto)
  expresión
```

**Ejemplo:**

```javascript
for(let player of players){
    console.log(player);
    /* imprime:
    	Altuve
    	Bregman
    	Correa
    	Springer */
}
```

Se ve que si usamos bucles `for...in` y `for...of` podemos llegar al mismo resultado. La gran diferencia entre unos y otros es que mientras que `for...in` itera sobre los nombres de propiedad, `for...of` itera sobre los valores de propiedad. Por tanto, en los bucles `for...in` tenemos que aplicar `players[player]` para que nos imprima los nombres de la propiedad.  <br>


**4. Declaración `forEach`**

Una variante de los bucles `for` es `forEach`.

forEach es un método de las arrays de JavaScript que se utiliza para iterar sobre los elementos de un array y ejecutar una función determinada en cada uno de ellos. A diferencia del bucle for, forEach no tiene un contador y no permite la interrupción o el salto de iteración.
En general, forEach puede ser más rápido que for debido a que es más simple y no requiere la gestión de un contador y la comprobación de condiciones.

**Ejemplo:**

```javascript
players.forEach(function(element){
	console.log(element);
	/* imprime:
		Altuve
		Bregman
		Correa
		Springer
	*/
});
```
<br>

**5. Declaración `while`**

Una declaración while ejecuta sus instrucciones siempre que una condición especificada se evalúe como true. Una instrucción while tiene el siguiente aspecto:

**La sintaxis es:**
```javascript
while (condición)
  expresión
```
Si la condición se vuelve false, la instrucción dentro del bucle se deja de ejecutar y el control pasa a la instrucción que sigue al bucle.

La prueba de condición ocurre antes de que se ejecute la expresión en el bucle. Si la condición devuelve true, se ejecuta la expresión y la condición se prueba de nuevo. Si la condición devuelve false, la ejecución se detiene y el control se pasa a la instrucción que sigue a while.

**Ejemplo:**
```javascript
var i = 0;
while(i < players.length){
	console.log(players[i]);
	i++; // NO OLVIDAR AUMENTAR EL CONTADOR; SINO SERIA UN BUCLE INFINITO.
	/* este bucle imprime:
		Altuve
		Bregman
		Correa
		Springer
	*/
}
```
- Siendo `i = 0`en la primera iteracción, primero se cumple la condición y luego se imprime `Altuve`. Se le añade 1 al contador y se vuelve a iterar en el bucle.
- En la segunda iteración el valor de `i = 1` y se sigue compliendo la condicion, ya que el valor de `i` sigue sienod mas pequeño que la longitud de la variable `players`. Se imprime `Bregman` y se vuelve a añadir 1 al contador, para que el valor de `i` sea 2 en la siguiente iteración. 
- el bucle finaliza cuando el valor de `i` es mas alto que la longitud de `players`.
<br>

**6. Declaración `do...while`**

La instrucción do...while se repite hasta que una condición especificada se evalúe como falsa.

**La sintaxis es:**
```javascript
do
  expresión
while (condición);
```
`Exposición` siempre se ejecuta una vez antes de que se verifique la condición.
Si condición es true, la declaración se ejecuta de nuevo. Al final de cada ejecución, se comprueba la condición. Cuando la condición es false, la ejecución se detiene y el control pasa a la declaración que sigue a do...while.

**Ejemplo:**
```javascript
var i = 0;
do{
	console.log(players[i]);
	i++; // NO OLVIDAR AUMENTAR EL CONTADOR; SINO SERIA UN BUCLE INFINITO.
	/* este bucle imprime:
		Altuve
		Bregman
		Correa
		Springer
	*/
}while(i < players.length);
```
- En la primera iteración al ser `i=0`, se imprime el primer elemento de la variable `players` que es `Altuve`. 
- Luego recorre el bucle y se le añade 1 al valor de `i` y continua si el calor de `i` es menor que la longitud de la variable `players` que es de 3.
- En base al valor de `i `se irán imprimiendo los elementos de la variable `players`.
- El bucle finalizará cuanod el valor de `i` sea mayor que la longitud de `players`. 
<br>

**7. Declaración labeled**

Una label proporciona una instrucción con un identificador que te permite hacer referencia a ella en otra parte de tu programa. Por ejemplo, puedes usar una etiqueta para identificar un bucle y luego usar las declaraciones break o continue para indicar si un programa debe interrumpir el bucle o continuar su ejecución.La sintaxis de la instrucción etiquetada es similar a la siguiente:label : instrucción

El valor de label puede ser cualquier identificador de JavaScript que no sea una palabra reservada. La declaración que identifica a una etiqueta puede ser cualquier enunciado.

Para ver mejor su uso, se utiliza como ejemplo la variable `frutas`que contiene 5 elementos;

```javascript
const frutas = ['manzana', 'banana', 'naranja', 'pera', 'kiwi'];
```

**7. 1. Declaración `break`**

Usa la instrucción break para terminar un bucle y transfiere el control a la siguiente declaración.

**Ejemplo:**
```javascript
const frutas = ['manzana', 'banana', 'naranja', 'pera', 'kiwi'];

for (let i = 0; i < frutas.length; i++) {
  if (frutas[i] === 'pera') {
    console.log('¡Encontré una pera! Se acaba el bucle!');
    break;
  }
  console.log(`En este iteración, la fruta es: ${frutas[i]}`);
}
/*
En este iteración, la fruta es: manzana
En este iteración, la fruta es: banana
En este iteración, la fruta es: naranja
¡Encontré una pera! Se acaba el bucle!
*/
```
Comienza el bucle sienod `i = 0`, y tiene que cumplirse que `i` sea menor que la longitud de la variable `frutas`. Despues se le añade 1 al valor de `i` y entra en el siguiente condicional, en el que en base al valor de `i` como índice, se pretende ver si la fruta selccionada es igual a `pera`. 
- Si no es `pera`, se impimirá `"En esta iteración, la fruta es (la fruta determinada para esta iteración)"`.
- Si por el contrario es `pera`, se imprime `"¡Encontré una pera! Se acaba el bucle!'"` y el bucle se finaliza aquí. Es decir, no hay mas iteraciones.


**7. 2. Declaración `continue`**

La instrucción continue se puede usar para reiniciar un while, do-while, for, o declaración label.

- Cuando utilizas continue sin una etiqueta, finaliza la iteración actual del while, do-while o for y continúa la ejecución del bucle con la siguiente iteración. A diferencia de la instrucción break, continue no termina la ejecución del bucle por completo. En un bucle while, vuelve a la condición. En un bucle for, salta a la expresión-incremento.
- Cuando usas continue con una etiqueta, se aplica a la declaración de bucle identificada con esa etiqueta.

**Ejemplo:**
```javascript
const frutas = ['manzana', 'banana', 'naranja', 'pera', 'kiwi'];

for (let i = 0; i < frutas.length; i++) {
  if (frutas[i] === 'pera') {
    console.log('¡Encontré una pera! Pero se continua con el bucle!');
    continue;
  }
  console.log(`En este iteración, la fruta es: ${frutas[i]}`);
}
/* IMPRIME
En este iteración, la fruta es: manzana
En este iteración, la fruta es: banana
En este iteración, la fruta es: naranja
¡Encontré una pera! Pero se continua con el bucle!
En este iteración, la fruta es: kiwi
*/
```
En este caso, pese a cumplirse la condición, al poner `continue`, el bucle no se cierra y continua hasta que el primer condicional `i < frutas.length` deja de cumplirse.


# var, let y conts. Usos y diferencias

Las variables `var`, `let`, y `const` en JavaScript se utilizan para declarar y manejar variables de manera efectiva. Cada una tiene sus propias características y ventajas, que se detallan a continuación:

|              | Var | Let | Const |
| ---------- | --------- | ------- | ------- |
| **Ámbito** | declara una variable en el ámbito local actual (la función actual) y se hereda a los niveles superiores.| declara una variable en el ámbito global, local para la función o de bloque. | declara una variable en el ámbito global, local para la función o de bloque, similar a let. |
| **Hoisting** | se elevan a la parte superior del ámbito, lo que significa que se pueden utilizar antes de ser declaradas. | también se elevan a la parte superior, pero no se inicializan con undefined como var. Si se intenta utilizar una variable let antes de declararla, se producirá un error de referencia. | también se elevan a la parte superior, pero no se inicializan con undefined como var. Si se intenta utilizar una variable const antes de declararla, se producirá un error de referencia. |
| **Reasignación** | pueden ser reasignadas. | pueden ser reasignadas. | no pueden ser reasignadas. |
| **Inicialización** | No es necesario inicializar una variable con var al momento de su declaración. | No es necesario inicializar una variable con let al momento de su declaración. | Es necesario inicializar una variable con const al momento de su declaración. |

**En RESUMEN:**
`var` es la forma más antigua y se recomienda evitar su uso a menos que sea necesario para compatibilidad con navegadores antiguos.
`let` es una mejor opción que var porque evita el problema de sobreescritura de variables y tiene un ámbito más preciso.
`const` se utiliza para declarar constantes que no se pueden reasignar, pero pueden ser mutables si se trata de objetos o arrays.


# Función de flecha // Arrow function

Una función de `flecha`, también conocida como función `arrow`, es una forma concisa de definir funciones en JavaScript. Fue introducida en el estándar ECMA Script 6 (ES6) y se caracteriza por utilizar el símbolo de flecha o arrow (=>) en lugar de la palabra clave `function` para definir la función. Estas funciones tienen varias ventajas sobre las funciones tradicionales, incluyendo una sintaxis más concisa y la capacidad de omitir la sentencia return si la función devuelve un valor implícito.

**Definición y Uso**<br>
Una función de flecha se define utilizando la sintaxis `parametros => expresión`. La expresión se evalúa y devuelve el resultado. Las funciones flecha son anónimas, lo que significa que no tienen un nombre explícito.

**Ventajas**<br>
**1. Sintaxis Concisa:** Las funciones flecha son más breves y fáciles de leer que las funciones tradicionales. Esto puede mejorar la legibilidad del código y reducir la cantidad de espacio utilizado.<br>
**2. No Necesidad de Return:** En una función de flecha, el return es implícito, lo que significa que no es necesario escribir explícitamente la palabra clave return si la función devuelve un valor.<br>
**3. Uso de this:** Las funciones flecha establecen this según el contexto en el que se definen, en lugar de según el objeto que las llama. Esto puede ser útil al trabajar con objetos y eventos en JavaScript. <br>
**4. Funciones de Callback:** Las funciones flecha son una excelente opción para funciones de callback, ya que no requieren la palabra clave return y pueden ser utilizadas directamente.<br>

**Desventajas**<br>
**1. No se Pueden Usar con call, apply y bind:** Las funciones flecha no pueden ser utilizadas con los métodos call, apply, y bind, ya que estas funciones se basan en el objeto this y no se ajustan a la forma en que las funciones flecha manejan this.<br>
**2. No se Pueden Usar como Métodos:** Las funciones flecha no pueden ser utilizadas como métodos de un objeto, ya que no establecen this según el objeto que las llama.<br>
**3. No se Pueden Depurar:** Debido a que las funciones flecha son anónimas, pueden ser más difíciles de depurar que las funciones tradicionales, ya que no hay un nombre explícito para rastrear errores.<br>

Para entender su uso, se expone el siguiente ejemplo:

Una declaración de función regular seria:
```javascript

function greetings() {
	console.log(`Hello!`)
}
greetings() // Hello!
```
O otro ejemplo con argumentos dentro:

```javascript
function identification(name, surname){
  console.log(`"Hi there ${name} ${surname}, wellcome!`);
}

identification("Juan", "Perez")     // Imprime --> "Hi there Juan Perez, wellcome!
```

Mediante el uso de `funciones flecha`se consigue el mismo resultado mediante una sintaxis mas simple:

```javascript
const greetings = () => {
  console.log("Hello!");
}
greetings()  // Hello!
```
O en el caso de la segunda función con dos argumentos:

```javascript
const identification = (name, surname) =>  {
  console.log(`"Hi there ${name} ${surname}, wellcome!`);
}

identification("Juan", "Perez")    // "Hi there Juan Perez, wellcome!
```

Las funciones flecha en JavaScript son una herramienta útil para simplificar y concisar el código, especialmente en situaciones donde se requiere un manejo intuitivo de this y se pueden omitir la palabra clave function y la sentencia return. Sin embargo, es importante considerar las limitaciones y desventajas de su uso, como la imposibilidad de ser utilizadas como constructores o métodos abreviados.
<br>


# Deconstrucción de variables

La desestructuración o desestructuración de variables en JavaScript es una técnica que permite extraer valores de arreglos o propiedades de objetos y asignarlos a nuevas variables de manera eficiente y legible. Esta técnica se introdujo en ECMAScript 6 y ha mejorado significativamente la forma en que se escribe código JavaScript.

La sintaxis para la deconstruccion de variables difiere segun lo que se pretende realizar. Aun asi, de forma general se escriben en el lado izquierdo de la asignación para definir qué valores desempacar de la variable origen.

Para entender mejor el uso de la deconstruccion de variables se van a plicar los siguientes ejemplos:<br>

**1. Asignacion básica de variables**

```javascript
const numeros = ["uno", "dos", "tres"];

const [rojo, amarillo, azul] = numeros;
console.log(rojo); // "uno"
console.log(amarillo); // "dos"
console.log(azul); // "tres"
```
En el que se parte de una variable `numeros` y se desestructura en diferentes variables.
<br>

**2. Aisgnación separada de la declaración**
A una variable se le puede asignar su valor mediante una desestructuración separada de la declaración de la variable.
```javascript
let a, b;

[a, b] = [1, 2];
console.log(a); // 1
console.log(b); // 2
```
En el que dadas `a`y `b`, se les asigna los valores de `1` y `2` a cada una de ellas, respectivamente.
<br>

**3. Intercambio de variables**

Los valores de dos variables se pueden intercambiar en una expresión de desestructuración.

```javascript
let juego = 1;
let set = 3;

[juego, set] = [set, juego];
console.log(set); // 1
console.log(juego); // 3
```
En este caso, el valor de las variables `juego`y `set` se intercambian mediante la expression de desestructuración.
<br>

**4. Asignar el resto de un arreglo a una variable**
En este caso, podemos asignar el resto a una variable, en este caso, `c`.
De este modo, `a` se asigna a `cabeza`, `b` se asigna a `brazos` y el resto, es decir `[ 'piernas', 'torax' ]` a `c`. 
```javascript
const [a, b, ...c] = ["cabeza", "brazos", "piernas", "torax"];
console.log(a); // cabeza
console.log(b); // brazos
console.log(c); // [ 'piernas', 'torax' ]
```
<br>

**5. Desestructuración de arrays**
Partiendo de un array que contenga los nombres de los ganadores de una carrera:
```javascript
const lista_nombres = ["Juan", "Pedro", "Miguel"];

const [primero, segundo, tercero] = lista_nombres;

console.log(primero); // Juan
console.log(segundo); // Pedro
console.log(tercero); // Miguel
```
De este modo se desestructura la variable `lista_nombres` y se crean las variables `primero`, `segundo` y `tercero` con los valores de la anterior, es decir, con los nombres de los tres primeros clasificados. 
<br>

**6. Desestrucutracion en funciones**

```javascript
const usuario = {
  name: "Aitor",
  email: "email@email.com",
  password: "password",
}
```
En este caso, vamos a realizar la deconstruccion usando una función flecha, en la que se le pasan los objetos.
```javascript
const entrada = ({name, email, password}) => {
  console.log(`${name}! Recuerda que tu email es ${email} y tu contraseña es ${password}`);
};

entrada(usuario);   // Aitor! Recuerda que tu email es email@email.com y tu contraseña es password
```

1. Se define un objeto usuario con tres propiedades: name, email, y password. Estas propiedades contienen información personal del usuario.
2. La función `entrada` es una función de orden superior que toma un objeto como argumento. Este objeto debe contener las propiedades `name`, `email`, y `password`.
3. Dentro de la función `entrada`, se utiliza una cadena de texto que combina los valores de `name`, `email`, y `password` del objeto pasado como argumento. Luego, se imprime este mensaje en la consola utilizando `console.log`.
4. Finalmente, se llama a la función `entrada` y se le pasa el objeto `usuario` como argumento. Esto significa que se utilizarán los valores de `name`, `email`, y `password` del objeto `usuario` para generar el mensaje que se imprime en la consola.
<br>

**7. Valores por defecto en objetos**

En este caso, se pueden aplicar valores por defecto en objetos y/o también modificarlos.

Al igual que en anterior ejemplo, se usa la función flecha para realizar la desestructuración para extraer las propiedades `titulo`y `resumen` del objeto pasado como parámetro. La propiedad `resumen` tiene un valor predeterminado de "Novela de Jack London" si no se proporciona un valor explícito.

La función se utiliza dos veces en el código:

1. La primera vez, se pasa el objeto `blog`, que contiene las propiedades `titulo` y `resumen`. La función imprime la cadena con los valores de `titulo` y `resumen` correspondientes.
2. La segunda vez, se pasa el objeto `anotherBlog`, que solo contiene la propiedad `titulo`. La función imprime la cadena con el valor de `titulo` y el valor predeterminado de `resumen`, que es "Novela de Jack London".

```javascript
const blog = {
  titulo: "Colmillo Blanco",
  resumen: "Narra la historia de un perro en la epoca de la fiebre del oro, en Canadá"
}

const informacion = ({titulo, resumen = "Novela de Jack London"}) => {
  console.log(`
      info-titulo=${titulo}
      info-resumen=${resumen}
  `);
};

informacion(blog);
/* se imprime:
    info-titulo=Colmillo Blanco
    info-resumen=Narra la historia de un perro en la epoca de la fiebre del oro, en Canadá*/

const anotherBlog = {titulo: "Colmillo Blanco V2"};
informacion(anotherBlog);
/* se imprime:
    info-titulo=Colmillo Blanco V2
    info-resumen=Novela de Jack London
*/
```

**En resumen; las ventajas de la desestructuración de variables son:**
**- Código más legible:** La desestructuración de variables simplifica el código al evitar la necesidad de asignaciones repetidas.
**- Mejora la eficiencia:** Reduce la cantidad de código necesario para realizar operaciones comunes.
**- Flexibilidad:** Permite asignar valores predeterminados y asignar nombres diferentes a variables.
<br>

# Operador de extensión en JV, usos y funciones

El operador de extensión en JavaScript se utiliza para expandir una variable o objeto en una función o en una variable literal. Esto permite pasar los elementos de una variable como argumentos individuales a una función o combinarlos en una nueva variable. 

Se denota con tres puntos (...) seguidos de una expresión o un iterable.

Entre los usos del operador de extensión están:
<br>

**1. Concatenar Arrays:**<br> Utiliza el operador spread para distribuir los elementos de un array en otro array. Esto es especialmente útil para concatenar arrays o crear una copia superficial de un array.

```javascript
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];

let concatenado = [...array1, ...array2];
console.log(concatenado); // Output: [1, 2, 3, 4, 5, 6]
```
<br>

**2. Extendiendo Cadenas de Texto:** <br>Utiliza el operador spread para desglosar los caracteres de una cadena en un array. Esto es útil para convertir una cadena en un array de caracteres que puede manipularse o combinarse con otros arrays utilizando métodos de array.

```javascript
let cadena = "Hola";
let array = [...cadena];
console.log(array); // Output: ["H", "o", "l", "a"]
```
<br>

**3. Combinación con el Parámetro Rest:**<br> El operador spread puede utilizarse junto con otras funciones modernas de JavaScript, como la desestructuración de arrays y objetos, para habilitar potentes operaciones de manipulación de datos.

```javascript
function combineObjects(...objects) {
    return { ...objects };
}

let obj1 = { a: 1, b: 2 };
let obj2 = { c: 3, d: 4 };
let obj3 = { e: 5, f: 6 };

let combinedObject = combineObjects(obj1, obj2, obj3);
console.log(combinedObject); // Output: { a: 1, b: 2, c: 3, d: 4, e: 5, f: 6 }
```
<br>

**4. Copiar una variable:**<br> Utiliza el operador spread para crear una copia superficial de una variable. Esto es especialmente útil cuando se necesita una copia independiente de la variable original.

```javascript
// Arreglo original
const original = [1, 2, 3, 4, 5];

// Copia superficial del arreglo utilizando el operador spread
const copy = [...original];

// Modificamos el arreglo original
original.push(6);

// El arreglo copia no se ve afectado
console.log(copy); // [1, 2, 3, 4, 5]
console.log(original); // [1, 2, 3, 4, 5, 6]
```
En este ejemplo, se crea una copia superficial de la variable `original` utilizando el operador spread (...). La copia se almacena en la variable `copy`. Luego, se modifica la variable original agregando un nuevo elemento, pero la copia no se ve afectada.


# Programación orientada a objetos / Object Oriented Programming - OOP

La programación orientada a objetos (Object Oriented Programming, OPP) es un paradigma de programación que estructura los programas alrededor de objetos, que son entidades que combinan datos y funciones. Este enfoque permite la reutilización de código, la modularidad y una mayor organización del software.

La POO se utiliza en todas partes, desde sistemas operativos hasta software comercial y de código abierto. Sus beneficios se ponen de manifiesto cuando el proyecto alcanza un cierto nivel de complejidad.

 **VENTAJAS**<br>
**1. Reusabilidad y ampliación del código**: Permite reutilizar y ampliar el código de manera efectiva.<br>
**2. Sistemas más complejos**: Permite crear sistemas más complejos y escalables.<br>
**3. Abstracción**: Permite abstraer problemas y representar el mundo real de manera fiel.<br>
**4. Agiliza el desarrollo**: Facilita el desarrollo de software.<br>
**5. Trabajo en equipo**: Facilita el trabajo en equipo.<br>
**6. Mantenibilidad**: Los programas orientados a objetos son más fáciles de leer y comprender debido a la abstracción y encapsulamiento.<br>
**7. Modificabilidad**: Facilita la adición, supresión o modificación de nuevos objetos.<br>
**8. Fiabilidad**: Divide el problema en partes más pequeñas, lo que facilita la prueba y depuración de errores. <br>


 **DESVENTAJAS**<br>
**1. Complejidad**: La creación de clases, objetos y relaciones entre ellos puede ser confusa para programadores novatos.<br>
**2. Sobrecarga de memoria**: La POO puede consumir más memoria que otros enfoques, especialmente en aplicaciones que requieren una gestión eficiente de recursos.<br>
**3. Rendimiento**: El proceso de creación y manipulación de objetos puede ralentizar la ejecución del programa.<br>
**4. Jerga**: La POO utiliza un lenguaje específico que puede ser difícil de entender al principio.<br>
**5. Dificultades a la hora de paralelizar el código**: El encapsulamiento del estado interno puede hacer que sea difícil paralelizar el código.<br>
**6. Pérdidas de rendimiento**: La naturaleza dinámica de la POO puede producir pérdidas de rendimiento debido a la falta de optimizaciones estáticas.<br>
**7. Curva de aprendizaje pronunciada**: Comprender los conceptos fundamentales de la POO puede requerir tiempo y esfuerzo adicional.<br>
**8. Rigidez en el diseño**: Una vez que se definen las clases y las relaciones entre ellas, realizar cambios significativos en la estructura del código puede ser complicado y propenso a errores.<br>

Para explicar bien el uso de la Programación orientada a objetos, vamos a aplicar el ejemplo de a continuacion:


```javascript
class Persona {

  constructor({ nombre, rol = "asistente" }) {
    this.nombre = nombre;
    this.rol = rol;
  }

  // INSTANCE METHOD
  Detalles() {
    console.log(`${this.nombre}: ${this.rol}`);
  }

  // STATIC METHOD
  static holaMundo() {
    console.log("Hola buenas!");
  }

  static canTeach(instructor) {
    return instructor.rol === "clase";
  }
}
```
**CONSTRUCTOR**<br>
El constructor de la clase Persona se define con el método constructor(). Cuando se crea una nueva instancia de Persona, el constructor se llama y se le pasa un objeto con las propiedades nombre y rol. Si no se proporciona un valor para rol, se asigna el valor predeterminado de "asistente". Dentro del constructor, se asignan los valores de nombre y rol a las propiedades de la instancia de Persona utilizando la palabra clave this.

**MÉTODOS de INSTANCIA**<br>
La clase `Persona` tiene un método de instancia llamado `Detalles()`. Este método imprime en la consola una cadena que muestra el `nombre` y el `rol` de la persona.<br>

**MÉTODOS ESTÁTICOS**<br>
La clase `Persona` también tiene dos métodos estáticos:

- `holaMundo()`: Este método simplemente imprime "Hola buenas!" en la consola.
- `canTeach(instructor)`: Este método toma un objeto instructor como argumento y devuelve true si el rol del instructor es "clase", y false en caso contrario.


**CREACIÓN de INSTANCIAS**<br>
Después de definir la clase `Persona`, se crean tres instancias de la clase:
- `aitor`: Se crea una instancia de `Persona` con el nombre "Aitor Atxa" y el rol predeterminado de "asistente".
- `juan`: Se crea una instancia de `Persona` con el nombre "Juan" y el rol de "profesor".
- `maria`: Se crea una instancia de `Persona` con el nombre "Maria" y el rol de "clase".

```javascript
const aitor = new Persona({ nombre: "Aitor Atxa" });
// 'aitor' es una instancia de 'Instructor'
const juan = new Persona({ nombre: "Juan", rol: "profesor" });
const maria = new Persona({ nombre: "Maria", rol: "clase" });
```

**USO de los MÉTODOS**
Luego, se muestra cómo se pueden utilizar los métodos de la clase `Persona`:
- Se imprime la información de la instancia `aitor` en la consola.
- Se llama al método `Detalles()` de las instancias `aitor`, `juan` y `maria`, lo que imprime en la consola el nombre y el rol de cada persona.
- Se llama al método estático `holaMundo()` de la clase `Persona`, lo que imprime "Hola buenas!" en la consola.


```javascript
console.log(aitor);           // Persona { nombre: 'Aitor Atxa', rol: 'asistente' }
console.log(aitor.nombre);   // Aitor Atxa

// INSTANCE METHOD
aitor.Detalles(); // Aitor Atxa: asistente
juan.Detalles(); // Juan: profesor

// STATIC METHOD
Persona.holaMundo(); // Hola buenas!
```

En resumen, este código introduce los conceptos básicos de la programación orientada a objetos en JavaScript, como la definición de clases, la creación de instancias y el uso de métodos de instancia y métodos estáticos.


# Promesas en JavaScript

Una promesa o `Promise` es un objeto que representa la terminación o el fracaso de una operación asíncrona y su valor resultante. 

Esencialmente, una promesa es un objeto devuelto al cual se adjuntan funciones callback, en lugar de pasar callbacks a una función.

Principalmente, las promesas se usan mucho para trabajar con APIs. En estos casos, JavaScript permite trabajar de forma asíncrona con promesas; es decir, permite realizar la petición a la API y seguir realizando otras tareas, para, cuando se obtuviera la información de la misma, entonces trabajar con ella.

Para crear promesas, hayq eu utilizar la sintaxis `new Promise`, tal y como se verá en los ejemplos de más adelante.

**ESTADOS DE UNA PROMESA**

![alt text](promises.png)
Obtenido de https://lenguajejs.com/javascript/asincronia/promesas/


**- pending**:<br> este estado pendiente se da cuando no hemos obtenido respuesta a la solicitud hecha por la promesa. En nuestro ejemplo, es el momento entre que nos vamos a comprar las patatas y cuando volvemos a casa.

**- fulfilled**: <br>una promesa pasa del estado pending al fulfilled mediante el comando resolve. Este estado se da cuando hemos obtenido una respuesta satisfactoria a la solicitud. Es decir, cuando hemos vuelto a casa con patatas en la mano.

**- rejected**: <br>este estado se da, a través del comando reject, cuando obtenemos una respuesta negativa a la solicitud que ha hecho la promesa. En nuestro ejemplo, es cualquier respuesta en la que nuestra madre no obtenga patatas. Ten presente que debemos obtener una respuesta igualmente. Es decir, no volver a casa mantiene la promesa en pending, no en rejected. 

Inicialmente, una promesa tiene el estado pending, estado que tendrá hasta que la promesa haya resuelto un valor mediante resolve o haya ocurrido un error (reject). Cuando una promesa alcanza uno de estos dos estados, ya no puede realizar transiciones a otro.

Además, cada promesa tiene los siguientes métodos:

| **Métodos** | **Descripción** |
| ---- | ----- |
|.then(resolve) |	Ejecuta la función callback resolve cuando la promesa se cumple.
|.catch(reject) |	Ejecuta la función callback reject cuando la promesa se rechaza.
|.then(resolve,reject) 	| Método equivalente a las dos anteriores en el mismo .then().
|.finally(end) |	Ejecuta la función callback end tanto si se cumple como si se rechaza.

Se utilizan `then` y `catch`, donde `then` está mapeada a `resolve`, es decir, se ejecuta siempre que la respuesta es `resolve`, mientras que `catch` lo hará cuando se devuelva el `reject`.

De hecho, usando arrow functions se puede mejorar aún más la legibilidad de este código, recordando que cuando sólo tenemos una sentencia en el cuerpo de la arrow function hay un return implícito.

Vamos a simular una llamada a una API para entenderlo mejor:
```javascript
let saludos = new Promise((resolve, reject) => {
    // simular la petición correct a la API
    setTimeout(() => {
        // se ejecuta lo que contiene resolve si todo va bien
        resolve("Hola! Estas conectando correctamente a la API!");
    }, 300);

    // para simular una petición errónea a la API
    setTimeout(() => {
        reject(Error("Algo fue mal..."));
    }, 2000);
})


saludos
    .then((data) => {
        console.log(data);
    })
    .catch((err) => {
        console.error(err);
    });
```
**1. let saludos = new Promise((resolve, reject) => { ... });:**
	- new Promise crea un objeto Promise que representa una tarea asincrónica.
    - El constructor Promise recibe una función que se ejecutará cuando se crea el objeto. Esta función tiene dos parámetros: resolve y reject.
    - resolve es una función que se llama cuando la tarea se completa con éxito. Se utiliza para devolver el resultado exitoso de la tarea.
    - reject es una función que se llama cuando la tarea falla. Se utiliza para devolver el error que causó el fallo.

**2. setTimeout(() => { ... }, 300);:**
    - setTimeout es una función que ejecuta una función después de un período de tiempo especificado. En este caso, se ejecutará la función después de 300 milisegundos (0.3 segundos).

**3. resolve("Hola Estas conectando correctamente a la API!");:**
	- Cuando se ejecuta la función dentro de setTimeout, se llama a resolve con el mensaje "Hola Estas conectando correctamente a la API!" como parámetro. Esto indica que la tarea se ha completado con éxito.

**4. setTimeout(() => { ... }, 2000);:**
	- Otra función dentro de setTimeout se ejecutará después de 2000 milisegundos (2 segundos).

**5. reject(Error("Algo fue mal..."));:**
	- Cuando se ejecuta esta función, se llama a reject con un objeto Error que contiene el mensaje "Algo fue mal...". Esto indica que la tarea ha fallado.

**6. Uso de then y catch:**
	- Se utiliza then para manejar el resultado exitoso de la petición. Cuando la petición se completa correctamente, se llama a la función pasada como parámetro, que imprime el mensaje de bienvenida en la consola.
    - Se utiliza catch para manejar el resultado fallido de la petición. Cuando la petición falla, se llama a la función pasada como parámetro, que imprime el mensaje de error en la consola.


La petición exitosa se completa después de 0.3 segundos, mientras que la petición fallida se completa después de 2 segundos.<br>


**AGRUPACIÓN de PROMESAS**

Las promesas se pueden agrupar y tatarlas como un grupo de promesas. Esto es muy util cuando tenemos dos promesas que se ejecutan cada vez que un usuario hace login en una app.

En el siguiente ejemplo hay dos promesas, `saludos` y `actualizarCuenta` que seejecutan a la vez.

```javascript
const saludos = new Promise((resolve, reject) => {
    resolve("Hola!");
    reject("Algo ha ido mal, revisa tus credenciales...");
});

const actualizarCuenta = new Promise((resolve, reject) => {
    resolve("Actualizando cuenta...");
    reject("Error actualizando la cuenta, no hay conexion a Internet");
});
```
```javascript
const loginPromesas = Promise.all([saludos, actualizarCuenta]);
```
Se agrupan ambas promesas en una `login.Promesas`.
Y luego se llaman a las respuestas:
```javascript
loginPromesas.then(res => {
    console.log(res);       // [ 'Hola!', 'Actualizando cuenta...' ]

    res.forEach(activity => {     //usamos esta funcion para imprimir cada promesa
        console.log(activity);
    })
})

/* Imprime: 
Hola!
Actualizando cuenta...
*/
```

Además de ello, para trabajar con APIs, se utilizan una variedad de funciones, entre las uqe está `fetch`.
`Fetch`devuelve una promesa, por lo que nos podemos evitar el tener que escribir el `new Promise`. 
```javascript
console.log("Empezando una llamada");
const postPromise = fetch('https:api_a_la_que_queramos_llamar/')
```


# async y await en JavaScript

Async y await son dos palabras clave en JavaScript que permiten transformar código asíncrono para que parezca ser síncrono. Estas palabras clave son muy utilizadas en el contexto de código realizado con promesas. 


**Funcionamiento de Async y Await**

**- Async:** La palabra clave async se utiliza para definir una función asíncrona. Esto significa que la función siempre devuelve una promesa. Por ejemplo:
```javascript
const miFuncionAsincrona = async () => {
  // Código asíncrono
};
```

**- Await:** La palabra clave await se utiliza dentro de una función asíncrona para esperar a que una promesa se resuelva antes de continuar con la ejecución del código. Por ejemplo:

```javascript
const miFuncionAsincrona = async () => {
  const resultado = await miPromesa();
  // Continuar con el código después de que la promesa se haya resuelto
};
```

**Ventajas de Async y Await**
**1. Sintaxis más clara y fácil de leer:**<br> Async y await proporcionan una sintaxis más clara y fácil de leer que los callbacks o las promesas. En lugar de tener que encadenar una serie de callbacks o manejar una serie de promesas anidadas, async y await ofrecen una sintaxis más sencilla que se asemeja mucho al código sincrónico tradicional.
**2. Eficacia en la gestión de errores:**<br> Async y await permiten manejar errores de manera más fácil, ya que los errores se pueden capturar con un bloque try-catch dentro de la función asíncrona.
**3. Flexibilidad en la gestión de operaciones asíncronas:**<br> Async y await permiten esperar a que varias operaciones asíncronas se completen antes de continuar con el código, lo que es útil para manejar operaciones de E/S lentas o animaciones.


Basicamente, ASYNC-AWAIT permiten crear un flujo de trabajo, una especie de lista u orden que queramos seguir a la hora de ejecutar funciones asíncronas.

Para entenderlo mejor, se expone el siguiente ejemplo, en el que se simula una llamada a login() y una llamada a actualizarCuenta() tal y como hemos explicado en el ejemplo anteriormente, pero sin el uso de funciones flecha en este caso.

Primero de todo, hay que asegurarse de que el login se ha hecho correctamente y anteriormente que el actualizarCuenta, pero tal y como está el codigo ahora se ejecutará primero aquello que ocurra antes sin importar cual queramos que se ejecute primero. Para hacer que las cosas se ejecuten en el orden que queremos usamos `async-await`.

```javascript
const login = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Hola! Te has loggeado!")
        }, 2000);
    });
}

const actualizarCuenta = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Actualizando la cuenta...");
        }, 2000);
    });
}

async function loginProcess(){
    const returnedLogin = await login();

    /*esta función va a llamar al login(), con el 'await' le indicamos que no
    queremos que se ejecute nada más hasta que el login() haya terminado.*/
    
    console.log(returnedLogin);

    /*se esperan 2 segundos (los del setTimeout del login) y login() devuelve el
    string que le hemos dicho que devuelva*/ 

    const returnedactualizarCuenta = await actualizarCuenta();

    /* Llama y espera respuesta */
    
    console.log(returnedactualizarCuenta);
    
    /* Se imprime:
    Hola! Te has loggeado!
    Actualizando la cuenta...
    */
}

loginProcess()
```
