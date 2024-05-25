# Javascript y otros lenguajes de programación

JavaScript es un lenguaje de programación de alto nivel, interpretado y orientado a objetos. Se ejecuta en el lado del cliente, es decir, en el navegador web del usuario.

A diferencia de otros lenguajes, JavaScript se integra con HTML y CSS, lo que permite modificar y ajustar las funcionalidades de una página web de forma dinámica. 
JavaScript permite el desarrollo de aplicaciones modernas que interactúan directamente con los usuarios in necesidad de recargar la página constantemente y mejoran la experiencia del usuario. Entre los usos más simples pero más destacables de JavaScript están **los efectos visuales**, **la validación de formularios** o **cargar contenido de forma dinámica**.

En cuanto a las **características** más importantes de JavaScript destacan:
- **Simplicidad:** Posee una estructura sencilla que lo vuelve más fácil de aprender e implementar.
- **Velocidad:** Se ejecuta más rápido que otros lenguajes y favorece la detección de errores.
- **Versatilidad:** Es compatible con otros lenguajes como HTML, CSS, PHP o Java.
- **Popularidad:** Hay infinidad de recursos y foros disponibles para ayudar a la resolución de problemas.
- **Actualización:** Se actualiza de forma continúe con nuevos frameworks y librerías, asegurándole relevancia y continuidad en el sector.

Por otro lado, el uso de JavaScript es fundamental para otros muchos **proyectos** de mayor calado como por ejemplo:
- Desarrollo de páginas web del lado del cliente (front end).
- Desarrollo de aplicaciones para dispositivos móviles.
- Construcción de servidores web y aplicaciones de servidor.
- Desarrollo de aplicaciones de escritorio para sistemas de Windows, Linux y Mac.
- Desarrollo de juegos. 

A diferencia de Java, JavaScript es interpretado por el navegador en tiempo real, lo que facilita su integración con páginas web sin necesidad de compilación previa. 

# Tipos de datos de JavaScript

Entre otras, JavaScript funciona con declaración de variables, que básicamente son herramientas para almacenar datos.
<br>
Para declarar una variable en JavaScript se hace del siguiente modo:
```javascript
var nombre_variable = valor_variable

var edad = 30
```
Cuando se crea una variable con `var` se puede renombrar poniendo otro valor. Para evitar esto y que esa variable no pueda cambiar de valor, se utiliza `let` de tal modo:

```javascript
let edad = 30

```
Y de ese modo nos aseguramos que la variable `edad` nunca va a cambiar de valor.

Dicho esto, JavaScript es capaz de trabajar con una serie de datos, distintos entre ellos, que se utilizan para almacenar diferentes tipos de valores. Almacenar dichos valores en los diferentes tipos de datos permite hacer diferentes operaciones que se irán viendo más adelante. Entre los tipos de datos se encuentran:

**1. Booleans:** para valores booleanos, es decir, verdadero o falso.

```javascript
var veredicto = true
console.log(veredicto)      # true
```
**2. Null:** para valores nulos o vacíos.

```javascript
var valor = null;
console.log(valor);     // null
```

**3. Undefined:** para valores sin definir, como variables no inicializadas.

```javascript
var notDefined;
console.log(notDefined)  //undefined
```

**4. Number:** Para valores numéricos, ya sean enteros o decimales.

```javascript
var edad = 12;
console.log(edad)  // 12
```

**5. String:** Para valores de texto, como cadenas de texto o caracteres.

```javascript
var nombre = "Carmen";
console.log(nombre)     // Carmen
```

**6. Symbol:** Para valores únicos.

```javascript
var mySym = Symbol('foo');
console.log(mySym);    // Symbol(foo)
```

**7. Object:** para estructuras de datos más complejas. Por ejemplo, dentro de una variable podemos meter una lista de objetos.

```javascript
var usuario = {
    nombre: "Aitor",
    edad: 30,
    ciudad: {
        calle: "Mediavilla",
        numero: 12,
        codigo: 12345
    }
}

console.log(usuario.nombre)    // Aitor
console.log(usuario.ciudad.numero)    // 12
```

