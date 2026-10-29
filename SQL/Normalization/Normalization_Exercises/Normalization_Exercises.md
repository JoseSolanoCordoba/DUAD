# Tarea: Ejercicios de Normalización
**Estudiante:** [José Andrés Solano Córdoba]  
**Módulo:** Bases de Datos — Lyfter Learning  

---

## 1. Ejercicio Orders

### Tabla Original
![Ejercicio Orders: Tabla Original](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/OriginalTable.png)

### Proceso de Normalización

* **Justificación / Análisis:** 
1. Primeramente la tabla no tiene primary key única por lo tanto tiene filas con datos redundantes. Incumple la 1FN\
2. La tabla presenta dependencias parciales (2FN), con llave compuesta por Order ID y Item ID. Ejemplo si se quiere consultar un registro en específico por decir el de Order ID 001 (pero hay dos 
con ese Order ID) entonces, se escoge el de Order ID 001 con Item ID 101 por ejemplo, ahí se visualiza la dependencia entre ambas columnas que conforman esa llave compuesta.\ 
3. Además se incumple la 3FN porque hay atributos que no dependen directamente de la primary key y pueden ser identificados por otra columna como es el caso de el Item Name que puede ser
idenficado por la columna Item ID. Otro caso es con el customer name, phone y address que no dependen de la primary key sino más bien del cliente que haya hecho la orden.
Por lo tanto se debe eliminar todo lo relacionado con los items y crear una tabla propia llamada Items.
Así mismo eliminar todo lo relacionado al customer y crear una tabla propia llamada Customers.

### Tabla items

