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
2.2 Tecnologías utilizadas.

Frontend:
1. React: Librería de JavaScript, la más popular en la industria
2. Vue.js: Framework de JavaScript, intuitivo y fácil de integrar.
3. Tailwind CSS. Framework de CSS, diseño rápido directamente en el HTML/JSX.

Backend:
1. Express.js: para construir API REST de forma rápida usando JavaScript en el servidor.
2. FastAPI: Framework de Python moderno y de alto rendimiento.
3. PostgreSQL: para el manejo de datos que realizaría el Backend.

2.3 El frontend haría request al backend esperando un response de acuerdo al tipo de operación enviada utilizando el protocolo HTTP (PUT, DELETE, GET...) con un body o sin él, 
y siempre con sus respectivos Headers. 
En resumen, la comunicación se daría mediante un API que se comunica siguiente fielmente el protocolo HTTP en este caso hipotético.
##
 3. REST vs SOAP vs GraphQL
 
| Tipo de API | Formato de datos usado |  Nivel de flexibilidad |  Dificultad de implementación |  Uso actual (Alta / Media / Baja) |
|-------------|------------------------|------------------------|-------------------------------|-----------------------------------|
|REST         |         JSON           |         ALTO           |        MEDIA  (Nota 1)        |              ALTO                 |
|SOAP         |         XML            |        Muy BAJO        |			 ALTA               |              BAJO                 |
|GraphQL      |JSON y propio de consultas|       ALTO           |			 BAJA               |              MEDIA                |

Nota 1: REST y dificultad de implementación media se refiere a cuando se debe trabajar con un API REST ya creado, debido a su flexibilidad dos REST API pueden funcionar de maneras totalmente distintas.

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**
REST API, porque es la más utilizada en la industria y fácil de implementar de cero. Se podría considerar como opción GraphQL si la industria gana más confianza y utilización a largo plazo.
##
 4. Explorando APIs con Postman

###
 4.1 Selección de la API

- **Nombre de la API: PokéAPI**
- **Descripción: Todos los datos de Pokémon en una API de fácil acceso**

###
 4.2 Configuración en Postman
- **Nombre de la colección:**
- **Solicitudes agregadas:**
  - GET -
  - POST -
  - PUT/PATCH/DELETE -
  
###
 4.3 Ejecución y análisis

**PokéAPI**
|       Solicitud       | Método |                   Endpoint                                 |                   Header                      | Código de estado |  Notas              |
|-----------------------|--------|------------------------------------------------------------|-----------------------------------------------|------------------|---------------------|
|Obtener data de Pokémon|  GET   | https://pokeapi.co/api/v2/pokemon/4/                       | Content-Type: application/json; charset=utf-8 |     200 OK       | Exitoso             |
|    Delete Pokémon     | DELETE | https://pokeapi.co/api/v2/pokemon-species/?name=pidgeotto  |      text/html; charset=UTF-8                 |  403 Forbidden   | Acceso no autorizado|

**jsonplaceholderAPI
|       Solicitud       | Método |                   Endpoint                                 |                   Header                      | Código de estado |  Notas              |
|-----------------------|--------|------------------------------------------------------------|-----------------------------------------------|------------------|---------------------|
|Post new data          |  POST  | https://jsonplaceholder.typicode.com/posts/                | Content-Type: application/json; charset=utf-8 |    201 Created   | Exitoso             |
Body:
{
    "title": "Useful information",
    "body": "This is the useful information",
    "userId": 5
}

###
 4.4 Explicación técnica
La primera API PokeAPI tiene todos los datos de los Pokémon, es de solo lectura.
La segunda API permite hacer todos los métodos principales, no solamente el método GET. Con random data.
####
 [Obtener data de Pokémon]

- **Método HTTP:**
GET
- **Endpoint:**
https://pokeapi.co/api/v2/pokemon/4/

- **Parámetros / body:**
Path parameter: id: 4

- **Descripción de la respuesta:**
Respuesta exitosa 200. Response obtenido para el pokémon con id 4.

**¿Qué aprendiste del proceso?**
A realizar request específicos modificando path parameters

 [Delete Pokémon]

- **Método HTTP:**
DELETE
- **Endpoint:**
https://pokeapi.co/api/v2/pokemon-species/?name=pidgeotto

- **Parámetros / body:**
Query parameter: 
Key: name
Value: pidgeotto

- **Descripción de la respuesta:**
Respuesta fallida 403 Forbidden.

**¿Qué aprendiste del proceso?**
A realizar request usando query parameters y que el request es correcto, el servidor lo entendió pero, no está permitida la acción de DELETE en este caso específico.
Analizando más a fonde se ve que:
Content-Type: text/html; charset=UTF-8
Server: cloudflare
Y en el body se nota que existe la misma información en las primeras líneas:
<head>
    <title>Attention Required! | Cloudflare</title>
    <meta charset="UTF-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

Investigando más vi que realmente lo respondió Cloudflare, una capa de seguridad previa no la API de PokeAPI. Y tiene sentido el tipo de Content-Type recibido, puesto que el body realmente es HTML no json.
Si la solicitud hubiese llegado a la API, el response para un método no soportado por un Endpoint debería haber sido: 405 Method Not Allowed y suele incluir un header Allow: GET, HEAD que específica los métodos permitidos.
El 403 Forbidden es la prohibición que hace Cloudflare para proteger, bloquear y no permitir que la solicitud alcance el API.
Esto se llama WAF (Web Application Firewall).

 [Post new data]

- **Método HTTP:**
POST
- **Endpoint:**
https://jsonplaceholder.typicode.com/posts/ 

- **Parámetros / body:**
Body:
{
    "title": "Useful information",
    "body": "This is the useful information",
    "userId": 5
}


- **Descripción de la respuesta:**
Respuesta exitosa 201 Created. Se creó el nuevo recurso con éxito.

**¿Qué aprendiste del proceso?**
El server se encarga de asignar un ID automáticamente para asegurarse que no se repitan IDs.
Y aprendí un nuevo status code más específico: 201 Created.
###
 4.5 Reflexión final
 
 **¿Qué aprendiste sobre el funcionamiento de las APIs?**
Se comprueba la teoría, las APIs siguen su propia estructura, sus funciones y valores. Esencialmente, analizar que nos permiten comunicarnos con el servidor en un lenguaje que entiende, en este caso HTTP.
Básicamente es como un lenguaje intermediario que pueden entender tanto el cliente como el servidor, siempre y cuando se siga el protocolo de elección.
 
**¿Cómo te ayudó Postman a entender la comunicación entre cliente y servidor?**
Observando los status codes y el body del response obtenido en caso de haberlo, me permitió entender mejor lo que normalmente no se observa al hacer solicitudes desde el navegador.
La analogía con funciones y parámetros se observa con evidencia, es como estar llamando una función del servidor y a la vez con dicha función este accede a la base de datos, si es que el request realmente existe.
Muy importante cuando la solicitud fue fallida, para analizar de dónde viene el error si es que lo hay, y entender que no siempre es un error ni del cliente ni del servidor, es simplemente asunto de los permisos.