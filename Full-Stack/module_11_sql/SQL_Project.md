# Proyecto - SQL


## Resumen del proyecto

Construye una base de datos SQL para una universidad que maneje `estudiantes`, `asignaturas`, `profesores` y `calificaciones`.


### Requisitos técnicos del proyecto

El proyecto debe contener las siguientes características técnicas:

* Construir una base de datos con las siguientes tablas: `Estudiantes`, `Asignaturas`, `Profesores`, `Calificaciones`.
* Claves foráneas para relacionar las tablas entre sí.
* Crear un script que rellene todas las tablas de la base de datos con datos de ejemplo.
* Crear scripts de consulta SQL para:
    * La nota media que da cada profesor.
    * Las mejores notas de cada estudiante.
    * Ordenar a los estudiantes por las asignaturas en las que están matriculados.
    * Crear un informe resumido de los cursos y sus notas medias, ordenados desde el curso más difícil (curso con la nota media más baja) hasta el curso más fácil.
    * Encontrar qué estudiante y profesor tienen más asignaturas en común.

---

## Solución al proyecto

Teniendo en cuenta en la descripción de la tarea/proyecto, a continuación muestro la forma en la que he creado la base de datos con tablas y qué scripts he creado para poder realizar las consultas.

Mencionar que pese a que se puede crear contenido manualmente mediante MySQL Workbench, utilizando sus características y herramientas, he optado por la opción de escribir todos los comandos. Sea mediatne MySQL Workbench o mediate comandos, he llegado al mismo resultado.


### Crea la base de datos con las tablas

Primero de todo creo una base de datos llamada `universidad`. 

```sql
CREATE DATABASE universidad;

USE universidad;
```
<br/>

### Crea las siguientes tablas:
<br/>

* Tabla `Estudiantes`:

```sql
CREATE TABLE Estudiantes (
    estudiante_ID INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE
);
```
| Nombre de columna | Tipo de dato   |
| ----------------- | -------------- | 
| `estudiante_ID`     | `INT`          |
| `nombre`   | `VARCHAR(50)`  | 
| `apellido`  | ` VARCHAR(50)` | 
| `fecha_nacimiento`  | `DATE` | 

<br/>
<br/>

* Tabla `Profesores`:

```sql
CREATE TABLE Profesores (
    profesor_ID INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    departamento VARCHAR(50)
);
```
| Nombre de columna  | Tipo de dato  | 
| ------------------ | ------------- | 
| `profesor_ID`      | `INT`         | 
| `nombre`           | `VARCHAR(50)` | 
| `apellido`         | `VARCHAR(50)` | 
| `departamento`     | `VARCHAR(50)` | 
<br/>
<br/>


* Tabla `Asignaturas`:

```sql
CREATE TABLE Asignaturas (
    asignatura_ID INT PRIMARY KEY,
    nombre VARCHAR(100),
    profesor_ID INT,
    FOREIGN KEY (profesor_ID) REFERENCES Profesores(profesor_ID)
);
```
| Nombre de columna | Tipo de dato  | Características                               |
| ----------------- | ------------- | --------------------------------------------- |
| `asignatura_ID`   | `INT`         | Primary Key, Not Null, Unique, Auto Increment |
| `nombre`          | `VARCHAR(80)` | Not Null                                      |
| `profesor_ID`     | `INT`         | Not Null                                      |

<br/>
<br/>

* Tabla `Calificaciones`:

```sql
CREATE TABLE Calificaciones (
    calificacion_ID INT PRIMARY KEY,
    estudiante_ID INT,
    asignatura_ID INT,
    nota DECIMAL(4,2),
    FOREIGN KEY (estudiante_ID) REFERENCES Estudiantes(estudiante_ID),
    FOREIGN KEY (asignatura_ID) REFERENCES Asignaturas(asignatura_ID)
);
```


| Nombre de columna      | Tipo de dato      | 
| ---------------------- | :----------------:| 
| `calificacion_ID`      | `INT`             | 
| `estudiante_ID`        | `INT`             | 
| `asignatura_ID`        | `INT`             | 
| `nota`                 | `DECIMAL(4, 2)`   | 


<br/>



### Claves foráneas para relacionar las tablas entre sí

Teniendo en cuenta las tablas creadas, las claves foránea a crear están distribuidas en las tablas `Asignaturas` y la tabla `Calificaciones`.

De tal modo que:

* `profesor_ID` de la tabla `Asignaturas` estará relacionada con `profesor_ID`  de la tabla `Profesores`. 

