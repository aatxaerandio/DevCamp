# CheckPoint 16 

## Route Guards - Definición y usos

<p align="center">
  <img src="images/figure_11.png">
</p>

Cuando desarrollamos una aplicacion React, es necesario restringir a los usuarios no autenticados el acceso a ciertas partes de su aplicación. Es por ello, que el uso de los Route Guards o Rutas de Guardia son indispensables. Los Route Guards son interfaces que permiten controlar el acceso a las rutas en una aplicación, actuando de guardias que deciden si se permite o no la navegación a una ruta específica, basándose en ciertas condiciones.
Los Route Guards sirven para:<br/>
- **Control de acceso:** Permiten restringir el acceso a ciertas rutas basándose en condiciones como la autenticación del usuario o permisos específicos.
- **Prevención de pérdida de datos:** Pueden evitar que un usuario abandone una página con cambios no guardados.
- **Precarga de datos:** Facilitan la carga de datos necesarios antes de que se active una ruta.

Por las características de los Route Guards, son muy útiles en numerosos casos, asi como;<br/>
- **Verificación de roles:** Para permitir el acceso basado en roles o permisos específicos del usuario.
- **Carga de módulos:** Para controlar la carga de módulos basada en ciertas condiciones.
- **Formularios no guardados:** Para advertir al usuario antes de abandonar un formulario con cambios pendientes.
- **Protección de rutas privadas:** Para asegurar que solo usuarios autenticados accedan a ciertas áreas de la aplicación.


El uso de los Route Guards tiene una serie de **inconvenientes**, ya que requiere una complejidad adicional en la lógica de nacegacion, se pueden bloquar accidentalmente rutas legitimas si la lógica es incorecta, o incluso se puede tener un impacto en el rendimiento si no se implementan correctamente.<br/>

Pese a ello, el **no uso de los Route Guards conlleva muchos mas riesgos**, ya que no usarlos puede llevar a una perdida de datos, a vulnerabilidades de seguridad (Usuarios no autorizados podrían acceder a áreas restringidas de la aplicación), o a la expreience de usuario deficiente, en la que se ace la carga sin los datos necesarios, llevando a errores o pantallas en blanco.<br/>

### Para entender mejor su uso, se expone un ejemplo a continuación:

#### 1.  Primero, creamos un componente PrivateRoute que actuará como nuestro Route Guard:

```JSX
import { Navigate, Outlet } from 'react-router-dom';

const PrivateRoute = () => {
  const isAuthenticated = localStorage.getItem('token');
  
  return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRoute;
```
 Este componente verifica si el usuario está autenticado (en este caso, comprobando si existe un token en el `localStorage`). Si está autenticado, renderiza el componente hijo (`<Outlet />`), de lo contrario, redirige al usuario a la página de login. 

#### 2.  Luego, configuramos nuestras rutas utilizando el componente PrivateRoute: 
```JSX
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PrivateRoute from './PrivateRoute';
import Home from './Home';
import Dashboard from './Dashboard';
import Login from './Login';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route element={<PrivateRoute />}>
          <Route path="/dashboard" element={<Dashboard />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```
En este ejemplo, la ruta `/dashboard` está protegida por el `PrivateRoute`. Solo los usuarios autenticados podrán acceder a esta página


**En resumen, los Route Guards son una característica crucial en React para mejorar la seguridad, la integridad de los datos y la experiencia del usuario. Su uso adecuado puede prevenir problemas significativos, mientras que no utilizarlos puede exponer la aplicación a riesgos de seguridad y usabilidad.**

--- 

## Solicitud POST - Usos y funciones
Una solicitud POST es un método HTTP que permite enviar datos al servidor para que sean procesados. A diferencia de GET, los datos se envían en el cuerpo de la solicitud en lugar de en la URL, lo que proporciona mayor seguridad y capacidad de envío. 

### Para qué sirve
Las solicitudes POST se utilizan principalmente para: 
- Enviar datos de formularios al servidor.
- Cargar archivos al servidor.
- Actualizar información en una base de datos.
- Crear nuevos recursos en el servidor.
- Enviar datos sensibles de forma más segura.

### Cuándo utilizarlas
Es recomendable utilizar solicitudes POST en los siguientes casos: 
- Al enviar información confidencial (contraseñas, datos personales).
- Cuando se necesita enviar grandes cantidades de datos.
- Para crear o modificar recursos en el servidor.
- Al subir archivos.
- En general, cuando la acción implica un cambio en el estado del servidor.

