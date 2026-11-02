# Tarea: Ejercicios de Normalización
**Estudiante:** [José Andrés Solano Córdoba]  
**Módulo:** Bases de datos — Lyfter Learning  

---

### 1. Explicación cruzada entre conjuntos y SQL

***All - Odd***\
Esta operación devuelve Even que es todo lo que no encuentra en Odd.

*En SQL*
Sería una tabla mayor que contenga la tabla Odd menor. 
Es requerido hacer un LEFT JOIN en este caso pero eliminando la intersección entre ambas ya que el LEFT JOIN me devuelve la
intersección + lo que no se encuentra en la tabla de la derecha (tabla Odd).
Para esto se hace algo como:\

SELECT Even.number\
FROM ALL\
LEFT JOIN Odd\
ON ALL.id = Odd.all_id\
WHERE Odd.all_id IS NULL\

Un LEFT JOIN normal pero apuntando solamente a los elementos que no esten relacionados entre ambas tablas que sean NULL, osea
los elementos que no se encuentran en la tabla Odd.
