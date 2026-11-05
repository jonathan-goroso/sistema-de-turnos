# Sistema de Gestión de Turnos

## Descripción

Sistema de gestión de turnos desarrollado en Python, que permite administrar pacientes, registrar turnos y consultar la disponibilidad de horarios.

El programa funciona mediante un menú interactivo en la terminal y utiliza archivos JSON para almacenar la información de los pacientes y sus turnos.

## Funcionalidades

### Gestión de pacientes

- Registrar pacientes con DNI, nombre, apellido, correo electrónico y teléfono.
- Validar los datos ingresados.
- Modificar la información de un paciente registrado.
- Consultar los datos de un paciente mediante su DNI.
- Listar todos los pacientes registrados en formato de tabla.
- Dar de baja a pacientes

### Gestión de turnos

- Registrar turnos para pacientes existentes.
- Generar automáticamente un identificador único de cuatro dígitos para cada turno.
- Modificar el paciente, la fecha o el horario de un turno.
- Cancelar turnos registrados.
- Consultar turnos mediante su identificador.
- Listar todos los turnos registrados.
- Consultar los turnos de un paciente.
- Consultar la disponibilidad de horarios para una fecha determinada.
- Evitar la asignación de dos turnos al mismo horario y fecha.

### Gestión de horarios

- Configurar el horario de inicio y finalización de la atención.
- Generar horarios en intervalos de 30 minutos.
- Utilizar los horarios configurados para registrar y modificar turnos.

**Nota:** Los horarios configurados se mantienen durante la ejecución del programa, pero actualmente no se guardan en un archivo.

## Tecnologías utilizadas

- **Python version 3.13.15:** lenguaje de programación principal.
- **JSON:** almacenamiento de pacientes y turnos.
- **tabulate:** presentación de los datos de pacientes en tablas.
- **pytest:** ejecución de pruebas automatizadas.

También se utilizan los módulos estándar `re` y `datetime`.

## Estructura del proyecto

```text
sistema-de-turnos/
│
├── data/
│   ├── pacientes.json
│   └── turnos.json
│
├── tests/
│   ├── test_pacientes.py
│   ├── test_turnos.py
│   └── test_validaciones.py
│
├── .gitignore
├── gestion_pacientes.py
├── gestion_turnos.py
├── persistencia.py
├── README.md
├── requirements.txt
├── sistema_turnos.py
└── validaciones.py
```

Los archivos JSON se crean cuando se guardan datos por primera vez. No es necesario que existan previamente.

### Descripción de los archivos

| Archivo | Función |
|---|---|
| `sistema_turnos.py` | Contiene el menú principal e inicia el programa. |
| `gestion_pacientes.py` | Gestiona los pacientes y valida sus datos. |
| `gestion_turnos.py` | Gestiona los turnos y la disponibilidad de horarios. |
| `persistencia.py` | Permite leer y guardar información en archivos JSON. |
| `test_pacientes.py` | Contiene pruebas de validación de datos de pacientes y lectura de archivos. |
| `test_turnos.py` | Archivo destinado a las pruebas del módulo de turnos. |
| `validaciones.py`| Centraliza las validaciones de datos (DNI,fechas,horarios) y entradas por teclado. |
| `.gitignore` | Indica los archivos y carpetas que Git debe ignorar. |



## Ejecución del programa

Desde la carpeta principal del proyecto, ejecutar:
```bash
pip install -r requirements.txt
```

Luego
```bash
python sistema_turnos.py
```

Se mostrará el menú principal:

```text
-----menu principal-----
1-Gestionar pacientes
2-Gestionar turnos
3-Gestionar horarios
0-Salir del programa
```


## Almacenamiento de datos

Los datos se almacenan en archivos JSON dentro de la carpeta `data/`.

- `pacientes.json`: almacena los pacientes utilizando el DNI como clave.
- `turnos.json`: almacena los turnos utilizando un identificador único como clave.

La información se carga al iniciar el programa y se guarda después de las operaciones que modifican los datos, siempre que estas informen que se completaron correctamente.


## Consideraciones

- El sistema funciona desde la terminal.
- Los pacientes se identifican mediante su DNI.
- Cada turno tiene un identificador único.
- Un paciente puede tener varios turnos registrados.
- No se permite registrar dos turnos para la misma fecha y horario.
- Los datos se almacenan localmente mediante archivos JSON.