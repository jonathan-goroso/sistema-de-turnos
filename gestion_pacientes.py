from tabulate import tabulate
from persistencia import guardar_datos
from validaciones import (
    pedir_dato_valido,
    validar_dni,
    validar_nombre,
    validar_correo,
    validar_telefono,
)


def mostrar_menu_pacientes() -> None:
    """
    Muestra por pantalla las opciones disponibles del menú de pacientes.

    Contrato:
    - Imprime en consola la lista numerada de opciones del menú (del 1 al 5
      y la opción 0 para volver) seguida de una línea en blanco.

    Precondiciones:
    - Ninguna. No recibe parámetros.

    Postcondiciones:
    - Imprime las opciones en pantalla y una línea vacía al final.
    - No solicita datos por teclado, no retorna ningún valor y no modifica
      el estado del sistema.
    """
    print("---------menú pacientes---------") 
    ops = {
        "1": "Registrar paciente",
        "2": "Modificar paciente",
        "3": "Dar de baja a un paciente",
        "4": "Consultar paciente",
        "5": "Listar pacientes",
        "0": "Volver al menú principal",
    }
    for clave, valor in ops.items():
        print(f"{clave}- {valor}")
    print()


def registrar_paciente(pacientes: dict[str, dict]) -> bool:
    """
    Registra un nuevo paciente en el sistema.

    Contrato:
    - Solicita por teclado el DNI. Si ya está registrado, informa y termina.
    - Si no lo está, solicita nombre, apellido, correo y teléfono, volviendo
      a pedir cada dato hasta que sea válido.
    - Agrega al paciente usando el DNI como clave.

    Precondiciones:
    - pacientes es un diccionario (puede estar vacío) cuyas claves son DNI
      (str) y cuyos valores son diccionarios con las claves "nombre",
      "apellido", "correo" y "telefono".

    Postcondiciones:
    - Si el DNI no estaba registrado, 'pacientes' tiene un paciente más, con
      ese DNI como clave, y se informa "Paciente registrado." y devuelve True.
    - Si el DNI ya estaba registrado, 'pacientes' no se modifica y se informa
      el motivo y devuelve False.
    """
    dni = pedir_dato_valido(
        "Ingrese el DNI (7 u 8 dígitos): ",
        validar_dni,
        "DNI inválido: ingresá solo números, sin puntos.",
    )
    if dni in pacientes:
        print("Ya existe un paciente registrado con ese DNI.")
        return False

    nombre = pedir_dato_valido(
        "Ingrese el nombre: ", validar_nombre, "Nombre inválido: usá solo letras."
    )
    apellido = pedir_dato_valido(
        "Ingrese el apellido: ", validar_nombre, "Apellido inválido: usá solo letras."
    )
    correo = pedir_dato_valido(
        "Ingrese el correo: ",
        validar_correo,
        "Correo inválido: ejemplo usuario@dominio.com.",
    )
    telefono = pedir_dato_valido(
        "Ingrese el número de teléfono (10 dígitos, sin 0 ni 15): ",
        validar_telefono,
        "Teléfono inválido: ingresá 10 dígitos, sin espacios ni guiones.",
    )

    pacientes[dni] = {
        "nombre": nombre.title(),
        "apellido": apellido.title(),
        "correo": correo,
        "telefono": telefono,
    }

    print("Paciente registrado.")
    return True


