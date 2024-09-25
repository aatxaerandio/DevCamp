# CheckPoint 14

Primero de todo, tenemos que definir que es npm, que es Node Package Manager, un administrador de paquetes de JavaScript que gestiona las dependencias en proyectos escritos en Node.js.
Con este administrador, puede administrar la instalación, actualización y eliminación de paquetes (bibliotecas). En términos generales, npm es el registro de software más grande del mundo.
npm tiene 3 componentes principales:
1-	Sitio web:
o	Desde el sitio web se pueden encontrar paquetes, configurar y administrar otros aspectos.
2-	Interfaz de línea de comando (Command Line Interface):
o	Se ejecuta en la terminal a través de la cual los desarrolladores interactúan con npm.
3-	Resgistro:
o	Es una gran base de datos publuca con software JavaScript e información que lo acompaña.
Una de las acciones mas comunes y sencillas de ejecutar en npm, es instalar un módulo de Node. Para ello se requiere que se ejecute en la terminal el siguiente comando:
npm install <nombre-del-modulo>
También se puede abreviar como:
npm i <nombre-del-modulo>
Ambos comandos descargan e instalan el moduclo especificado en el proyecto en el que se esté trabajando. A partir de la ejecución de este comando, se crará un directorio llamada node_mocules en el directorio actual y se descsargaré en él la versión mas reciente del paquete.
En resumen, el uso de npm tiene numerosos beneficios, asi como:
-	Es facil de instalar
-	Facil gestión de dependencias.
-	Tiene una gran cantidad de paquetes disponibles
-	Tiene un control de versiones, pudiendo usar diferentes versiones dependiendo de las compatibilidades del sistema o con otros modulos.
-	Tiene soporte en línea de comando, automatizando la instalación y gestión.


## Tipos de componentes de reacción
En React, los dos tipos principales de componentes son los componentes de clase y los componentes funcionales. Su uso es diferente, al igual que su sintaxis, y aunque su uso pueda ser el mismo en ciertas ocasiones, ambos tienen ventajas frente al otro método: 

|Componentes DE CLASE | Componentes funcionales |
|------|-----|
|Se definen como clases de JavaScript que extienden de React.Component.|Funciones de JavaScript que reciben props como argumento|
|Tienen un método render() que devuelve el JSX a renderizar.|Retornan directamente el JSX a renderizar|
|Pueden tener estado interno y acceder al ciclo de vida de React.|No tienen estado interno ni acceso a métodos del ciclo de vida (originalmente)|
|Permiten implementar lógica más compleja.|Son más simples y concisos|

### Componentes de clase VS componentes funcionales
Cada tipo tiene sus ventajas, pero en general los componentes funcionales son preferidos por su simplicidad y mejor rendimiento. Los componentes de clase siguen siendo útiles en ciertos casos más complejos.
Los componentes funcionales son la forma más moderna y recomendada de crear componentes en React, especialmente desde la introducción de los Hooks, que les permiten manejar estado y efectos secundarios.
### Ventajas de los componentes funcionales
#### 1. Simplicidad y legibilidad
Los componentes funcionales son más concisos y fáciles de leer que los componentes de clase. Requieren menos líneas de código y tienen una estructura más simple. 
#### 2. Hooks
Con la introducción de los hooks, los componentes funcionales pueden manejar estado y efectos secundarios, igualando la funcionalidad de los componentes de clase. Esto eliminó la principal ventaja que tenían los componentes de clase. 
#### 3. Rendimiento
Los componentes funcionales tienden a tener un mejor rendimiento, ya que evitan el overhead de las clases en JavaScript. 
Tendencias de programación funcional
El uso de componentes funcionales se alinea mejor con las tendencias actuales hacia la programación funcional en el desarrollo frontend.
#### 4. Facilidad de testing
Generalmente es más sencillo realizar pruebas unitarias en componentes funcionales. 
#### 5. Curva de aprendizaje
Los componentes funcionales son más fáciles de aprender y entender, especialmente para desarrolladores nuevos en React. 

En conclusión, para nuevos desarrollos y componentes, se recomienda utilizar componentes funcionales con hooks. Sin embargo, es valioso entender ambos enfoques, ya que es probable encontrar componentes de clase en proyectos existentes o en ciertas situaciones específicas.


## Uso de accesorios en React

Los accesorios (props) en React son una parte fundamental del diseño de componentes. Las `props` (abreviatura de "properties") se utilizan en React para pasar datos de un componente padre a un componente hijo. Son inmutables y ayudan a mantener el flujo de datos unidireccional.

La principal razón para usar `props` es pasar datos de un componente padre a un componente hijo. Esto permite crear componentes reutilizables que pueden recibir diferentes datos y comportarse de manera distinta según los props que reciban.

Por ejemplo, 

```JSX
function Saludo(props) {
  return <h1>¡Hola, {props.nombre}!</h1>;
}
```