* `estudiante_ID` de la tabla `Calificaciones` estará relacionada con `estudiante_ID`  de la tabla `Asignaturas`. 

* `asignatura_ID` de la tabla `Calificaciones` estará relacionada con `asignatura_ID`  de la tabla `Asignaturas`. 


<br/>

### Script que rellene todas las tablas con datos de ejemplo

Mediante este script se rellenan datos de las tablas `Estudiantes`, `Profesores`, `Asignaturas`, `Calificaciones`.


```sql
-- Insertar datos en Estudiantes
INSERT INTO Estudiantes (estudiante_ID, nombre, apellido, fecha_nacimiento) VALUES
(1, 'Aitor', 'Garcia', '1991-05-15'),
(2, 'María', 'González', '1999-03-22'),
(3, 'Aritz', 'Mendieta', '1995-11-10'),
(4, 'Ana', 'Sánchez', '1987-07-08'),
(5, 'Luis', 'Landa', '1996-09-30');

-- Insertar datos en Profesores
INSERT INTO Profesores (profesor_ID, nombre, apellido, departamento) VALUES
(1, 'Iñaki', 'Urruchurtu', 'Fisiologia'),
(2, 'Oscar', 'Ecenarro', 'Física'),
(3, 'Nerea', 'Alonso', 'Química'),
(4, 'Aitor', 'Payros', 'Geologia'),
(5, 'Begoña', 'Jugo', 'Química');

-- Insertar datos en Asignaturas
INSERT INTO Asignaturas (asignatura_ID, nombre, profesor_ID) VALUES
(1, 'Fisiología Animal', 1),
(2, 'Física Cuántica', 2),
(3, 'Bioquímica Básica', 3),
(4, 'Bioquímica Avanzada', 3),
(5, 'Geología de Costas', 4),
(6, 'Geología de Valles', 4),
(7, 'Química Analítica', 5),
(8, 'Química Orgánica', 5);



-- Insertar datos en Calificaciones (Cada estudiante tiene 3 asignaturas)
INSERT INTO Calificaciones (calificacion_ID, estudiante_ID, asignatura_ID, nota) VALUES
(1, 1, 2, 5.6),
(2, 1, 3, 7.2),
(3, 1, 4, 7.4),

(4, 2, 2, 6.2),
(5, 2, 3, 8.4),
(6, 2, 4, 7.7),

(7, 3, 1, 8.5),
(8, 3, 7, 5.1),
(9, 3, 8, 6.2),

(10, 4, 1, 7.9),
(11, 4, 7, 6.9),
(12, 4, 8, 7.8),

(13, 5, 2, 6.4),
(14, 5, 5, 8.6),
(15, 5, 6, 9.7);

```

<br/>

### Scripts para realizar consultas SQL


1. **Para la nota media que da cada profesor:**

```sql
SELECT p.nombre, p.apellido, AVG(c.nota) as nota_media
FROM Profesores p
JOIN Asignaturas a ON p.profesor_ID = a.profesor_ID
JOIN Calificaciones c ON a.asignatura_ID = c.asignatura_ID
GROUP BY p.profesor_ID, p.nombre, p.apellido
ORDER BY nota_media DESC;

```

Al ser la primera consulta, se desglosa a continuación:

1. Primero de todo se seleciona el `nombre` y el `apellido` del profesor. Además, calcula el promedio (AVG) de las notas y lo nombra como `nota_media`.
2. Comienza con la tabla `Profesores` (alias `p`).
3. Une (JOIN) con la tabla `Asignaturas` (alias `a`) usando el `profesor_ID`.
4. Luego une con la tabla `Calificaciones` (alias `c`) usando el `asignatura_ID`.
5. Agrupa los resultados por `profesor_ID`, `nombre` y `apellido` del profesor. Esto permite calcular la nota media para cada profesor.
6. Ordena los resultados por la `nota_media` en orden descendente (DESC).Los profesores con las `nota_media` más altas aparecerán primero.


> Resultado:
>
> | nombre      | apellido    | nota_media |
> | ----------- | ----------- | ---------- |
> | Aitor       | Payros      |  9.150000  |
> | Iñaki       | Urruchurtu  |  8.200000  |
> | Nerea       | Alonso      |  7.675000  |
> | Begoña      | Jugo        |  6.500000  | 
> | Oscar       | Ecenarro    |  6.066667  |


<br/>

2. **Para las mejores notas de cada estudiante:**

```sql
SELECT e.nombre, e.apellido, MAX(c.nota) AS MejorNota
FROM Estudiantes e
JOIN Calificaciones c ON e.estudiante_ID = c.estudiante_ID
GROUP BY e.estudiante_ID, e.nombre, e.apellido
ORDER BY MejorNota DESC;
```