En este caso hemos metido una lista de objetos. Si queremos acceder a ellos, primero tendremos que acceder a la variable `usuario` y luego el objeto que queramos que nos devuelva. Si queremos que nos devuelva `nombre` se pondrá `usuario.nombre`. Por otro lado, si queremos acceder a `numero`, tendremos que acceder primero a `usuario`, luego a `ciudad`y mas tarde a `numero`.



# Funciones de String en JavaScript
En JavaScript, las funciones de cadena son fundamentales para trabajar con texto, facilitando la manipulación y representación de cadenas de manera eficiente en el desarrollo de aplicaciones web y programas JavaScript.

De este modo, podemos llamar a funciones para que hagan tareas así como buscar valores, encontrar los índices de carácteres, y mucho más. Aunque hay innumerables acciones que se pueden hacer con las funciones de string o cadenas en JavaScript, aquí **nos centraremos en las más importantes o las que más se usan.**

**1. Atributo Longitud** <br>
Este simplemente sirve para ver la longitud de la cadena.<br>
Para ello se utiliza `.length` detrás del nombre de la variable asignada.<br>
Por ejemplo:
```javascript
var str = "Este texto es una cadena"

console.log(str.length)   // 24
```
Esta cadena tiene una longitud de 24 caracteres. 


**2. Concatenar strings**<br>
Para poder concatenar dos o más cadenas. <br>
Se utiliza `.concat` antes de la variable asignada.<br>
En el ejemplo de a continuación, tenemos dos cadenas y queremos juntarlas:
```javascript
var str = "Este texto es una cadena"
var añadir = " y este texto es el que se añade"

var nueva_str = str.concat(añadir)

console.log(nueva_str)    // Este texto es una cadena y este texto es el que se añade
```
- Primero se crean las dos variables que contienen las cadenas que queremos concatenar.
- Creamos la variable final que será la concatenación de ambas variables.
- A la primera cadena `str`, se concatena la segunda cadena `añadir` y el resultado final cuando llamamos a `nueva_str` será `"Este texto es una cadena y este texto es el que se añade"`.

**3. Buscar cadenas en cadenas**<br>
Se utiliza para buscar cadenas o palabras clave en cierta cadena. <br>
Se utiliza `.includes("cadena a buscar")` detrás de la variable asignada.<br>
En el caso de que la cadena que queramos buscar se encuentre en la cadena, nos devolverá `true`, mientras que si no está, nos devolverá `false`.<br>
Por ejemplo:
```javascript
var str = "El gato marrón se encontraba perdido en el bosque"

console.log(str.includes("gato"))    // true
console.log(str.includes("perro"))  // false
```
En la cadena `str` queremos buscar "gato" y "perro".
Si buscamos "gato", nos devuelve `true`, lo cual significa que **SI** está presente.
Si por el contrario buscamos "perro", nos devuelve `false`, lo cual significa que **NO** está presente.



**4. Obtener carácteres en posiciones especificas**<br>

Se utiliza para obtener determinados caracteres en base al índice de ellos.<br>
Se utiliza `.chartAT(index)` detrás de la variable asignada.<br>
Por ejemplo:
```javascript
var str = "El gato marrón se encontraba perdido en el bosque"

console.log(str.charAt(3))    // g
```
De este modo obtenemos el caracter que se encuentra en el `index = 3`.

**5. Ver si hay cadenas que empiezan o acaban con palabras determinadas**

Mediante el uso de `startsWith("cadena/palabra clave")`y `endsWith("cadena/palabra clave")` se puede ver si la cadena empieza o acaba con cierta palabra especifica. Si se cumple, nos devolverá `true`, y si por el contario no se cumple nos devolverá `false`.
Por ejemplo:
```javascript
var str = "El gato marrón se encontraba perdido en el bosque"

console.log(str.startsWith("El gato"))     // true
```
De este modo, se imprime si la variable `str` empieza con `"El gato"`, y nos devuelve `true`. Lo cual, nos confirma que empieza por `"El gato"`.

En este otro ejemplo, queremos saber si la variable `str` acaba con `"arbol"`.
```javascript
console.log(str.endsWith("arbol"))    // false 
```
Nos devuelve `false`, lo cual se da por hecho que no acaba por `"arbol"`.

**6. Reemplazar una palabra por otra**