Este es un componente funcional llamado `Saludo`. Los componentes en React son bloques de construcción reutilizables para la interfaz de usuario. 
- La función recibe un parámetro props, que es un objeto que contiene todas las propiedades pasadas al componente.
- Dentro del componente, se accede a la propiedad nombre del objeto props usando props.nombre.
- El componente retorna un elemento JSX, que es una sintaxis similar a HTML utilizada en React.

```JSX
function App() {
  return <Saludo nombre="Mundo" />;
}
```

Este es otro componente funcional llamado `App`. 
- Dentro de App, se renderiza el componente `Saludo`.
- Se le pasa una `prop` llamada nombre con el valor `"Mundo"`.

### Funcionamiento
1.	Cuando se renderiza App, este crea una instancia del componente Saludo.
2.	La prop nombre="Mundo" se pasa al componente Saludo.
3.	Dentro de Saludo, props.nombre se evalúa como "Mundo".
4.	El componente Saludo renderiza un elemento h1 con el texto "¡Hola, Mundo!".

### Resultado
Al renderizar App, se mostrará en la página: 
```XML
<h1>¡Hola, Mundo!</h1>
```
Este ejemplo demuestra cómo los componentes en React pueden ser reutilizables y cómo se pueden pasar datos de un componente padre a un componente hijo mediante props. Es una forma eficiente de construir interfaces de usuario modulares y dinámicas.
Aquí, el componente Saludo recibe el prop nombre y lo utiliza para renderizar un saludo personalizado.

### Entre los beneficios de usar props destacan:

**Creación de componentes reutilizables**
Los props permiten crear componentes más flexibles y reutilizables. En lugar de codificar valores fijos, podemos pasar diferentes datos a través de props, lo que hace que nuestros componentes sean más versátiles. 
**Comunicación unidireccional**
React sigue un flujo de datos unidireccional, donde la información fluye de componentes padres a hijos. Los props son el mecanismo principal para implementar este flujo de datos, lo que hace que las aplicaciones sean más predecibles y fáciles de depurar. 
**Rendimiento y optimización**
React puede optimizar el rendimiento comparando los valores de los props para determinar si un componente necesita volver a renderizarse.

En resumen, los props son esenciales en React para crear componentes flexibles, reutilizables y mantenibles. Permiten la comunicación entre componentes, facilitan la separación de responsabilidades y son fundamentales para el flujo de datos unidireccional de React.


## JSX - JavaScript XML
JSX (JavaScript XML) es una extensión sintáctica para JavaScript que permite a los desarrolladores escribir código similar al HTML dentro de archivos JavaScript. Fue desarrollada por Meta (antes Facebook) y se utiliza principalmente en el marco de trabajo React para definir interfaces de usuario. 

### Usos principales de JSX
JSX se usa principalmente para: 
1.	Crear componentes de interfaz de usuario en React
2.	Combinar lógica JavaScript y marcado HTML en un solo archivo
3.	Describir la estructura visual de componentes de forma declarativa

### Beneficios de usar JSX
JSX ofrece varias ventajas importantes, entre las que destacan las siguientes:
#### Sintaxis intuitiva:
Permite escribir código similar a HTML dentro de JavaScript, lo que resulta familiar y fácil de leer para muchos desarrolladores. Ademas, permite usar expresiones JavaScript directamente, facilitando la creación de interfaces dinámicas.
#### Mejora la eficiencia:
Facilita la creación de componentes reutilizables, ahorrando tiempo y esfuerzo en proyectos de gran escala.
#### Optimización del rendimiento:
JSX se compila a JavaScript optimizado antes de ejecutarse en el navegador, mejorando el rendimiento.
#### Detección de errores:
Ayuda a detectar errores de sintaxis durante la compilación, lo que facilita la depuración.
#### Funcionamiento de JSX
JSX se transforma en JavaScript estándar antes de ejecutarse en el navegador. Esta transformación la realiza un transpilador, siendo Babel el más popular. Por ejemplo: 

```JSX
const element = <h1>Hello, world!</h1>;
```

Se convierte en: 

```javascript
const element = React.createElement("h1", null, "Hello, world!");
```

En resumen, JSX simplifica el proceso de desarrollo de interfaces de usuario complejas y dinámicas, especialmente en el contexto de React, mejorando la legibilidad del código y la eficiencia del desarrollo.




## Estado (state) en React

El estado (state) en React es un objeto que contiene datos relevantes para un componente y que pueden cambiar a lo largo del tiempo, afectando la representación del componente en pantalla. 
Entre los principales datos que maneja React se encuentran los state, junto con las props. Este objeto contiene datos internos que un componente puede manejar y modificar, y se utiliza para almacenar datos que cambian con el tiempo dentro de un componente. De este modo, se crea dinamismo e interactividad en las aplicaciones React.

A diferencia que los props que son inmutables, state es mutable, y pertenece y se define dentro del propio componente, no se pasa desde componentes padres.
En cuanto a su funcionamiento, cuado el estado cambia, el componente se vuelve a renderizar automáticamente con la nueva información. Se puede definir usando el hook useState en componentes funcionales o la propiedad state en componentes de clase, y se actualiza utilizando el método setState (en clases) o la función actualizadora devuelta por useState (en funciones).

