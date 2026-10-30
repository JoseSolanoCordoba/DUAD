# Tarea: Ejercicios de Normalización
**Estudiante:** [José Andrés Solano Córdoba]  
**Módulo:** Bases de Datos — Lyfter Learning  

---

### Normalización de Empleados y Proyectos

| Employee ID | Employee Name | Department | Department Phone | Project ID | Project Name | Project Budget |
|-------------|---------------|------------|------------------|------------|--------------|----------------|
| 201         | Ana Rivera    | IT         | 2222-2222        | P001       | Web App      | 50000          |
| 201         | Ana Rivera    | IT         | 2222-2222        | P002       | API REST     | 25000          |
| 202         | Luis Mendez   | Marketing  | 1111-1111        | P003       | Campaña TV   | 30000          |


***1FN***
Primero se nota que se incumple la 1FN por que el primary key no es único y los datos no son únicos, si se deseara tener una sola primary key 201 habría que meter
el project id 1 y 2 separado por comas o si no en columnas separadas project id 1 y project id 2 lo cual también incumple la 1FN. Por lo tanto hay que separar estos
datos de la tabla.

Quitando todo lo relacionado con los proyectos y usando un id que empieza en 1 la tabla quedaría así:

*Tabla Employees 1FN*
| id | Employee Name | Department | Department Phone |
|----|---------------|------------|------------------|
| 1  | Ana Rivera    | IT         | 2222-2222        |
| 2  | Luis Mendez   | Marketing  | 1111-1111        |

Y por otro lado a la tabla de proyectos le cambio el Project ID de P001, P002...a 1,2,3...y queda como sigue:

*Tabla Projects*
| id | Project Name | Project Budget |
|----|--------------|----------------|
| 1  | Web App      | 50000          |
| 2  | API REST     | 25000          |
| 3  | Campaña TV   | 30000          |

Ahora toca relacionar ambas tablas. Un empleado puede tener varios proyectos y varios empleados pueden trabajar en los mismos proyectos. Así que esto es una relación tipo N:N.
Se crea la tabla cruz para relacionar ambas tablas.

*Tabla Employee Project*
| id | employee_id | project_id |
|----|-------------|------------|
| 1  | 1           | 1          |
| 2  | 1           | 2          |
| 3  | 2           | 3          |

Así se cumple la 1FN.

***2FN***
En la tabla original existía una dependencia parcial creando una llave compuesta con las columnas employee id y project id. Por ejemplo si se quería hacer un request de un proyecto
en específico había que decir con el employee id 201, ajá y de cuál de los dos project id? El P001 o el P002? Al final había que dar 201 con P001, una combinación de ambas columnas.
Ese problema se eliminó al hacer que la tabla cumpla con la 1FN, al cumplir 1FN ya cumple con 2FN.

***3FN***
Para hacer cumplir la nueva tabla Employees 1FN con la 3FN se observa que los datos de Department primeramente no tiene lógica que vayan en la tabla de empleados pero, principalmente
basándonos en la 3FN se ve que los datos del departamento no dependen meramente del primary key lo que conduce además a una repetición descomunal de los mismos datos una y otra vez
en distintas filas. El department phone puede ser identicado por la columna department, y por el primay key.
Entonces se procede a separar dichos datos en otra tabla como sigue:

*Tabla Departments*
| id | Department | Department Phone |
|----|------------|------------------|
| 1  | IT         | 2222-2222        |
| 2  | Marketing  | 1111-1111        |

Ahora toca relacionar ambas tablas, un empleado va pertener solamente a un departamento pero, un departamento puede tener varios empleados, consequentemente es una relación N:1.
El N lo tiene la tabla de empleados, por lo tanto se coloca el foreign key en dicha tabla, lo cual además viene por lógica de que se debe asignar un departamento a un empleado.
Y la tabla queda así:

*Tabla Employees 3FN*
| id | Employee Name | Department_id |
|----|---------------|---------------|
| 1  | Ana Rivera    | 1             |
| 2  | Luis Mendez   | 2             |

Con lo que finalmente se llegó a la 3FN en el ejercicio.

### Normalización de Registro de Clases

| Student ID | Student Name | Course Code | Course Name | Instructor Name | Instructor Email |
|------------|--------------|-------------|-------------|-----------------|------------------|
| 301        | Marco Gómez  | CS101       | Python I    | Juan Pérez      | juan@uni.edu     |
| 301        | Marco Gómez  | CS102       | Python II   | Laura Rojas     | laura@uni.edu    |
| 302        | Carla Ruiz   | CS101       | Python I    | Juan Pérez      | juan@uni.edu     |

***1FN***
Se observa que no hay llave primaria única, hay distintos registros para una misma llave primaria. El problema radica en más de un curso por llave primaria, entonces a partir de
Course code se separa la tabla. Se crean dos: una para estudiantes y otra para los cursos. 

*Tabla Students*
| id | Student Name |
|----|--------------|
| 1  | Marco Gómez  |
| 2  | Carla Ruiz   |
Se cambió Studen ID por id, y que los números empiecen en 1 en vez de 301.