![Ejercicio Orders: Items Table](https://github.com/JoseSolanoCordoba/DUAD/blob/91817119f2a1df170567cfab8e2816144f9100ea/SQL/Normalization/Normalization_Exercises/assets/ItemsTable.png)

### Tabla Customers

Ahora, vamos a crear la tabla Customers sin relacionar con sus respectivos addreses de momento:
![Ejercicio Orders: Customers Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/CustomersTable.png)


Ahora para evitar la redundancia de las ordenes se crea una tabla de Order nueva, que contenga cada primary key única y para esto se eliminan las columnas que evitarían tener solo una
fila para cada Orden, por lo tanto:

### Tabla Orders

![Ejercicio Orders: Orders Table](https://github.com/JoseSolanoCordoba/DUAD/blob/50dd807c890a6d61c943f49b7d32351f80fd3352/SQL/Normalization/Normalization_Exercises/assets/OrdersTable.png)

Antes de crear dicha tabla se analizó cuales elementos podría quedarse y el tipo de relación entre ellos. Por ejemplo las órdenes tienen una relación del tipo N:1 con los clientes, 
una orden siempre va pertenecer solamente a un cliente pero, un cliente puede tener más de una orden. Entonces se colocó la Foreign Key donde está el N, o sea en la tabla Orders.
Además el delivery time es propio y depende exclusivamente de la primary key (3FN) entonces de dejó así como la dirección de entrega única para cada order.

Continuando con  el análisis, la relación observada entre Orders y Items es N:N, una orden puede tener varios items y un item puede estar presente en varias ordenes. Entonces se creo
la tabla cruz Order Item:

### Tabla Order Item

![Ejercicio Orders: Order Item Table](https://github.com/JoseSolanoCordoba/DUAD/blob/8826303853cd753048193b904e7941aa3e296caa/SQL/Normalization/Normalization_Exercises/assets/OrderItemTable.png)

Se mantuvo la cantidad y el special request por ser únicos a cada item.

---

## 2. Ejercicio Cars

### Tabla Original
![Ejercicio Cars: Original Cars Table](https://github.com/JoseSolanoCordoba/DUAD/blob/18f631dd0e6221b9196af27bc072d7001d252847/SQL/Normalization/Normalization_Exercises/assets/CarsOriginalTable.png)

### Proceso de Normalización

* **Justificación / Análisis:** 
Analizando la tabla original se ve tenemos filas con información repetida, por ejemplo el número de VIN repetido, podría considerarse una falta para la 1FN. Además se observa una 
falta hacia la 2FN por una dependencia compuesta entre el VIN y el owner ID. Además de que los datos del owner no pertenecen a dicha tabla y no dependen únicamente del primary key 
por lo que es una violación a la 3FN.
Lo mismo sucede con la compañía de seguros, no son datos que pertenecen a la tabla como tal y no dependen del primary key estrictamente. Por lo tanto se procede a separar dichos datos
tanto de los owners como de las compañías.\

Se crea una tabla Owners, y otra tabla Companies:

### Tabla owners

![Ejercicio Cars: Owners Table](https://github.com/JoseSolanoCordoba/DUAD/blob/18f631dd0e6221b9196af27bc072d7001d252847/SQL/Normalization/Normalization_Exercises/assets/OwnersTable.png)

### Tabla Companies

![Ejercicio Cars: Companies Table](https://github.com/JoseSolanoCordoba/DUAD/blob/50dd807c890a6d61c943f49b7d32351f80fd3352/SQL/Normalization/Normalization_Exercises/assets/CompaniesTable.png)


Se observa falta a la 3FN, porque el modelo por sí solo puede identificar la marca, un CR-V siempre va ser Honda, quiere decir que la marca puede ser idenficada por el VIN y por el modelo,
lo que quiere decir que no depende única y exclusivamente del VIN como primary key natural(se asignara un id más adelante). Entonces se procede a separar las marcas en otra tabla Models que tenga
todas las características pertenecientes al carro.

### Tabla Models

![Ejercicio Cars: Models Table](https://github.com/JoseSolanoCordoba/DUAD/blob/50dd807c890a6d61c943f49b7d32351f80fd3352/SQL/Normalization/Normalization_Exercises/assets/ModelsTable.png)

Ahora, es bien sabido que un vehículo puede tener más de un dueño, esto sería una relación 1:N pero, una persona podría también tener más de un vehículo, entonces se crea la tabla cruz
N:N Owner Car:

### Tabla Owner Car

![Ejercicio Cars: Owner Car Table](https://github.com/JoseSolanoCordoba/DUAD/blob/18f631dd0e6221b9196af27bc072d7001d252847/SQL/Normalization/Normalization_Exercises/assets/OwnerCarTable.png)

El insurance policy aplica al carro específicamente, y además puede aplicar a más de un vehículo. Para evitar repetición de registros se crea la tabla cruz Car Insurance. Un 
vehículo puede tener más de una póliza y una póliza la puede tener más de un vehículo.

### Tabla Car Insurance Policy
![Ejercicio Cars: Car Policy Table](https://github.com/JoseSolanoCordoba/DUAD/blob/50dd807c890a6d61c943f49b7d32351f80fd3352/SQL/Normalization/Normalization_Exercises/assets/CarInsuranceTable.png)

Ahora es necesario aclarar la relación entre las compañías y sus pólizas. Se sabe que todas las compañías pueden tener todas las pólizas, entonces se hace la tabla cruz que identifica
la póliza en combinación con su compañía como un registro independiente N:N irrepetible.

### Tabla Insurance Compamies and Policies
![Ejercicio Cars: Companies Policies Table](https://github.com/JoseSolanoCordoba/DUAD/blob/6b18bb922602978151f92a3461404c0074df8c2f/SQL/Normalization/Normalization_Exercises/assets/CompaniesInsurancesTable.png)

Tanto esta tabla como las tablas Car Insurance Policy se pueden extender hasta cumplir todas las combinaciones existentes. En este caso se ejemplifica solamente el escenario actual
pero son N:N.


Finalmente se tiene la tabla Cars nueva:

### Tabla Cars Nueva
![Ejercicio Cars: Cars Table](https://github.com/JoseSolanoCordoba/DUAD/blob/50dd807c890a6d61c943f49b7d32351f80fd3352/SQL/Normalization/Normalization_Exercises/assets/CarsTable.png)

Esta tabla tiene solamente información única, referenciando el brand_id previamente mencionado y el resto de características únicas. Mientras que los owners y las compañías de seguro,
ya se relacionan con las tablas cruz creadas.