En resumen, el uso de state aporta una serie de beneficios, asi como: 
•	Manejo de datos dinámicos
•	Actualización eficiente de la interfaz de usuario
•	Encapsulación de la lógica del componente
A continuación se pondrá un ejemplo para que se entienda mejor:

```JSX
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
```
Esta línea define una nueva clase llamada Counter que extiende React.Component. Esto significa que Counter es un componente de React.
Este es el constructor de la clase. Hace dos cosas importantes: 
1.	Llama a super(props) para invocar el constructor de la clase padre (React.Component).
2.	Inicializa el estado del componente con un objeto que tiene una propiedad count establecida en 0.

```JSX
  render() {
    return (
      <div>
        <p>Has hecho clic {this.state.count} veces</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Haz clic
        </button>
      </div>
    );
  }
}
```
Este es el método render(), que define lo que el componente debe mostrar: 
•	Retorna un div que contiene un párrafo <p> y un botón <button>.
•	El párrafo muestra el número actual de clics, accediendo a this.state.count.
•	El botón tiene un manejador de eventos onClick que, cuando se hace clic, llama a this.setState() para incrementar count en 1.
Funcionamiento general:
1.	Cuando el componente se monta, muestra "Has hecho clic 0 veces" y un botón que dice "Haz clic".
2.	Cada vez que se hace clic en el botón, el estado se actualiza incrementando count en 1.
3.	React re-renderiza el componente después de cada actualización del estado, mostrando el nuevo recuento de clics.


En resumen, el estado es fundamental en React para manejar datos dinámicos dentro de los componentes y crear interfaces de usuario interactivas y reactivas a los cambios.



## Constructor en React


El constructor se utiliza en los componentes de clase en React. Es el lugar adecuado para inicializar el estado y enlazar métodos. 
en breves palabras, el constructor se usa para: 
•	Inicializar el estado
•	Enlazar métodos de clase
•	Recibir props iniciales


Para entenderlo mejor, se expone un ejemplo a continuación:

```javascript
class MiComponente extends React.Component {
  constructor(props) {
    super(props);
    this.state = { contador: 0 };
    this.incrementar = this.incrementar.bind(this);
  }

  incrementar() {
    this.setState(prevState => ({
      contador: prevState.contador + 1
    }));
  }

  render() {
    return (
      <div>
        <p>Contador: {this.state.contador}</p>
        <button onClick={this.incrementar}>Incrementar</button>
      </div>
    );
  }
}

```

 Este código define un componente de React llamado MiComponente que implementa un contador simple. Desgosandolo en diferentes partes:
 ```javascript
class MiComponente extends React.Component {
```
Se define una clase llamada MiComponente que extiende React.Component. Esto significa que MiComponente es un componente de React y puede utilizar todas las características de los componentes de React.

 ```javascript
constructor(props) {
  super(props);
  this.state = { contador: 0 };
  this.incrementar = this.incrementar.bind(this);
}
```
- Constructor: Se utiliza para inicializar el estado del componente y enlazar métodos.
- super(props): Llama al constructor de la clase base (React.Component) para asegurarse de que el componente se inicialice correctamente.
- this.state: Se establece el estado inicial del componente. Aquí, el estado tiene una propiedad llamada contador, que se inicializa en 0.
- this.incrementar = this.incrementar.bind(this): Esto enlaza el método incrementar al contexto actual de la clase, asegurando que this dentro de incrementar se refiera a la instancia del componente.


 ```javascript
incrementar() {
  this.setState(prevState => ({
    contador: prevState.contador + 1
  }));
}
```
- Este método se encarga de incrementar el valor del contador.
- this.setState: Es un método de React que permite actualizar el estado del componente. Aquí, se utiliza una función que recibe el estado anterior (prevState) y retorna un nuevo objeto de estado.
- contador: prevState.contador + 1: Incrementa el valor actual del contador en 1.

```javascript
render() {
  return (
    <div>
      <p>Contador: {this.state.contador}</p>
      <button onClick={this.incrementar}>Incrementar</button>
    </div>
  );
}
```
- Método render: Es obligatorio en todos los componentes de clase y es responsable de describir lo que se debe renderizar en la interfaz de usuario.
Dentro del método render, se retorna un elemento JSX:

- Un <div> que contiene:
  - Un párrafo (<p>) que muestra el valor actual del contador.
  - Un botón (<button>) que, al hacer clic, llama al método incrementar.

Funcionamiento General
1. Al montar el componente, el contador se inicializa en 0.
2. Cada vez que el usuario hace clic en el botón "Incrementar", se llama al método incrementar.
3. El método incrementar actualiza el estado del componente, incrementando el valor del contador en 1.
4. La interfaz se vuelve a renderizar automáticamente para reflejar el nuevo valor del contador.