Se puede utilizar `replace("cadena_a_reemplazar", "cadena_nueva")`.<br>
```javascript
var str = "El gato marrón se encontraba perdido en el bosque"

console.log(str.replace("gato", "perro"))  // El perro marrón se encontraba perdido en el bosque
```
Aquí se reemplaza `gato`con `perro`. Y nos devuelve `"El perro marrón se encontraba perdido en el bosque"`.


**7. Buscar con `search`**
Se utiliza `.search("cadena")` antes de la variable para buscar el indice en el que se encuentra.<br>
Si se encuentra una coincidencia, se devuelve el índice de la primera aparición; de lo contrario, se devuelve -1.<br>

```javascript
var str = "El gato marrón se encontraba perdido en el bosque"

console.log(str.search("gato"))  // 3
console.log(str.search("arbol"))  // -1
console.log(str.search("marron")) // -1
```
En el primer caso, `"gato"`se encuentra en el indice 3, y por tanto nos devuelve `3`.
En el segundo caso, `"arbol"` no se encuentra, y por tanto nos devuelve `-1`.
En el tercer caso, `"marron"` no tiene tilde, y por tanto, no está, nos devuelve `-1`.


**8. Buscar indice de una cadena**
Se usa `indexOf("cadena_a_buscar")`o `lastIndexOf("cadena_a_buscar")`, para encontrar el índice de la cadena que se repite en la variable.
En el siguiente ejemplo, `gato`aparece dos veces, por lo tanto, para ver los indices de la primera vez que aparece `gato`se usará `indexOf("gato")`, mientras que si queremos ver el índice de la segunda vez que aparece `gato`, se usará `lastIndexOf("gato")`:
```javascript

var str = "El gato marrón se sentó. El gato marrón comió el pienso."

console.log(str.indexOf("gato"))  // 3

console.log(str.lastIndexOf("gato"))     // 28
```
De tal modo, que el índice del "primer" `gato`es `3`, mientras que el índice del "segundo" `gato` sería `28`.


**9. Extraer una sección de la cadena.**
En este caso, se usa `slice("índice_cadena")`para extraer una sección de la cadena que tenemos en la variable.
Por ejemplo:
```javascript
var str = "El gato marrón se sentó. El gato marrón comió el pienso."

console.log(str.slice(25))  // El gato marrón comió el pienso.

console.log(str.slice(-10)) // el pienso.

console.log(str.slice(15, -10))  // se sentó. El gato marrón comió 
```

En el primer caso, `slice(25)` extrae una subcadena a partir del índice 25 hasta el final de la cadena original. El índice 25 corresponde al carácter "E" de la palabra "El" en la segunda oración. Por tanto, nos devuelve `"El gato marrón comió el pienso."`

En el segundo caso, cuando se pasa un número negativo como argumento a `slice()`, se cuenta desde el final de la cadena hacia el principio. En este caso, `slice(-10)` extrae una subcadena de los últimos 10 caracteres de la cadena original, devolviendo `"el pienso."`

En el tercer caso, `slice(15, -10)` extrae una subcadena que comienza en el índice 15 y termina en el índice -10 (contando desde el final). El índice 15 corresponde al carácter "s" de la palabra "sentó". El índice -10 corresponde al carácter "c" de la palabra "comió". Por lo tanto, se devuelve `"se sentó. El gato marrón comió "`.

**10. Poner en mayúscula o minúscula una cadena.**

Para poner una cadena en mayúscula se usa `.toUpperCase()` delante de la variable asignada. Este método convierte todos los caracteres de la cadena a mayúsculas y devuelve una nueva cadena con el resultado.

Para hacer lo mismo pero en lugar de mayúsculas, en minúsculas, se usará `toLowerCase()`.

Por ejemplo:
```javascript
var str = "El gaTO marrón SE sentó."

console.log(str.toUpperCase())      // EL GATO MARRÓN SE SENTÓ.

console.log(str.toLowerCase())     // el gato marrón se sentó.
```
Se parte dela variable `str` que tiene mayúsculas y minúsculas de forma irregular. Para poder poner toda la cadena en mayúscula se aplica `str.toUpperCase()`, mientras que en el segundo caso se aplicar `str.toLowerCase()`. 

Así, en el primer caso nos devuelve `"EL GATO MARRÓN SE SENTÓ."`, mientras que en el segundo `"el gato marrón se sentó."`