def modificar_paciente(pacientes: dict[str, dict]) -> bool:
    """
    Modifica un dato (nombre, apellido, correo o teléfono) de un paciente.

    Contrato:
    - Solicita por teclado el DNI y, si el paciente existe, qué dato modificar
      y su nuevo valor, que se vuelve a pedir hasta que sea válido.
    - El DNI no se puede modificar porque es la clave del paciente.

    Precondiciones:
    - pacientes es un diccionario (puede estar vacío) cuyas claves son DNI
      (str) y cuyos valores son diccionarios con las claves "nombre",
      "apellido", "correo" y "telefono".

    Postcondiciones:
    - Si el DNI existe y la opción elegida es válida, se actualiza ese único
      dato del paciente y se informa "Paciente modificado." y devuelve True.
    - Si el DNI no existe o la opción es inválida, pacientes no se modifica
      y se informa el motivo y devuelve False.
    - Ningún otro paciente ni otro dato se modifica.
    """
    dni = pedir_dato_valido(
        "Ingrese el DNI del paciente: ",
        validar_dni,
        "DNI inválido: ingresá solo números, sin puntos.",
    )
    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return False

    print("------Dato a modificar------")
    opciones_modificar_paciente()
    opcion = input("Elija una opción: ")

    match opcion:
        case "1":
            campo = "nombre"
            nuevo_valor = pedir_dato_valido(
                "Ingrese el nuevo nombre: ",
                validar_nombre,
                "Nombre inválido: usá solo letras.",
            ).title()
        case "2":
            campo = "apellido"
            nuevo_valor = pedir_dato_valido(
                "Ingrese el nuevo apellido: ",
                validar_nombre,
                "Apellido inválido: usá solo letras.",
            ).title()
        case "3":
            campo = "correo"
            nuevo_valor = pedir_dato_valido(
                "Ingrese el nuevo correo: ",
                validar_correo,
                "Correo inválido: ejemplo usuario@dominio.com.",
            )
        case "4":
            campo = "telefono"
            nuevo_valor = pedir_dato_valido(
                "Ingrese el nuevo teléfono (10 dígitos, sin 0 ni 15): ",
                validar_telefono,
                "Teléfono inválido: ingresá 10 dígitos, sin espacios ni guiones.",
            )
        case _:
            print("Opción no válida")
            return False

    pacientes[dni][campo] = nuevo_valor
    print("Paciente modificado.")
    return True


def opciones_modificar_paciente() -> None:
    """
    Muestra por pantalla los campos de un paciente que pueden modificarse.

    Contrato:
    - Imprime en consola las opciones numeradas correspondientes a los campos
      modificables de un paciente (Nombre, Apellido, Correo y Teléfono).

    Precondiciones:
    - Ninguna. No recibe parámetros.

    Postcondiciones:
    - Imprime las opciones de modificación en pantalla y una línea vacía al final.
    - No solicita datos por teclado, no retorna ningún valor y no modifica
      el estado del sistema.
    """
    ops = {"1": "Nombre", "2": "Apellido", "3": "Correo", "4": "Teléfono"}
    for clave, valor in ops.items():
        print(f"{clave}-{valor}")
    print()


def eliminar_paciente(pacientes: dict[str, dict], turnos: dict[str, list[str]]) -> bool:
    """
    Elimina a un paciente del sistema, siempre que no tenga turnos asignados.

    Contrato:
    - Solicita por teclado el DNI y, si el paciente existe y no tiene turnos,
      lo elimina por completo del sistema.

    Precondiciones:
    - 'pacientes' es un diccionario (puede estar vacío) cuyas claves son DNI
      (str) y cuyos valores son diccionarios con las claves "nombre",
      "apellido", "correo" y "telefono".
    - turnos es el diccionario de turnos del sistema (puede estar vacío).

    Postcondiciones:
    - Si el DNI existe y el paciente no tiene turnos, se elimina esa clave de
      pacientes y se informa "Paciente <nombre> <apellido> eliminado." y devuelve True.
    - Si el DNI no existe o el paciente tiene turnos, 'pacientes' no se
      modifica y se informa el motivo y devuelve False.
    - turnos nunca se modifica.
    """

    dni = pedir_dato_valido(
        "Ingrese el DNI del paciente: ",
        validar_dni,
        "DNI inválido: ingresá solo números, sin puntos.",
    )
    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return False

    if paciente_tiene_turnos(turnos, dni):
        print("No se puede eliminar: el paciente tiene turnos asignados.")
        return False

    paciente = pacientes[dni]
    del pacientes[dni]
    print(f"Paciente {paciente['nombre']} {paciente['apellido']} eliminado.")
    return True


def paciente_tiene_turnos(turnos: dict[str, list[str]], dni: str) -> bool:
    """
    Indica si un paciente tiene al menos un turno asignado.

    Contrato:
    - Recorre los turnos y comprueba si alguno pertenece al DNI recibido.

    Precondiciones:
    - 'turnos' es un diccionario {id: [dni, fecha, hora]} (puede estar vacío).
    - dni es un str.

    Postcondiciones:
    - Devuelve True si algún turno tiene ese DNI; False en caso contrario.
    - No modifica turnos.
    """
    for datos in turnos.values():
        if datos[0] == dni:
            return True
    return False


