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





