> Resultado:
>
> | nombre      | apellido     |  mejor_nota  |
> | ----------- | ------------ |  ----------  |
> | Luis	       | Landa	       |  9.70        |
> | Aritz	    | Mendieta     |  8.50        |
> | María    	 | González     |  8.40        |
> | Ana	       | Sánchez	    |  7.90        |
> | Aitor	    | Garcia       |  7.40        |

<br/>


3. **Para ordenar a los estudiantes por los cursos en los que están matriculados:**

```sql
SELECT 
    e.nombre as nombre_estudiante, 
    e.apellido as apellido_estudiante,
    a.asignatura_ID,
    a.nombre as nombre_asignatura
FROM Estudiantes e
JOIN Calificaciones c ON e.estudiante_ID = c.estudiante_ID
JOIN Asignaturas a ON c.asignatura_ID = a.asignatura_ID
ORDER BY asignatura_ID;

```
> Resultado:
>
> | nombre    | apellido   | asignatura_ID | nombre_asignatura   |
> | --------- | ---------- | --------------| -----------------   |
> | Aritz	  | Mendieta   |	1	          | Fisiología Animal   |
> | Ana	     | Sánchez    |	1	          | Fisiología Animal   |
> | Aitor     | Garcia     |	2	          | Física Cuántica     |
> | María     | González   |	2	          | Física Cuántica     |
> | Luis      | Landa      |	2	          | Física Cuántica     |
> | Aitor     | Garcia     |	3	          | Bioquímica Básica   |
> | María	  | González   |	3	          | Bioquímica Básica   |
> | Aitor	  | Garcia     |	4	          | Bioquímica Avanzada |
> | María	  | González   |	4	          | Bioquímica Avanzada |
> | Luis      | Landa      |	5	          | Geología de Costas  |
> | Luis      | Landa      |	6	          | Geología de Valles  |
> | Aritz     | Mendieta   |	7	          | Química Analítica   |
> | Ana       | Sánchez    |	7   	       | Química Analítica   |
> | Aritz     | Mendieta   |	8	          | Química Orgánica    |
> | Ana       | Sánchez    |	8	          | Química Orgánica    |

<br/>

4. **Para crear un informe resumido de los cursos y sus notas medias, ordenados desde el curso más difícil (*curso con la nota media más baja*) hasta el curso más fácil:**

```sql
SELECT a.nombre as asignatura, AVG(c.nota) as nota_media
FROM Asignaturas a
JOIN Calificaciones c ON a.asignatura_ID = c.asignatura_ID
GROUP BY a.asignatura_ID, a.nombre
ORDER BY nota_media ASC;
```

> Resultado:
>
> |     asignatura      |  nota_media  |
> | ------------------  |  ----------  |
> | Química Analítica   |  6.000000    |
> | Física Cuántica	   |  6.066667    |
> | Química Orgánica    |  7.000000    |
> | Bioquímica Avanzada	|  7.550000    |
> | Bioquímica Básica	|  7.800000    |
> | Fisiología Animal	|  8.200000    |
> | Geología de Costas	|  8.600000    |
> | Geología de Valles	|  9.700000    |
<br/>

5. **Encontrar qué estudiante y profesor tienen más cursos en común:**

```sql

SELECT e.nombre as estudiante, p.nombre as profesor, COUNT(DISTINCT a.asignatura_ID) as asignaturas_en_comun
FROM Estudiantes e
JOIN Calificaciones c ON e.estudiante_ID = c.estudiante_ID
JOIN Asignaturas a ON c.asignatura_ID = a.asignatura_ID
JOIN Profesores p ON a.profesor_ID = p.profesor_ID
GROUP BY e.estudiante_ID, p.profesor_ID
ORDER BY asignaturas_en_comun DESC
LIMIT 10;
```

> Este es el resultado:
>

> | estudiante | profesor | asignaturas_en_comun |
> | ---------- | -------- | -------------------- |
> | Aitor	   | Nerea	  | 2                    |
> | María	   | Nerea	  | 2                    |
> | Aritz	   | Begoña	  | 2                    |
> | Ana	       | Begoña	  | 2                    |
> | Luis	   | Aitor	  | 2                    |
> | Aitor	   | Oscar	  | 1                    |
> | María	   | Oscar	  | 1                    |
> | Aritz	   | Iñaki	  | 1                    |
> | Ana        | Iñaki	  | 1                    |
> | Luis	   | Oscar	  | 1                    |


<br/>

<hr/><hr/><br/>
