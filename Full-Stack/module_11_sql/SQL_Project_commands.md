
### De forma resumida, aquí están los comandos SQL para testear de forma rápida el Projecto SQL:


```sql

-- Crear base de datos

CREATE DATABASE universidad;

USE universidad;


-- Crear Tablas Estudiantes, Profesores, Asignaturas y Calificaciones y también las claves foráneas

CREATE TABLE Estudiantes (
    estudiante_ID INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE
);

CREATE TABLE Profesores (
    profesor_ID INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    departamento VARCHAR(50)
);

CREATE TABLE Asignaturas (
    asignatura_ID INT PRIMARY KEY,
    nombre VARCHAR(100),
    profesor_ID INT,
    FOREIGN KEY (profesor_ID) REFERENCES Profesores(profesor_ID)
);

CREATE TABLE Calificaciones (
    calificacion_ID INT PRIMARY KEY,
    estudiante_ID INT,
    asignatura_ID INT,
    nota DECIMAL(4,2),
    FOREIGN KEY (estudiante_ID) REFERENCES Estudiantes(estudiante_ID),
    FOREIGN KEY (asignatura_ID) REFERENCES Asignaturas(asignatura_ID)
);


-- Rellenear tablas con datos
INSERT INTO Estudiantes (estudiante_ID, nombre, apellido, fecha_nacimiento) VALUES
(1, 'Aitor', 'Garcia', '1991-05-15'),
(2, 'María', 'González', '1999-03-22'),
(3, 'Aritz', 'Mendieta', '1995-11-10'),
(4, 'Ana', 'Sánchez', '1987-07-08'),
(5, 'Luis', 'Landa', '1996-09-30');

INSERT INTO Profesores (profesor_ID, nombre, apellido, departamento) VALUES
(1, 'Iñaki', 'Urruchurtu', 'Fisiologia'),
(2, 'Oscar', 'Ecenarro', 'Física'),
(3, 'Nerea', 'Alonso', 'Química'),
(4, 'Aitor', 'Payros', 'Geologia'),
(5, 'Begoña', 'Jugo', 'Química');

INSERT INTO Asignaturas (asignatura_ID, nombre, profesor_ID) VALUES
(1, 'Fisiología Animal', 1),
(2, 'Física Cuántica', 2),
(3, 'Bioquímica Básica', 3),
(4, 'Bioquímica Avanzada', 3),
(5, 'Geología de Costas', 4),
(6, 'Geología de Valles', 4),
(7, 'Química Analítica', 5),
(8, 'Química Orgánica', 5);

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



-- Script para la nota media del profesor:

SELECT p.nombre, p.apellido, AVG(c.nota) as nota_media
FROM Profesores p
JOIN Asignaturas a ON p.profesor_ID = a.profesor_ID
JOIN Calificaciones c ON a.asignatura_ID = c.asignatura_ID
GROUP BY p.profesor_ID, p.nombre, p.apellido
ORDER BY nota_media DESC;


-- Script para las mejores notas de cada estudiante:

SELECT e.nombre, e.apellido, MAX(c.nota) AS MejorNota
FROM Estudiantes e
JOIN Calificaciones c ON e.estudiante_ID = c.estudiante_ID
GROUP BY e.estudiante_ID, e.nombre, e.apellido
ORDER BY MejorNota DESC;


-- Script para ordenar a los estudiantes por los cursos en los que están matriculados:

SELECT 
    e.nombre as nombre_estudiante, 
    e.apellido as apellido_estudiante,
    a.asignatura_ID,
    a.nombre as nombre_asignatura
FROM Estudiantes e
JOIN Calificaciones c ON e.estudiante_ID = c.estudiante_ID
JOIN Asignaturas a ON c.asignatura_ID = a.asignatura_ID
ORDER BY asignatura_ID;


-- Script para crear un informe resumido de los cursos y sus notas medias, ordenados desde el curso más difícil (curso con la nota media más baja) hasta el curso más fácil:

SELECT a.nombre as asignatura, AVG(c.nota) as nota_media
FROM Asignaturas a
JOIN Calificaciones c ON a.asignatura_ID = c.asignatura_ID
GROUP BY a.asignatura_ID, a.nombre
ORDER BY nota_media ASC;


-- Script para encontrar qué estudiante y profesor tienen más cursos en común:
 
SELECT e.nombre as estudiante, p.nombre as profesor, COUNT(DISTINCT a.asignatura_ID) as asignaturas_en_comun
FROM Estudiantes e
JOIN Calificaciones c ON e.estudiante_ID = c.estudiante_ID
JOIN Asignaturas a ON c.asignatura_ID = a.asignatura_ID
JOIN Profesores p ON a.profesor_ID = p.profesor_ID
GROUP BY e.estudiante_ID, p.profesor_ID
ORDER BY asignaturas_en_comun DESC
LIMIT 10;

```
