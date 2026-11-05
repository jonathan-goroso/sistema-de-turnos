

# Plan de pruebas — Sistema de turnos

## 1. Objetivo

Documentar los casos de prueba definidos para comprobar algunas funcionalidades del sistema de turnos. Para cada caso se indica qué se prueba, cuál es el resultado esperado y por qué se eligió ese caso.

Las pruebas automatizadas se encuentran en la carpeta `tests/` y se ejecutan con `pytest`.

## 2. Ejecución de las pruebas

Desde la carpeta raíz del proyecto, ejecutar:

```bash
py -m pytest -v
```

El resultado obtenido indica el valor que devuelve la función o el comportamiento observado al ejecutar cada prueba.

## 3. Pruebas de pacientes y persistencia

Archivo: `tests/test_pacientes.py`

### 3.1. Validación del DNI

Se comprueba que el DNI esté formado por 7 u 8 dígitos, que no comience con cero y que no contenga letras, símbolos ni espacios.

| Caso | Entrada | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Acepta 8 dígitos | `"12345678"` | `True` | Comprueba una longitud válida de 8 dígitos. | `True` |
| Acepta 7 dígitos | `"1234567"` | `True` | Comprueba la longitud mínima permitida. | `True` |
| Rechaza 6 dígitos | `"123456"` | `False` | Comprueba una longitud inferior al mínimo. | `False` |
| Rechaza 9 dígitos | `"123456789"` | `False` | Comprueba una longitud superior al máximo. | `False` |
| Rechaza cero inicial | `"02345678"` | `False` | Comprueba que el primer dígito no pueda ser cero. | `False` |
| Rechaza letras | `"12ABC678"` | `False` | Comprueba que el DNI contenga únicamente dígitos. | `False` |
| Rechaza puntos | `"12.345.678"` | `False` | Comprueba que no se admitan separadores ni símbolos. | `False` |
| Rechaza cadena vacía | `""` | `False` | Comprueba que sea obligatorio ingresar un DNI. | `False` |
| Rechaza espacios | `" 12345678 "` | `False` | Comprueba que la función no acepte espacios al principio o al final. | `False` |

### 3.2. Validación de nombres y apellidos

Se comprueba que el nombre o apellido esté formado por letras y que admita los caracteres y separadores contemplados por la función: tildes, diéresis, ñ, espacios simples y apóstrofes. También se comprueba el rechazo de números, símbolos, espacios consecutivos y guiones.

| Caso | Entrada | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Acepta nombre simple | `"Luis"` | `True` | Comprueba un nombre formado por una sola palabra. | `True` |
| Acepta nombre compuesto | `"De la Torre"` | `True` | Comprueba varias palabras separadas por espacios simples. | `True` |
| Acepta nombre con tilde | `"José Luis"` | `True` | Comprueba la aceptación de vocales con tilde. | `True` |
| Acepta apóstrofe | `"D'abundo"` | `True` | Comprueba que se permita un apóstrofe como separador. | `True` |
| Acepta diéresis | `"Güemes"` | `True` | Comprueba la aceptación de la letra ü. | `True` |
| Acepta ñ | `"Muñoz"` | `True` | Comprueba la aceptación de la letra ñ. | `True` |
| Rechaza cadena vacía | `""` | `False` | Comprueba que se requiera al menos una palabra. | `False` |
| Rechaza números | `"Carlos123"` | `False` | Comprueba que no se admitan dígitos. | `False` |
| Rechaza símbolos | `"Ana@!#%"` | `False` | Comprueba que no se admitan símbolos ajenos al formato. | `False` |
| Rechaza espacios consecutivos | `"José   Luis"` | `False` | Comprueba que entre palabras se permita un solo espacio. | `False` |
| Rechaza guiones | `"José-Luis"` | `False` | Comprueba que el guion no forma parte de los separadores admitidos. | `False` |

### 3.3. Validación del correo electrónico

Se comprueba que el correo tenga la forma `usuario@dominio.extensión`, con usuario, dominio y una extensión de al menos dos letras. También se comprueban algunos caracteres permitidos y formatos inválidos contemplados por la función.

