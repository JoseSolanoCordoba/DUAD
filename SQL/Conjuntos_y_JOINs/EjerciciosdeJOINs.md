# Tarea: Ejercicios de Normalización
**Estudiante:** [José Andrés Solano Córdoba]  
**Módulo:** Bases de datos — Lyfter Learning  

---

### Tabla informativa GROUP BY, ORDER BY, LIMIT

|                    | GROUP BY                                                               | ORDER BY                                                                                 | LIMIT                                              |
|--------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------|
| Basic utility      | To group extracted data, including multiple columns                    | To order extracted data, including multiple columns.  Two options: Ascending/Descending. | To restrict the number of rows database extracts.  |
| Basic syntax       | GROUP BY column A, column B,....;                                      | ORDER BY columnA ASC/DESC, columnB ASC/DESC....;                                         | LIMIT integernumber; Ex: LIMIT 50;                 |
| Order              | After WHERE                                                            | After WHERE, GROUP BY, HAVING                                                            | This is the last query to be executed (and OFFSET) |
| Normally used with | Aggregate functions: COUNT(), SUM(), and AVG()                         | Aliases in SELECT                                                                        | Any other clause.                                  |
| Restrictions       | All the select columns must be grouped, except the aggregate functions | The order                                                                                | The order                                          |

### Tabla informativa INNER JOIN, RIGHT/LEFT JOIN, FULL OUTER JOIN

|              | INNER JOIN                                                                                  | RIGHT/LEFT JOIN                                                                                                                                                                         | FULL OUTER JOIN                                                                                                                           |
|--------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Basic Syntax | FROM (Lefttable) INNER JOIN (Righttable) ON (columnA=columnB)                               | FROM (Lefttable) LEFT JOIN (Righttable) ON (columnA=columnB)                                                                                                                            | FROM (Lefttable) FULL OUTER JOIN (Righttable) ON (columnA=columnB)                                                                        |
| Explanation  | Will return the common data in both tables matching columns from left table and right table | Will return the common data in both tables matching columns from left table and right table. Plus data only present in left table. For RIGHT JOIN is the same but for right table side. | Will return the common data in both tables, plus the data present only in the left and the right tables. Basically will return the Union. |