def consultar_paciente(pacientes: dict[str, dict]) -> None:
    """
    Muestra por pantalla los datos de un paciente.

    Contrato:
    - Solicita por teclado el DNI y, si el paciente existe, muestra sus datos
      en una tabla.

    Precondiciones:
    - 'pacientes' es un diccionario con la estructura
      acordada.

    Postcondiciones:
    - Si el DNI existe, se muestra la tabla con los datos del paciente.
    - Si no existe, se informa el motivo.
    - No modifica pacientes.
    """
    dni = pedir_dato_valido(
        "Ingrese el DNI del paciente: ",
        validar_dni,
        "DNI inválido: ingresá solo números, sin puntos.",
    )
    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return

    print("                     FICHA DEL PACIENTE")
    mostrar_pacientes({dni: pacientes[dni]})


def mostrar_pacientes(pacientes: dict[str, dict]) -> None:
    """
    Muestra por pantalla una tabla con los datos de los pacientes recibidos.

    Contrato:
    - Arma una fila por paciente con DNI, nombre, apellido, correo y teléfono,
      y la imprime como tabla con encabezados.

    Precondiciones:
    - pacientes es un diccionario con al menos un paciente, con la estructura
      acordada (claves DNI en str; valores con "nombre", "apellido",
      "correo" y "telefono").

    Postcondiciones:
    - Se imprime la tabla con todos los pacientes recibidos.
    - No modifica pacientes ni solicita datos por teclado.
    """
    filas = []
    for dni, datos in pacientes.items():
        filas.append(
            [
                dni,
                datos["nombre"],
                datos["apellido"],
                datos["correo"],
                datos["telefono"],
            ]
        )
    encabezados = ["DNI", "Nombre", "Apellido", "Correo", "Teléfono"]
    print(
        tabulate(
            filas, headers=encabezados, tablefmt="simple_grid", disable_numparse=True
        )
    )


def listar_pacientes(pacientes: dict[str, dict]) -> None:
    """
    Muestra por pantalla a todos los pacientes del sistema.

    Contrato:
    - Muestra una tabla con todos los pacientes registrados.

    Precondiciones:
    - 'pacientes' es un diccionario con la estructura
      acordada.

    Postcondiciones:
    - Si hay pacientes, se muestra la tabla con todos ellos.
    - Si no hay ninguno, se informa que no hay pacientes registrados.
    - No modifica pacientes.
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    print("                           PACIENTES")
    mostrar_pacientes(pacientes)


def gestionar_pacientes(pacientes: dict[str, dict], turnos, archivo: str) -> None:
    """
    Muestra el menú de pacientes y deriva cada opción a su función.

    Contrato:
    - Repite el menú hasta que el usuario elija la opción 0 (volver al menú
      principal).
    - Según la opción, llama a registrar_paciente, modificar_paciente,
      eliminar_paciente, consultar_paciente o listar_pacientes.
    - No valida ni modifica datos por sí misma: delega todo en esas funciones.
    - Si alguna de las opciones que modifican datos (1, 2 o 3) se completó con éxito, guarda pacientes en pacientes.json mediante guardar_datos.

    Precondiciones:
    - pacientes es un diccionario (puede estar vacío) cuyas claves son DNI
      (str) y cuyos valores son diccionarios con las claves "nombre",
      "apellido", "correo" y "telefono".

    Postcondiciones:
    - Termina únicamente cuando el usuario elige la opción 0.
    - Al terminar, pacientes.json contiene los pacientes tal como quedaron
      después de la última modificación.
    - Si el usuario elige una opción que no existe, informa "Opción no
      válida" y vuelve a mostrar el menú sin modificar pacientes.
    """
    while True:
        print("-------- Menú pacientes --------")
        mostrar_menu_pacientes()

        opcion = input("Elija una opción: ")

        match opcion:
            case "0":
                break
            case "1":
                if registrar_paciente(pacientes):
                    guardar_datos(archivo, pacientes)
                    print()
            case "2":
                if modificar_paciente(pacientes):
                    guardar_datos(archivo, pacientes)
                    print()
            case "3":
                if eliminar_paciente(pacientes, turnos):
                    guardar_datos(archivo, pacientes)
                    print()
            case "4":
                consultar_paciente(pacientes)
                print()
            case "5":
                listar_pacientes(pacientes)
                print() 
            case _:
                print("Opción no válida")
                print() 
