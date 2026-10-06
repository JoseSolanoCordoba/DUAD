#
 Fundamentos de Internet 

##
 1. Del Cliente al Servidor
Lo primero que ocurre es el navegador haciendo un request al servidor. Específicamente al DNS (Domain Name Server) que se encarga de "traducir" la url a una dirección IP.
El DNS que está preconfigurado en el router del proveedor, devuelve la dirección IP (internet protocol) al navegador.
Luego el navegador utiliza esa dirección IP 192.168... para hacer otros request a servidores específicos que tienen esa dirección IP asociada y que los identifica.
Se pueden hacer varias consultas para así poder obtener la información requerida de los servidores consultados que, básicamente estarían devolviendo lo solicitado al cliente o navegador.
El HTTP o hyper text transfer protocol se mueve detras de cada interacción entre cliente-servidor, es el procotolo más utilizado en internet.
##
 2. Frontend y Backend en acción
2.1 Frontend: interfaz de usuario, que incluiría calendarios visibles, disponibilidad y demás.
	Backend: toda la lógica que se mueve sin necesariamente ser vista por el usuario; base de datos, autenticación, y todo el flujo de control que hace posible la app.
2.2 Para el frontend javascript, java(con librerías), python(con librerías), para el backend python, java, C#...
2.3 El frontend haría request al backend esperando un response de acuerdo al tipo de operación enviada utilizando el protocolo HTTP (PUT, DELETE, GET...) con un body o sin él, y siempre con sus respectivos Headers. En resumen, la comunicación
se daría mediante un API que se comunica siguiente fielmente el protocolo HTTP en este caso hipotético.
##
 3. REST vs SOAP vs GraphQL
| Tipo de API | Formato de datos usado |  Nivel de flexibilidad |  Dificultad de implementación |  Uso actual (Alta / Media / Baja) |
|-------------|------------------------|------------------------|-------------------------------|-----------------------------------|
|REST         |         JSON           |         ALTO           |        MEDIA  (Nota 1)        |              ALTO                 |
|SOAP         |         XML            |        Muy BAJO        |			 ALTA               |              BAJO                 |
|GraphQL      |JSON y propio de consultas|       ALTO           |			 BAJA               |              MEDIA                |

Nota 1: REST y dificultad de implementación media se refiere a cuando se debe trabajar con un API REST ya creado, debido a su flexibilidad dos REST API pueden funcionar de maneras totalmente distintas.

**
¿Cuál es más apropiada para una startup moderna? ¿Por qué?
**
REST API, porque es la más utilizada en la industria y fácil de implementar de cero. Se podría considerar como opción GraphQL si la industria gana más confianza y utilización a largo plazo.
##
 4. Explorando APIs con Postman

###
 4.1 Selección de la API

-
 
**
Nombre de la API:
**

-
 
**
Descripción:
**

###
 4.2 Configuración en Postman

-
 
**
Nombre de la colección:
**

-
 
**
Solicitudes agregadas:
**

  
-
 GET -
  
-
 POST -
  
-
 PUT/PATCH/DELETE -
###
 4.3 Ejecución y análisis

|
 Solicitud 
|
 Método 
|
 Endpoint 
|
 Código de estado 
|
 Notas 
|
|
-----------
|
--------
|
----------
|
-------------------
|
-------
|
|
|
|
|
|
|

###
 4.4 Explicación técnica

####
 [Nombre de la solicitud]

-
 
**
Método HTTP:
**

-
 
**
Endpoint:
**

-
 
**
Parámetros / body:
**

-
 
**
Descripción de la respuesta:
**

**
¿Qué aprendiste del proceso?
**

###
 4.5 Reflexión final