# Condicionales en JavaScript

En JavaScript, un condicional es una estructura de control que permite ejecutar diferentes bloques de código dependiendo de si una **condición** es **verdadera** o **falsa**. Dependiendo de esto, permite tomar decisiones.

Se utilizan muy parecido a Python, mediante el uso de operadores y también el uso de `if-else`, entre otros.

Utilizando los operadores, podemos crear condicionales de:

1. Igualdad
```javascript
var edad = 12
var edad2 = `12`

if (edad == edad2) {
  console.log("Son el mismo número")
} else {
  condole.log("No son el mismo número")
}
```
En este caso, si las dos variables tienen el mismo valor, nos devolvería `"Son el mismo número"`

Pero cuidado! No son iguales, ya que si aplicamos "igual estricto":
```javascript
if (edad === edad2 ) {
  console.log("Son el mismo elemento")
} else {
  console.log("No son estrictamente iguales")
}
```
No devolvería "No son estricamente iguales, ya que son tipos diferentes de datos, uno es un `numero` y el otro es una `cadena`.



2. Des-igualdad
```javascript
var edad = 12
var edad2 = `12`

if (edad !== edad2) {
  console.log("No son iguales")
} else {
  condole.log("Son lo mismo")
}
```
Nos devolverá `"No son iguales"`.

3. Mayor o igual que
```javascript
var edad = 12

if (edad >= 20) {
  console.log("El valor es mas grande")
} else {
  console.log("El valor es mas pequeño")
}
```
Aquí se imprime el segundo condicional, ya que el primero es falso (no se cumple).

Otro ejemplo sería:

```javascript
var dinero = 1000

if (dinero > 550) {
  console.log("Tienes dinero para comprarte esta bicicleta.")
} else {
  console.log("Una pena, vas a tener que ahorra algo mas!")
}
```
En este ejemplo simple se crea un condicional en el que si tienes más de 550 (`dinero > 550`), **SI** se cumple el primer condicional y se imprime `"Tienes dinero para comprarte esta bicicleta."`. <br>
En el caso en el que el valor establecido en la variable `dinero` no sea superior a 550, **NO** se cumple el primer condicional y por tanto devuelve `"Una pena, vas a tener que ahorra algo mas!"`.


4. Menor o igual que
```javascript
var edad = 12

if (edad <= 20) {
  console.log("El valor es mas pequeño")
} else {
  console.log("El valor es mas grande")
}
```
En este caso, el primer condicional se cumple, ya que el valor que es 12, es mas pequeño que 20. Por tanto, se imprime `"El valor es mas pequeño"`."`

5. Operador lógico

Se pueden usar operadores lógicos, si una o ambas condiciones son verdaderas `true`, entonces se ejecutará el código dentro de la sentencia `if`.
```javascript
const pagar = true;
const voluntariado = false;

if (pagar || voluntariado) {
  console.log("Bienvenido! Esperemos que disfrute de la velada.");
} else {
  console.log("No has colaborado, no puedes asistir");
}
```
En este caso, si se cumple una condicion o la otra, es decir, si `pagar = true` o si `voluntariado = true`, se cumple y se imprime `"Bienvenido! Esperemos que disfrute de la velada."` Si las dos variables son `= false`, nos devolverá la otra cadena.

Para cambiar este funcionamiento, podriamos aplicar el signo de exclamación `!`. De este modo, el operador tomará alfo que es `true`y lo hará `false`, o viceversa, tomará algo que es `false` y lo hará `true`:
```javascript
const pagar = true;
const voluntariado = false;

if (!pagar || voluntariado) {
  console.log("Bienvenido! Esperemos que disfrute de la velada.");
} else {
  console.log("No has colaborado, no puedes asistir");
}
```
Para que se cumpla el condicional, SI se tiene que haber pagado Ó haber hecho voluntariado. Si el valor de `voluntariado`ya es `false`, solo nos queda que `pagar` fuera verdadero `true`. La variable está asignada a `true`, pero está precedido de un `!`, lo cual tomará `distinto de`, y será `falso`. Por tanto, se imprimirá `"No has colaborado, no puedes asistir"`.


6. Condiciones compuestas

Al igual que los condicionales en Python, también se pueden crear condicionales con 3 condiciones o múltiples, incluso condicionales dentro de condicionales.<br>