| Caso | Entrada | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Acepta correo habitual | `"juan@gmail.com"` | `True` | Comprueba una dirección con formato habitual. | `True` |
| Acepta puntos y signo más en usuario | `"juan.perez+turnos@gmail.com"` | `True` | Comprueba caracteres permitidos en la parte del usuario. | `True` |
| Acepta guion en dominio | `"juan@mi-dominio.com"` | `True` | Comprueba que se permita un guion en el dominio. | `True` |
| Acepta subdominio | `"juan@consultorio.ejemplo.com"` | `True` | Comprueba que se admitan varios componentes de dominio separados por puntos. | `True` |
| Rechaza cadena vacía | `""` | `False` | Comprueba que sea obligatorio ingresar una dirección. | `False` |
| Rechaza ausencia de arroba | `"juangmail.com"` | `False` | Comprueba que la arroba sea obligatoria. | `False` |
| Rechaza ausencia de usuario | `"@gmail.com"` | `False` | Comprueba que debe existir un usuario antes de la arroba. | `False` |
| Rechaza ausencia de dominio | `"juan@"` | `False` | Comprueba que debe existir un dominio después de la arroba. | `False` |
| Rechaza ausencia de extensión | `"juan@gmail"` | `False` | Comprueba que el dominio tenga una extensión. | `False` |
| Rechaza extensión de una letra | `"juan@gmail.c"` | `False` | Comprueba que la extensión tenga al menos dos letras. | `False` |
| Rechaza espacios | `"jose luis@gmail.com"` | `False` | Comprueba que no se admitan espacios. | `False` |
| Rechaza puntos consecutivos en dominio | `"juan@dominio..com"` | `False` | Comprueba que no haya puntos consecutivos en el dominio. | `False` |
| Rechaza dos arrobas | `"juan@@gmail.com"` | `False` | Comprueba que la dirección tenga una sola arroba. | `False` |
| Rechaza números en extensión | `"juan@gmail.c1"` | `False` | Comprueba que la extensión esté formada por letras. | `False` |

### 3.4. Validación del teléfono

Se comprueba que el teléfono esté formado por exactamente 10 dígitos y que el primer dígito no sea cero, de acuerdo con el patrón utilizado por el validador.

| Caso | Entrada | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Acepta número habitual | `"1155558482"` | `True` | Comprueba un número de 10 dígitos. | `True` |
| Acepta primer dígito uno | `"1123456789"` | `True` | Comprueba que se acepte un número que comienza con 1. | `True` |
| Rechaza 9 dígitos | `"115555848"` | `False` | Comprueba una longitud inferior a la requerida. | `False` |
| Rechaza 11 dígitos | `"11555584820"` | `False` | Comprueba una longitud superior a la requerida. | `False` |
| Rechaza cero inicial | `"01155558482"` | `False` | Comprueba que el primer dígito no sea cero. | `False` |
| Rechaza letras | `"1155ABcd82"` | `False` | Comprueba que solo se admitan dígitos. | `False` |
| Rechaza guiones | `"115555-842"` | `False` | Comprueba que no se admitan separadores. | `False` |
| Rechaza espacios | `"115555 8548"` | `False` | Comprueba que no se admitan espacios. | `False` |
| Rechaza cadena vacía | `""` | `False` | Comprueba que sea obligatorio ingresar un teléfono. | `False` |

### 3.5. Lectura de datos persistidos

Se comprueba el comportamiento de la función que lee información desde un archivo JSON.

| Caso | Entrada / situación | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Archivo inexistente | `leer_datos("archivo_que_no_existe.json")` | `{}` | Comprueba que, cuando el archivo no existe, la función devuelve un diccionario vacío. | `{}` |

## 4. Pruebas de gestión de turnos

Archivo: `tests/test_turnos.py`

Estas pruebas comprueban el comportamiento de las operaciones cuando faltan datos necesarios o no hay turnos registrados.