*Tabla Courses 1FN*
| id | Course Code | Course Name | Instructor Name | Instructor Email |
|----|-------------|-------------|-----------------|------------------|
| 1  | CS101       | Python I    | Juan Pérez      | juan@uni.edu     |
| 2  | CS102       | Python II   | Laura Rojas     | laura@uni.edu    |

Se añadió columna a la izquierda con id que empieza en 1.

Ahora hay que relacionar ambas tablas, un estudiante puede tener varios cursos, y un curso puede tener varios estudiantes, entonces es una relación de tipo N:N, se crea la tabla cruz
que los relaciona:

*Tabla Student Course*
| id | Student_id | Course_id |
|----|------------|-----------|
| 1  | 1          | 1         |
| 2  | 1          | 2         |
| 3  | 2          | 1         |

Con lo que ya se cumple la 1FN.

***2FN***
Se cumple con la 1FN por lo tanto ya se cumple con la 2FN, por qué? Porque existía una dependencia parcial entre Student ID y Course Code. Para acceder los datos del curso llevado
por un estudiante era necesario dar los dos IDs al mismo tiempo. Al separar dichos datos se eliminó esta dependencia.

***3FN***
La tabla Students y la tabla cruz Students Course cumplen, pero la tabla Courses 1FN no cumple. Esta tabla presenta datos que no dependen exclusivamente de la primary key.
Además de que su naturaleza no pertenece a la tabla Courses, y me refiero a los datos del instructor, que si no se maneja bien se pueden repetir indefinamente en muchas filas.\
Puede ocurrir que el mismo instructor de varios cursos. Separamos creando una tabla exclusivamente de Courses y otra de Instructors.

*Tabla Courses Only*
| id | Course Code | Course Name |
|----|-------------|-------------|
| 1  | CS101       | Python I    |
| 2  | CS102       | Python II   |

*Tabla Instructors*
| id | Instructor Name | Instructor Email |
|----|-----------------|------------------|
| 1  | Juan Pérez      | juan@uni.edu     |
| 2  | Laura Rojas     | laura@uni.edu    |

Ahora hace falta relacionarlas, se sabe que un curso va ser impartido (normalmente) por un solo instructor y cada instructor puede tener más de un curso. Por lo tanto es una
relación del tipo N:1 donde el N se encuentra en la tabla Courses Only. Por lo tanto se asigna el foreign key a dicha tabla, además de que por lógica hay que asignarle un
instructor a cada curso. La tabla queda así:

*Tabla Courses 3FN*
| id | Course Code | Course Name | Instructor_id |
|----|-------------|-------------|---------------|
| 1  | CS101       | Python I    | 1             |
| 2  | CS102       | Python II   | 2             |

Con lo que se logró llevar el ejercicio a 3FN.

### Normalización de Hospital y Citas Médicas

| Appointment ID | Patient Name | Patient Phone | Doctor Name | Specialty   | Date       | Time     |
|----------------|--------------|---------------|-------------|-------------|------------|----------|
| A01            | Diana Vargas | 8888-1111     | Dr. Soto    | Pediatría   | 2024-08-01 | 10:00 AM |
| A02            | Diana Vargas | 8888-1111     | Dr. Soto    | Pediatría   | 2024-08-10 | 10:00 AM |
| A03            | Edwin Mora   | 8999-2222     | Dr. Mora    | Cardiología | 2024-08-05 | 01:00 PM |

Se ve que hay datos que no dependen solamente de la primary key. Por ejemplo, se puede obtener el patient phone del primary key y del patient name.\
También ocurre con el specialty del doctor, se ve que depende del primary key pero principalmente depende de el doctor name.\
Ahora para evitar una redundancia extrema con los datos del paciente y del doctor en múltiples filas lo mejor es separar estos datos en otras tablas: una de pacientes
y otra de doctores.

*Tabla Patients*
| id | Patient Name | Patient Phone |
|----|--------------|---------------|
| 1  | Diana Vargas | 8888-1111     |
| 2  | Edwin Mora   | 8999-2222     |

*Tabla Doctors*
| id | Doctor Name | Specialty   |
|----|-------------|-------------|
| 1  | Dr. Soto    | Pediatría   |
| 2  | Dr. Mora    | Cardiología |

De esta manera se removieron las columnas que no dependen estrictamente del primary key. Y relacionando las nuevas tablas con la original, quedaría de la siguiente manera:

*Tabla Appointments*
| id | Patient_id | Doctor_id | Date       | Time     |
|----|------------|-----------|------------|----------|
| 1  | 1          | 1         | 2024-08-01 | 10:00 AM |
| 2  | 1          | 1         | 2024-08-10 | 10:00 AM |
| 3  | 2          | 2         | 2024-08-05 | 01:00 PM |

Así se cumple con la 3FN. El date y time se dejaron porque siempre han dependido estrictamente del primary key, es decir un appointment si o si va tener una fecha y una hora únicas.