En el siguiente ejemplo se establecen 3 condiciones para la edad de un conductor. Se usa un condional compuesto en la segunda condición, ya que dentro de el, la `edad`tiene que ser mayor que 18, pero menor que 85.

```javascript
var edad_conductor = 50

if (edad_conductor < 18) {
  console.log("Lo sentimos, no puedes conducir")
} else if (edad_conductor > 18 && edad_conductor < 85) {
  console.log("Puedes conducir")
} else {
  console.log("Lo sentimos, no puedes conducir")
}

        // Puedes conducir
```
Aquí se emplea un condicional en el que dependiendo de la condición (edad del conductor), se le permite conducir o no.
- Si el primer condicional se cumple, se devuelve `Lo sentimos , no puedes conducir`.
- Si no se cumple el primer condicional se irá al siguiente. Si se cumple devolverá `Puedes conducir`.
- Si por el contrario no se cumple el segundo condicional, se cumplirá el tercero, devolviendo `Lo sentimos, no puedes conducir`. <br>

En este caso, se usan los operadores así como **menor que** `<` o **mayor que** `>`, entre otros. También se usa **`&&`** para meter dos operadores en un condicional, para que se cumpla el segundo condicional si la edad está entre 18 y 85.

En este ejemplo, si la variable `edad_conductor` es 50, se cumplirá el segundo condicional y por tanto se imprimirá `"Puedes conducir"`.
7. Condicionales anidados

Se pueden anidar condicionales unos en otros, tal que asi:
```javascript
var estado = "avion"

if (estado !== "Apagado") {
  console.log("El equipo esta encendido, ")
  if (estado == "Encendido") {
    console.log("y completamente operativo!")
  } else if (estado == "mantenimiento") {
    console.log(" pero se encuentra en modo mantenimiento")
  } else if (estado == "avion") {
    console.log("pero se encuentra en modo avion")
  } else {
    console.log("pero se está actulizando")
  }
} else {
  console.log("El equipo esta apagado")
}
```
Aquí se crear una variable `estado` para el estado de un equipo informatico. Se crea un condicional que sea para verificar si el equipo está encendido o apagado. Si la variable `estado` es diferente `!==`a `"Apagado"`, entonces se cumplirá el primer condicional y entrará a leer el resto de condicionales anidados. Del caso contrario, imprimiré `"El equipo esta apagado"`. 

Si se cumple la primera condición, se imprime `"El qeuipo esta encendido, "` y hay ahora 3 condiciones anidadas:
- Si el valor de la variable es `Encendido`, se cumple la primera condición e imprime `" y completamente operativo"`.
- Si el valor de la variable es `mantenimiento`, se cumple la segunda condición e imprime `" pero se encuenta en modo mantenimiento"`.
- Si el valor de la variable es `avion`, se cumple la tercera condicion e imprime `" pero se encuentra en modo avión"`.
- Si no cumple nimnguna de las anteriores condiciones automaticamente imprime `" pero se está actualizando"´.

Por tanto, y siguiendo el ejemplo, si la variable `estado` está asignada a `avion`, se cumpliria el primer condicional y el tercer condicional anidado, dando lugar a `"El equipo esta encendido, pero se encuentra en modo avion"`.

### SWITCH

En relación a los condionales, se puede usar también la declaración `switch`, que evalua una **expresión**, comparando el valor de esa expresión con una instance `case`, y ejecuta `declaraciones`asociadas a ese `case`, así como las declaraciones en los que `case`siguen.

Para entenderlo mejor, vamos a poner un ejemplo a continuación:
```javascript
const situacion = "baja";

switch (situacion) {
  case "alta":
    console.log("El trabajador se encuenta activo");
    break;
  case "baja":
    console.log("El trabajador se encuenta de baja");
    break;
  case "incapacidad":
    console.log("El trabajador tiene una incapacidad");
    break;
  case "fraude":
    console.log("El trabajador está cometiendo fraude");
    break;
  default:
    console.log("Se desconoce la situacion del trabajador");
    break;
}
```
Aquí, en lugar de usar condicionales multiples mediante el uso de `else if`, se pueden usar `case` y `break`para determinar el fin de la condición. Hay que tener en cuenta que para acabar, habria que poner un`default`que seria lo mismo a `else`en los condicionales al uso. De este modo se crea un condicional mas facil de escribir y de leer.

`Break`--> En el caso de que se nos olvide poner `break`, el script se ejecutará desde donde se cumple la condicion y ejecutara el siguiente `case`independientemente si esta condicion se cumple o no. Se ve en el siguiente ejemplo:

```javascript
var Animal = "Jirafa";

