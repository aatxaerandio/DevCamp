# CheckPoint 12

## 1 ¿Qué significa UML?
UML es el acrónimo de Unified Modeling Language, o Lenguaje de Modelado Unificado. UML es un lenguaje estándar que proporciona un conjunto de diagramas y anotaciones gráficas que permites representar diferentes aspectos de un sistema.

UML se creó en 1995 por Grady Booch, Ivar Jacobson y James Rumbaugh, como un lenguaje de modelado claro para que los desarrolladores lo usen, para entender de forma fácil y sencilla los procesos y el diseño de software. 
Para los desarrolladores de software es imprescindible tener una visión general del sistema, teniendo en cuenta las jerarquías y relaciones dentro de un sistema, al igual que las dependencias entre estos. Es por ello, que UML ayuda a visualizar, construir y documentar nuevos sistemas de software y planos. 

Entre los diferentes diagramas UML se encuentran los diagramas estructurales, que se usan para modelar la forma de cómo se diseña un sistema, y los diagramas de comportamiento, que se ocupan de cómo se comporta el sistema. Ambos tipos de sistemas se especificarán más adelante.

## 2. ¿Por qué usamos UML?
EL uso de un modelo UML divide los sistemas en componentes y subcomponentes, facilitando la visualización, planificación y ejecución del proyecto. 
Entre otras, el uso de UML tiene numerosas ventajas, entre otras:

**-	Documentación y comprensión del sistema:** UML permite documentar y presentar de manera precisa y estructurada, el diseño, la arquitectura y requisitos del sistema, ayudando a comprender mejor el comportamiento del sistema, el análisis y la toma de decisiones durante el proceso de desarrollo.

**-	Diseño y planificación:** permite modelar y visualizar diferentes perspectivas del sistema, ayudando a identificar y resolver problemas de diseño antes de la implementación.

**-	Comunicación efectiva:** Es un lenguaje estandarizado, lo que supone que es un lenguaje visual común muy representativo, que permite a diferentes miembros del equipo de desarrollo (diseñadores, programadores, etv), comunicarse de manera efectiva sobre los diferentes aspectos del sistema.

**-	Explorar diferentes alternativas u opciones:** el uso de UML puede ayudar a visualizar nuevas ramas de desarrollo, corregir o mejorar algunas descritas, con el fin de ver que versión o que componente funciona mejor, etc.

## 3. Nombra algunos diagramas estructurales.
En cuanto a los diagramas estructurales, se distinguen 3 tipos:

**-	Diagramas de clase (Class Diagrams):** Son los diagramas mas comunes, y se utilizan para modelar la estructura de un sistema, incluyendo sus clases, atributos, métodos y relaciones entre ellos. Sus componentes son Nombre, Atributos y Operaciones.

**-	Diagramas de implantación/despliegue (Deployment Diagrams):** Nos dan la habilidad de modelar cómo debería configurarse una arquitectura de un sistema por completo. Es muy útil para tener una visión general de cómo conectan los diferentes componentes de un sistema. Sus componentes son Nodos, Componentes, Artefactos, Links, Dependencias y Asociaciones.

**-	Diagramas de paquetes (Package Diagrams):** Permiten agrupar elementos de tal forma que se pueda visualizar de forma sencilla las dependencias entre los elementos y las relaciones que existen entre ellos. Sus componentes son Tipo, Clasificador, Clase, Caso de uso, Componente, Paquete, Restricción, Dependencia y Evento.

## 4. Nombra algunos diagramas de comportamiento.
En cuanto a los diagramas estructurales, se distinguen 4 tipos:

**-	Diagramas de actividad (Activity Diagrams):** Muestran el flujo de control o de objetos con énfasis en la secuencia y las condiciones del flujo, proporcionando la posibilidad de fraccionar en parte mas pequeñas y manejables. Se pueden usar como boceto inicial para tener una idea de cómo continuar con el desarrollo de un sistema. Sus componentes son “Estado Inicial”, “Estado de Actividad”, “Flujo de Acción”, “Estado de Decisión”, “Condiciones” y “Estado Final”.

**-	Diagramas de casos de uso (Use Case Diagrams):** nos visualizan las distintas operaciones que puede realizar cada perfil de usuario, y uno de los más importantes y que nos visualizan el resultado de todo lo que hemos querido realizar anteriormente. Este tipo de diagramas te permite mostrar todo aquello a lo que un usuario tiene acceso. Por ello, son muy útiles en aquellos casos en los que se quiera diseñar el sistema de autorización. Sus componentes son Actores, Subsistemas, Relaciones y Casos de uso.

**-	Diagramas de máquinas de estado (StateMachine Diagrams):** Sirven para mostrar cómo se ven los datos y las acciones de los mismos en diferentes estados a lo largo del ciclo de vida del sistema. Sus componentes son Punto de Entrada, Elección, Restricción, Estado y Transición.

**-	Diagramas secuenciales (Sequence Diagrams):** Es uno de esos diagramas que más gustan a los desarrolladores. Esto se debe a que cuanto más desarrollas, más comienzas a pensar en tu sistema como una especie de enviar y recibir mensajes, incluso de forma interna. Este tipo de diagramas es uno de los diagramas más complejos, muestra exactamente cómo debe implementarse el código. Sus componentes son “Roles de clase o participantes”, “Ocurrencias de activación o ejecución”, “Mensajes” y “Líneas de vida”.



## 5. ¿Qué es el enrutamiento RESTful?
El enrutamiento RESTful es un componente fundamental en el diseño de APIs REST que define cómo se mapean las solicitudes HTTP a los recursos y acciones correspondientes en el servidor.
El enrutamiento RESTful permite una estructura clara y coherente en la API, facilitando la comprensión y el mantenimiento del código.

Las rutas o URL se diseñan de manera significativa y semántica para representar los recursos y las operaciones que se pueden realizar sobre ellos. Cada ruta se asocia con un verbo HTTP (como GET, POST, PUT o DELETE) que indica la acción que se desea realizar.
Los métodos HTTP se asocian a acciones específicas sobre los recursos: 

**•	GET:** :arrow_right: Obtener recursos.

**•	POST:** :arrow_right: Crear nuevos recursos.

**•	PUT/PATCH:**  :arrow_right: Actualizar recursos existentes.

**•	DELETE:** :arrow_right: Eliminar recursos.

Por ejemplo, se puede utilizar el proceso de un post (tweet) en Twitter para definir las rutas RESTful.

-	GET :arrow_right: Ver varios tweets.
  
-	POST :arrow_right: Crear un nuevo tweet.
  
-	PUT :arrow_right: Reemplazar un tweet existente.
  
-	PATCH :arrow_right: Editar o hacer un cambio en un tweet, pero no reemplazarlo como con PUT.
  
-	DELETE :arrow_right: Eliminar un tweet.

