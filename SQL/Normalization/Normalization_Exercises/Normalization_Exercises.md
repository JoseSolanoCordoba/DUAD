# Tarea: Ejercicios de Normalización
**Estudiante:** [José Andrés Solano Córdoba]  
**Módulo:** Bases de Datos — Lyfter Learning  

---

## 1. Ejercicio Orders

### Tabla Original
![Ejercicio Orders: Tabla Original](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/OriginalTable.png)

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

![Ejercicio Orders: Items Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/ItemsTable.png)

*En el caso de los customers se nota que hay algunos que tienen más de un address, por lo tanto otra vez se está repitiendo datos del mismo tipo en dichas filas incumpliendo la 1FN nuevamente, hay que eliminar esa 
*redundancia separando el address de los customer en otra tabla.

### Tabla Addresses

![Ejercicio Orders: Addresses Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/AdressesTable.png)

### Tabla Customers

*Ahora, vamos a crear la tabla Customers sin relacionar con sus respectivos addreses de momento:
![Ejercicio Orders: Customers Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/CustomersTable.png)

*Se podría pensar que como cada address tiene solo un dueño la solución sería añadir una columna foránea en la tabla Addresses que refenciara los Customers ID pero, puede ocurrir el
*caso en que más de una persona tenga la misma dirección entonces vemos que se trata de una relación N:N: 
*Una persona puede tener muchas direcciones, y una dirección puede pertenecer a más de un cliente. Por lo tanto se crea una tabla cruz Customer Address para relacionar a ambas tablas:

### Tabla Customer Address

![Ejercicio Orders: Customers Address Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/CustomerAddressTable.png)

*Ahora para evitar la redundancia de las ordenes se crea una tabla de Order nueva, que contenga cada primary key única y para esto se eliminan las columnas que evitarían tener solo una
*fila para cada Orden, por lo tanto:

### Tabla Orders

![Ejercicio Orders: Orders Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/OrdersTable.png)

*Antes de crear dicha tabla se analizó cuales elementos podría quedarse y el tipo de relación entre ellos. Por ejemplo las órdenes tienen una relación del tipo N:1 con los clientes, 
*una orden siempre va pertenecer solamente a un cliente pero, un cliente puede tener más de una orden. Entonces se colocó la Foreign Key donde está el N, o sea en la tabla Orders.
*Además el delivery time es propio y depende exclusivamente de la primary key (3FN) entonces de dejó.

*Continuando con  el análisis, la relación observada entre Orders y Items es N:N, una orden puede tener varios items y un item puede estar presente en varias ordenes. Entonces se creo
*la tabla cruz Order Item:

### Tabla Order Item

![Ejercicio Orders: Order Item Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/OrderItemTable.png)

*Se mantuvo la cantidad y el special request por ser únicos a cada item.

---

## 2. Ejercicio Cars

### Tabla Original
*(Aquí puedes incluir la tabla original o una breve descripción)*

### Proceso de Normalización