switch (Animal) {
  case "Vaca":
  case "Jirafa":
  case "Perro":
  case "Cerdo":
    console.log("Este animal subirá al Arca de Noé.");
    break;
  case "Dinosaurio":
  default:
    console.log("Este animal no lo hará.");
}
```
Aquí no hemos puesto break en ningun `case` hasta el que tiene el valor `Cerdo`. Al asignar el valor `Jirafa`, el script se ejecuta desde donde se cumple la condicon y ejecutará los siguientes `case` hasta cuando llega a `Cerdo`. Por tanto, se imprime `"Este animal subirá al Arca de Noé."`







# Operadores Ternarios

Se podría decir que un operador ternario es un atajo para la declaración `if...else`.<br>
Se utilizan principalmente ya que otros softwares igual no puedes leer adecuadamente los condicionales, y por tanto, se usa este método.<br><br>
Los operadores ternarios evalúan la condición y devuelven un valor u otro dependiendo si la condición es verdadera o falda.

La sintaxis de los operadores ternarios simples son de este modo:

`condición ? valorSiVerdadero : valorSiFalso;`

En el que se crea una `condición`, y le sigue un signo de interrogación `?` y se escriben los valores después. **El primer valor se imprimirá si el condicional se cumple, mientras que se imprimirá el segundo valor si es falso.**

Para el uso de operadores ternarios se suelen incorporar en `funciones`. Dentro de la función se designa una variable que contiene el operador ternario y se le añade un `console.log` para imprimir el valor final de esa variable.

Para entender mejor su uso, se expone primero un condicional al uso y luego el mismo condicional pero en operador ternario:

````javascript
function acceso(edad) {
  if (edad >= 18) {
    console.log("Puedes comprar tabaco")
  } else {
    console.log("NO puedes comprar tabaco")
  }
}

acceso(18)    // Puedes comprar tabaco
````
Este seria un condicional al uso, en el que pasamos un valor que es `18``  a la función `acceso`. Si es superior igual a 18 se cumple el condicional y se imprime `"Puede comprar tabaco"`.<br>
Si por el contrario pasamos otro valor que sea menos que 18, se cumpliría el segundo condicional e imprimiría `"NO puedes comprar tabaco"`.

Si utilizásemos **operadores ternarios**, seria del siguiente modo:
```javascript
function acceso(edad) {
  let respuesta = edad >= 18 ? 'Puedes comprar tabaco' : 'NO puedes comprar tabaco';
  console.log(respuesta)
}

acceso(18)      // Puedes comprar tabaco
```
Mediante este operador ternario llegaríamos al mismo resultado. En el que pasamos el valor 18 a la función que contiene la variable y el operador ternario. De este modo, como se cumple el condicional se imprime el primer valor, que es `"Puedes comprar tabaco"`.

Además de ello, los operadores ternarios se pueden usar para **condicionales compuestos**, tal y como el que se expone a continuación:

```javascript

function accessServer(name){
  if (name) {
    console.log("Welcome to the server");
    if (name.admin) {
      console.log("you are an admin");
    } else {
      console.log("you are NOT an admin");
    }  
  } else {
    console.log("Access denied")
  }
}

  let usuario_1 = {
    name : 'Pedro',
    admin : true
  }  
  accessServer(usuario_1)
  
  let usuario_2 = {
    name : "Juan",
    admin : false
  }  
  accessServer(usuario_2)
```


**En este ejemplo se crea un condicional de acceso a un servidor.** 
- Por una parte se crea la función `accessServer` a la que le pasamos un valor, en este caso `name`.
- Esta función tiene por un lado un condicional que es si existe usuario. Si NO se cumple, imprimirá `"Access denied"`. Si por el contrario, se cumple el primer condicional se imprime `"Wellcome to the server`.