### Riesgos de usar o NO usar
Algunos riesgos asociados al uso de POST incluyen el envío accidental de datos duplicados al recargar la página, la mayor complejidad en la implementación comparado con GET y los posibles problemas de seguridad si no se manejan adecuadamente los datos recibidos.

Pero por otro lado, **no usar POST cuando es apropiado** puede conllevar  a una exposición de datos sensibles en la URL si se usa GET, limitaciones en la cantidad de datos que se pueden enviar, problemas de seguridad al enviar información confidencial de forma visible, o dificultad para manejar operaciones que modifican el estado del servidor.

Una solicitud POST típicamente consta de:
```javasccipt
POST /submit-form HTTP/1.1

Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

username=john&password=secret
```
Desglosandolo:
```javascript
POST /submit-form HTTP/1.1
```

    POST: Este es el método HTTP que se está utilizando. POST se usa típicamente para enviar datos que serán procesados por el servidor.
    /submit-form: Esta es la ruta en el servidor a la que se está enviando la solicitud.
    HTTP/1.1: Esto indica la versión del protocolo HTTP que se está utilizando.

```javascript
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
```

    Host: Especifica el nombre de dominio del servidor (www.example.com).
    Content-Type: Indica el tipo de medio del recurso que se está enviando al servidor. En este caso, es "application/x-www-form-urlencoded", que se usa comúnmente para enviar datos de formularios HTML.
    Content-Length: Indica el tamaño del cuerpo de la solicitud en bytes (27 bytes en este caso).

```javascript
username=john&password=secret

```
Estos son los datos reales que se están enviando al servidor. Están formateados como pares clave-valor, separados por símbolos "&", que es el formato estándar para datos "application/x-www-form-urlencoded".

    username=john: El nombre de usuario que se está enviando es "john".
    password=secret: La contraseña que se está enviando es "secret".


En resumen, las solicitudes POST son fundamentales para el envío seguro y eficiente de datos al servidor, especialmente cuando se trata de información sensible o voluminosa. Su uso adecuado es crucial para mantener la seguridad y funcionalidad de las aplicaciones web modernas.

---

## Entrevista de trabajo - planificación y ejecucción

Para la preparación de una entrevista de trabajo, personalmente realizaría una serie de actividades/acciones con el fin de destacar como candidato y obtener el puesto.

<p align="center">
  <img src="images/figure_12.png">
</p>

1.	Primero de todo, haría una investigación exhaustiva de la empresa en la que voy a hacer la entrevista de trabajo. Primero analizaría bien su página web para ver apartados como “misión” o “valores” de la empresa, para ver por donde van sus afinidades y proyectos. Es importante saber a qué se dedican, que proyectos han realizado o que están realizando, al igual que tener una idea de las personas que hay dentro de esa empresa. A parte de eso, investigaría acerca de sus últimos productos, con que otras empresas han tenido relaciones/han trabajado, con el fin de estar al día con las actividades mas recientes. Además de ello, seria interesante saber que opiniones hay de otros trabajadores, que se pueden observar en webs como Glassdor o Indeed, para tener una idea del ambiente laboral, sueldo aprox, etc.

2.	Me prepararía una batería de preguntas posibles, así como: “Háblame de ti”, “Por qué consideras que eres un buen aspirante al trabajo”, “¿Qué puedes aportar a la empresa?”, etc. De este modo tendría una respuesta un poco “automática” para poder responder.

3.	Haría un simulacro de entrevista, bien en frente del espejo o que una segunda persona (amigo/familiar) me hiciese las preguntas. También me prepararía una posible transición al inglés, para poder continuar en inglés sin ningún problema.

4.	El día de la entrevista, me vestiría acorde al día y a la cultura de la empresa. Sobre todo, no llegaría tarde y seria tal y como soy, amable y cordial. Para gestionar el estrés o la ansiedad, y aunque parezca irrisorio, tengo la costumbre o manía de mascar chicle. Me ayuda a relajarme antes de la exposición, entrevista, etc., junto con haber dormido bien la noche anterior, ya que dormir suficiente es indispensable.

5.	Ya en la entrevista, intentaría estar lo más tranquilo posible, pero sin parecer una persona condescendiente, “pelota” o también “soso/pasivo”. Me enfocaría en mis fortalezas (bien comentando mis logros o habilidades, pero sin excederse), y también adoptaría una actitud de aprendizaje, ya que, de este modo, pese a no tener las competencias totales que buscan, demuestra tu interés por el puesto.

6.	Después de acabar, mandaría un correo de agradecimiento por la oportunidad y repitiendo mi interés por el puesto.
