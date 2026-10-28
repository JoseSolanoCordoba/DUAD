# Tarea: Ejercicios de Normalización
**Estudiante:** [José Andrés Solano Córdoba]  
**Módulo:** Bases de Datos — Lyfter Learning  

---

## 1. Ejercicio Orders

### Tabla Original
![Ejercicio Orders: Tabla Original](https://github.com/JoseSolanoCordoba/DUAD/blob/835d156fad4a9e1a90751512bc8dce10b0f803e0/SQL/Normalization/Normalization_Exercises/assets/OriginalTable.png)

### Proceso de Normalización

* **Creación de tabla Customers** 

* **Justificación / Análisis:** 
*1. Primeramente la tabla no tiene primary key única por lo tanto tiene filas con datos redundantes. Incumple la 1FN.
*2. La tabla presenta dependencias parciales (2FN), con llave compuesta por Order ID y Item ID. Ejemplo si se quiere consultar un registro en específico por decir el de Order ID 001 (pero hay dos 
*con ese Order ID) entonces, se escoge el de Order ID 001 con Item ID 101 por ejemplo, ahí se visualiza la dependencia entre ambas columnas que conforman esa llave compuesta. 
*3. Además se incumple la 3FN porque hay atributos que no dependen directamente de la primary key y pueden ser identificados por otra columna como es el caso de el Item Name que puede ser
*idenficado por la columna Item ID. Otro caso es con el customer name, phone y address que no dependen de la primary key sino más bien del cliente que haya hecho la orden.
*Por lo tanto se debe eliminar todo lo relacionado con los items y crear una tabla propia llamada Items.
*Así mismo eliminar todo lo relacionado al customer y crear una tabla propia llamada Customers.

### Tabla items

![Tabla Items](https://github.com/JoseSolanoCordoba/DUAD/blob/835d156fad4a9e1a90751512bc8dce10b0f803e0/SQL/Normalization/Normalization_Exercises/assets/ItemsTable.png)





---

## 2. Ejercicio Cars

### Tabla Original
*(Aquí puedes incluir la tabla original o una breve descripción)*

### Proceso de Normalización