- Pero no acaba aqui, el primer condicional tiene otros dos condicionales dentro de él. Nos dice que si el valor de `name.admin` existe, es decir, si `name.admin == true` entonces se imprimirá `"you are an admin"`.
- Por el contrario, si `name.admin` no es ==true, imprimirá `"you are NOT an admin"`.

- Para pasar valores a la función, tendríamos que crear variables que tengan objetos, así como `usuario_1`, que tiene el valor `"Pedro"` para `name`y `"true"` para `admin`.
  - Si pasamos `usuario_1` por la función, por una parte cumplirá el primer condicional y luego dentro del primero, cumplirá de nuevo el primer condicional, lo que imprimirá `"Wellcome to the server you are an admin"`.
  - En el caso del segundo, `usuario_2`, se cumpliría el primer condicional y dentro del mismo no se cumpliría, lo cual imprimiría `"Wellcome to the server you are NOT an admin"`.

Utilizando operadores ternarios, sería de la siguiente manera:

```javascript
function accessServer(name) {
  let respuesta = name 
    ? (name.admin ? 'Welcome to the server, you are an admin' : 'Welcome to the server, you are NOT an admin')
    : 'Access denied';
  console.log(respuesta)
}

accessServer(usuario_1)

```
- Dentro de la función, establecemos una variable que se llame `respuesta` que será igual al operador ternario.
- El primer condicional es `name` que significa "¿existe `name`?".
- Si **NO** se cumple, automáticamente se imprime lo último del operadores, `"Access denied"`.
- En el caso de que se cumple, va a por el siguiente condicional que es `name.admin` que significa "¿tiene valor `admin` en ese `name`?".
  - En el caso que se cumpla se imprime el primer valor del operador `"Welcome to the server, you are an admin"`.
  - Mientras que si **NO** se cumple se imprimirá el segundo valor del operador `"Welcome to the server, you are NOT an admin"`.






# Diferencias entre una declaración de función y una expresión de función

Pese a que las declaraciones de función y las expresiones de función puedan llegar a dar el mismo resultado, o utilizadas para el mismo fin, hay una serie de diferencias significativas entre ellas. Estas diferencias a su vez son responsables de su utilidad en diferentes contextos.

En cuando a la sintaxis, **la declaración de función** se define usando la palabra clave `function` seguida del nombre de la función, parámetro y cuerpo. Estas se procesan antes de que se ejecute cualquier otro código.
```javascript
function sumar(a, b) {
  return a+ b;
}
```

Una **expresión de función** se define asignando una función anónima a una variable usando la palabra clave `function` seguida de parámetros y cuerpo, pero **SIN nombre de función**.
```javascript
let sum = function(a, b) {
  return a + b;
}
```

A parte de las diferencias de sintaxis entre unas y otras, otras diferencias clave son:

|              | Declaraciones de función | Expresiones de función |
| ---------- | --------- | ------- |
| **Comportamiento** | Hoisting  | Se ponen al principio del ámbito, lo cual hace que se pueden llamar antes de que se declaren | Solo se pueden usar después de que se asignen. |
| **Nomenclatura** | Requieren de un nombre de función | Pueden ser anónimas |
| **Ejecución**   | Se ejecutan antes de cualquier código | Se cargan y se ejecutan solo cuando el intérprete del programa llega a la línea de código |
| **Almacenamiento** | No requieren de una asignación de variable | Se pueden almacenar en asignaciones de baribales |
| **Condicionales** | No pueden ser condiciones | Si pueden ser condicionales |
| **Facilidad de uso** | Son mas legibles y fáciles de entender | Pueden dar lugar a mas confusión debido a su mayor dificultad | 
| **Versatilidad** | Flexibles y legibles | versátiles y permiten usos más avanzados |

**En resumen**, las declaraciones de función se procesan antes de la ejecución del código y se pueden llamar en cualquier lugar, mientras que las expresiones de función se evalúan como parte de un flujo de ejecución y solo se pueden llamar desudes de que se asignen a una variable.

Poniendo un ejemplo se pretende explicar su utilidad. Podemos crear un condicional y meter dentro expresiones de funciones, ya que no es recomendable poner declaración de funciones dentro de bloques de código en condicionales.