| Caso | Datos de entrada / situación | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Registrar sin pacientes | Diccionario de turnos vacío, diccionario de pacientes vacío y horarios disponibles. | `False` | No se puede registrar un turno si no hay pacientes registrados. | `False` |
| Registrar sin horarios | Diccionario de turnos vacío, pacientes disponibles y lista de horarios vacía. | `False` | No se puede registrar un turno si no hay horarios disponibles. | `False` |
| Registrar sin datos no agrega turnos | Se intenta registrar con el diccionario de pacientes vacío. | El diccionario `turnos` permanece `{}`. | Comprueba que un intento de registro sin pacientes no modifique los turnos. | `{}` |
| Modificar sin turnos | Diccionario de turnos vacío, pacientes y horarios disponibles. | `False` | No se puede modificar un turno cuando no hay turnos registrados. | `False` |
| Eliminar sin turnos | Diccionario de turnos vacío. | `False` | No se puede eliminar un turno cuando no hay turnos registrados. | `False` |

## 5. Pruebas de funciones auxiliares de validación

Archivo: `tests/test_validaciones.py`

### 5.1. Generación de identificadores de turnos

| Caso | Datos de entrada | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Generar ID con diccionario vacío | `{}` | `"0001"` | Comprueba cuál es el primer identificador cuando todavía no hay turnos. | `"0001"` |
| Generar siguiente ID | Un diccionario que contiene el ID `"0001"`. | `"0002"` | Comprueba que se genere el identificador siguiente. | `"0002"` |
| Reutilizar ID libre | Un diccionario con los ID `"0001"` y `"0003"`. | `"0002"` | Comprueba que se pueda reutilizar un identificador faltante. | `"0002"` |

### 5.2. Comprobación de horarios ocupados

| Caso | Datos de entrada | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Horario ocupado en misma fecha y hora | Existe un turno para `01/01/2099` a las `9:00`; se consulta esa misma fecha y hora. | `True` | Comprueba que se detecte una coincidencia de fecha y hora. | `True` |
| Horario libre en otra hora | Existe un turno a las `9:00`; se consulta `9:30` en la misma fecha. | `False` | Comprueba que una hora diferente esté libre. | `False` |
| Horario libre en otra fecha | Existe un turno el `01/01/2099` a las `9:00`; se consulta el `02/01/2099` a las `9:00`. | `False` | Comprueba que la ocupación de una hora no se extienda a otra fecha. | `False` |
| Horario libre con diccionario vacío | No hay turnos registrados. | `False` | Comprueba el comportamiento con una colección vacía. | `False` |
| Ignorar turno excluido | Se consulta la fecha y hora de un turno, indicando su ID como excluido. | `False` | Comprueba que el turno indicado no se considere ocupado; resulta útil al modificarlo. | `False` |

### 5.3. Ordenamiento de turnos

| Caso | Datos de entrada | Resultado esperado | Justificación | Resultado obtenido |
|---|---|---|---|---|
| Ordenar por fecha | Dos turnos: uno del `02/01/2026` y otro del `01/12/2025`. | IDs ordenados: `["0002", "0001"]`. | Comprueba que los turnos se ordenen cronológicamente por fecha. | `["0002", "0001"]` |
| Ordenar por hora en el mismo día | Dos turnos del `01/01/2026`, uno a las `10:00` y otro a las `9:00`. | IDs ordenados: `["0002", "0001"]`. | Comprueba que, cuando la fecha coincide, se ordenen por hora. | `["0002", "0001"]` |

## 6. Resumen de cobertura actual

El siguiente resumen corresponde a las funciones de prueba que aparecen en los tres archivos compartidos.

| Archivo | Área | Cantidad de funciones de prueba |
|---|---|---:|
| `test_pacientes.py` | Validación de DNI | 9 |
| `test_pacientes.py` | Validación de nombres y apellidos | 10 |
| `test_pacientes.py` | Validación de correo | 14 |
| `test_pacientes.py` | Validación de teléfono | 9 |
| `test_pacientes.py` | Lectura de archivo | 1 |
| `test_turnos.py` | Gestión de turnos | 5 |
| `test_validaciones.py` | Funciones auxiliares | 10 |
| **Total** | | **58** |
