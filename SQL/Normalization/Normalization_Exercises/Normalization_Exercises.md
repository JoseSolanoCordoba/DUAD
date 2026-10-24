# Tarea: Ejercicios de Normalización
**Estudiante:** [Tu Nombre]  
**Módulo:** Bases de Datos — Lyfter Learning  

---

## 1. Ejercicio Orders

### Tabla Original
![Ejercicio Orders: Tabla Original](https://github.com/JoseSolanoCordoba/DUAD/blob/835d156fad4a9e1a90751512bc8dce10b0f803e0/SQL/Normalization/Normalization_Exercises/assets/image_1.png)

### Proceso de Normalización

#### Paso 1: Primera Forma Normal (1FN)
* **Objetivo:** Asegurar un primary key único y que cada columna contenga valores únicos.
* **Creación de tabla Customers** 

* **Justificación / Análisis:** 

* **Resultado (Tablas 1FN):**
```markdown
| Order ID | Customer Name | Customer Phone | Address | Item ID | Item Name | Price | Quantity | Special Request | Delivery Time |
|----------|---------------|----------------|---------|---------|-----------|-------|----------|-----------------|---------------|
```

#### Paso 2: Segunda Forma Normal (2FN)
* **Objetivo:** Verificar que no existan dependencias parciales por llaves compuestas y qué se cumpla 2FN después de ya cumplirse 1FN.
* **Justificación / Análisis:** 
* **Tablas resultantes:**
  * **Tabla `Orders`** (Información general del pedido)
  * **Tabla `Order_Items`** (Detalle de los ítems del pedido)

#### Paso 3: Tercera Forma Normal (3FN)
* **Objetivo:** Cumplir con la 3FN y eliminar dependencias transitivas (atributos que dependen de otros atributos no clave).
* **Justificación / Análisis:** Separación de la información de los clientes y productos para evitar redundancias de datos (como el nombre del cliente, teléfono, dirección o precio del producto).
* **Tablas Finales:**
  * **`Customers`**
  * **`Orders`**
  * **`Items`**
  * **`Order_Items`** (Tabla intermedia N:N con su respectiva `Quantity`)

---

## 2. Ejercicio Cars

### Tabla Original
*(Aquí puedes incluir la tabla original o una breve descripción)*

### Proceso de Normalización

#### Paso 1: Primera Forma Normal (1FN)
* **Objetivo:** Valores atómicos y ausencia de grupos repetitivos.
* **Justificación / Análisis:**

#### Paso 2: Segunda Forma Normal (2FN)
* **Objetivo:** Eliminar dependencias parciales respecto a la clave principal (`VIN`).
* **Justificación / Análisis:**

#### Paso 3: Tercera Forma Normal (3FN)
* **Objetivo:** Eliminar dependencias transitivas (por ejemplo, los datos del propietario o de la aseguradora que dependen de un ID y no directamente del VIN del carro).
* **Tablas Finales:**
  * **`Cars`**
  * **`Owners`**
  * **`Insurance`**
  * **Tablas intermedias de relación** (si aplica, por ejemplo, para la relación de varios dueños por vehículo).

---