Vamos a crear un menú para los comensales dependiendo de la edad de ellos:
```javascript
var edad = 14;


if (edad <= 10) {
  var crearMenu = function () {
    return "Menú para niños";
  };
  
  console.log(crearMenu());

  } else if (edad > 10 && edad < 18) {
    var crearMenu = function () {
      return "Menú para adolescentes";
    }
  console.log(crearMenu())
  } else {
    var crearMenu = function () {
      return "Menú para adultos";
    }
    console.log(crearMenu())
  }
```

Se declara la variable `edad` y un condicional con tres condiciones:
- Si la edad es menor de 10.
- Si la edad está entre 10 y 18.
- Si la edad es superior a 18.<br>
En cada bloque de código se crea una expresión de función, es decir, se crea una variable `crearMenu` igual a una función anónima. En caso de que se cumpla esa condición se imprimirá lo que está puesto para que nos devuelva esa expresión de función.<br>
Si por ejemplo la variable `edad` es 14, se cumplirá el primer condicional y nos devolverá "Menu para niños".

# Palabra clave "this" - función y usos

La palabra clave `this` es una palabra muy especial en JavaScript, y se refiere a un objeto o contexto dentro de la función que se está ejecutando.

**Esta palabra es crucial para acceder y manipular valores de objetos y comportamientos en funciones y métodos de JavaScript, dando un mayor dinamismo para interactuar con objetos en base al contexto de su invocación.**

Los principales **funciones** de `this` son:

**1. Dentro de un método:**
```javascript
var persona = {
  nombre: 'Juan',
  edad: 30,
  saludo() {
      console.log('Hola, mi nombre es ' + this.nombre + ' y tengo ' + this.edad + ' años.');
  }
};
persona.saludo();      // Hola, mi nombre es Juan y tengo 30 años.
```
En este caso, se llama a la función `saludo` que se encuentra dentro de la variable `persona`. Aquí la palabra `this` hace referencia a `persona` y sería equivalente a poner `persona.nombre` y `persona.edad`. De ese modo se accede a los valores de `nombre`y `edad` mediante `this`.

**2. Por si sola la palabra `this`:** <br>
Se refiere al objeto global:
```javascript
function saludo() {
  console.log('Hola, mi nombre es ' + this.nombre);
}

var persona = { 
  nombre: 'Juan', 
  diHola: saludo };

console.log(persona.diHola());      // Hola, mi nombre es Juan
```

Dentro de la función `saludo`, `this` se refiere al objeto global porque la función no es llamada como un método de un objeto. Cuando se llama `persona.saludo()`, está buscando una propiedad llamada `saludo` en el objeto de persona, el cual no existe. Por ello, hay que llamar a la propiedad `diHola` que contiene la función `saludo`.

Un ejemplo práctico sería ver cuantas entradas quedan por vender para ver un partido de futbol:
```javascript
var entradas = {
  entradas: 100,
  entradasVendidas: 78,
  entradasRestantes: function() {
    return (this.entradas - this.entradasVendidas)
  },
  entradaSobrantes: function() {
    if (this.entradasRestantes() > 0) {
      return (this.entradasRestantes())
    } else {
      return ("No hay entradas")
    }
  }
}
```

Primero se crea el objeto `entradas` que tiene 4 propiedades; `entradas`, `entradasVendidas`, `entradasRestantes` y `entradasSobrantes`. Las dos últimos son métodos (funciones) dentro del objeto.

Creamos el método `entradasRestantes`que calcula el número de entradas restantes, restando `entradasVendidas` a `entradas`. Aquí se utiliza la palabra clave `this` para poder acceder a las propiedades del objeto actual.

Después se crea el método `entradaSobrantes`que primero verifica si hay entradas restantes llamando al método `entradasRestantes()`. Si el resultado es mayor que 0, devuelve el número de entradas restantes. De lo contrario, devuelve el string `"No hay entradas"`. 

Podemos acceder a las propiedades y métodos del objeto `entradas` de la siguiente manera:
```javascript
console.log(entradas.entradaSobrantes())          // 22
console.log(entradas.entradas);                   // 100
console.log(entradas.entradasVendidas);           // 78
console.log(entradas.entradasRestantes());        // 22
```
En la que vemos cuántas entradas sobrantes hay (22), cuántas entradas totales hay (100) y cuántas entradas se han vendido (78).
