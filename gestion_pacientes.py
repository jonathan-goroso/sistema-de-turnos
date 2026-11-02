import re


def menu_pacientes() -> None:
    ops = {
        "1": "Registrar paciente",
        "2": "Modificar paciente",
        "3": "Dar de baja a un paciente",
        "4": "Consultar paciente",
        "5": "Listar pacientes",
        "0": "Volver al menú principal",
    }
    for indice, elemento in ops.items():
        print(f"{indice}-{elemento}")
    print()


"""
pacientes = {
    "12345678": {
        "nombre": "Juan", 
        "apellido": "Pérez", 
        "correo": "juan27@gmail.com", 
        "telefono": "2267444854"
    }
}
"""


def registrar_paciente(pacientes: dict[str, dict]) -> None:
    """
    Registra un nuevo paciente en el sistema.

    Contrato:
    - Solicita por teclado el DNI. Si ya está registrado, informa y termina.
    - Si no lo está, solicita nombre, apellido, correo y teléfono, volviendo
      a pedir cada dato hasta que sea válido.
    - Agrega al paciente usando el DNI como clave.
    - Solo modifica el diccionario en memoria: no guarda en ningún archivo.

    Precondiciones:
    - pacientes es un diccionario (puede estar vacío) cuyas claves son DNI
      (str) y cuyos valores son diccionarios con las claves "nombre",
      "apellido", "correo" y "telefono".

    Postcondiciones:
    - Si el DNI no estaba registrado, 'pacientes' tiene un paciente más, con
      ese DNI como clave, y se informa "Paciente registrado.".
    - Si el DNI ya estaba registrado, 'pacientes' no se modifica y se informa
      el motivo.
    - Ningún otro paciente se modifica.
    """
    dni = pedir_dato_valido(
        "Ingrese el DNI (7 u 8 dígitos): ",
        validar_dni,
        "DNI inválido: ingresá solo números, sin puntos.",
    )
    if dni in pacientes:
        print("Ya existe un paciente registrado con ese DNI.")
        return

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
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "telefono": telefono,
    }

    print("Paciente registrado.")


def pedir_dato_valido(mensaje: str, funcion_validadora, mensaje_error: str) -> str:
    """
    Solicita un dato por teclado hasta que el usuario ingrese uno válido.

    Contrato:
    - Muestra mensaje, lee lo que escribe el usuario y normaliza los espacios:
      quita los de los extremos y reduce los repetidos a uno solo.
    - Si el dato normalizado no cumple funcion_validadora, muestra
      mensaje_error y vuelve a pedirlo.
    - No tiene forma de cancelar: sigue pidiendo hasta recibir un dato válido.

    Precondiciones:
    - mensaje y mensaje_error son str.
    - funcion_validadora es una función que recibe un str y devuelve un bool
      (por ejemplo, validar_dni).

    Postcondiciones:
    - Devuelve un str que cumple funcion_validadora, con los espacios
      normalizados.
    - Imprime mensaje_error una vez por cada intento inválido.
    """
    while True:
        dato = " ".join(input(mensaje).split())
        if funcion_validadora(dato):
            return dato
        print(mensaje_error)


def validar_dni(dni: str) -> bool:
    """
    Indica si 'dni' tiene el formato de un DNI argentino.

    Contrato:
    - Comprueba que 'dni' esté formado únicamente por 7 u 8 dígitos, y que el primer dígito no sea un 0.
    - Valida solo el formato; no verifica que el DNI exista realmente ni contempla documentos antiguos con letra (F/M)

    Precondiciones:
    - 'dni' debe ser una cadena de texto.

    Postcondiciones:
    - Devuelve True si dni tiene 7 u 8 dígitos.
    - Devuelve False en cualquier otro caso (vacío, letras, símbolos, otra longitud, 0 inicial).
    - No modifica dni, no imprime nada y no solicita datos por teclado.
    """
    patron_dni = r"[1-9][0-9]{6,7}"
    return bool(re.fullmatch(patron_dni, dni))


def validar_nombre(nombre: str) -> bool:
    """
    Indica si un 'nombre' es válido como nombre o apellido de una persona.

    Contrato:
    - Comprueba que 'nombre' esté formado por una o más palabras de letras
      (con tildes, diéresis y ñ), separadas por un único espacio o apóstrofe.
    - Se usa tanto para el nombre como para el apellido.
    - Solo contempla letras del alfabeto latino del español; no admite otros alfabetos.

    Precondiciones:
    - 'nombre' debe ser una cadena de texto.

    Postcondiciones:
    - Devuelve True si 'nombre' cumple el formato descrito.
    - Devuelve False en cualquier otro caso (vacío, números, símbolos, etc.
    - No modifica 'nombre', no imprime nada y no solicita datos por teclado.
    """
    letras = "A-Za-zÁÉÍÓÚÜÑáéíóúüñ"
    patron_nombre = rf"[{letras}]+([ '][{letras}]+)*"
    return bool(re.fullmatch(patron_nombre, nombre))


def validar_correo(correo: str) -> bool:
    """
    Indica si un 'correo' tiene el formato de una dirección de correo electrónico.

    Contrato:
    - Comprueba que 'correo' tenga la forma usuario@dominio.extensión, con una extensión de al menos 2 letras.
    - Valida solo el formato; no verifica que la casilla exista ni cubre todos los casos raros que admite el estándar de correo.

    Precondiciones:
    - 'correo' debe ser una cadena de texto.

    Postcondiciones:
    - Devuelve True si correo tiene un usuario, una arroba, un dominio y una
      extensión de al menos 2 letras.
    - Devuelve False en cualquier otro caso (vacío, sin arroba, con espacios,
      sin extensión, con puntos consecutivos en el dominio).
    - No modifica 'correo', no imprime nada y no solicita datos por teclado.
    """
    patron_correo = r"[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,}"
    return bool(re.fullmatch(patron_correo, correo))


def validar_telefono(telefono: str) -> bool:
    """
    Indica si un 'telefono' tiene el formato de un teléfono argentino de 10 dígitos.

    Contrato:
    - Comprueba que 'telefono' sea el código de área (sin 0 inicial) seguido
      del número (sin 15), todo junto: 10 dígitos en total.
    - No contempla números extranjeros ni prefijos internacionales (+54), y
      no admite espacios ni guiones.

    Precondiciones:
    - 'telefono' debe ser una cadena de texto.

    Postcondiciones:
    - Devuelve True si 'telefono' son 10 dígitos (0-9) y el primero no es 0.
    - Devuelve False en cualquier otro caso (vacío, letras, guiones, otra
      longitud, 0 inicial).
    - No se modifica 'telefono'.
    """
    patron_telefono = r"[1-9][0-9]{9}"
    return bool(re.fullmatch(patron_telefono, telefono))


def modificar_paciente(pacientes: dict[str, dict]) -> None:
    """
    Modifica un dato (nombre, apellido, correo o teléfono) de un paciente.

    Contrato:
    - Solicita por teclado el DNI y, si el paciente existe, qué dato modificar
      y su nuevo valor, que se vuelve a pedir hasta que sea válido.
    - El DNI no se puede modificar porque es la clave del paciente.
    - Solo modifica el diccionario en memoria: no guarda en ningún archivo.

    Precondiciones:
    - pacientes es un diccionario (puede estar vacío) cuyas claves son DNI
      (str) y cuyos valores son diccionarios con las claves "nombre",
      "apellido", "correo" y "telefono".

    Postcondiciones:
    - Si el DNI existe y la opción elegida es válida, se actualiza ese único
      dato del paciente y se informa "Paciente modificado.".
    - Si el DNI no existe o la opción es inválida, pacientes no se modifica
      y se informa el motivo.
    - Ningún otro paciente ni otro dato se modifica.
    """
    dni = pedir_dato_valido(
        "Ingrese el DNI del paciente: ",
        validar_dni,
        "DNI inválido: ingresá solo números, sin puntos.",
    )
    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return

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
            )
        case "2":
            campo = "apellido"
            nuevo_valor = pedir_dato_valido(
                "Ingrese el nuevo apellido: ",
                validar_nombre,
                "Apellido inválido: usá solo letras.",
            )
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
            return

    pacientes[dni][campo] = nuevo_valor
    print("Paciente modificado.")


def opciones_modificar_paciente() -> None:
    ops = {"1": "Nombre", "2": "Apellido", "3": "Correo", "4": "Teléfono"}
    for indice, elemento in ops.items():
        print(f"{indice}-{elemento}")
    print()


def eliminar_paciente(pacientes: dict[int:list]) -> None:
    """
    elimina a un paciente del sistema

    pre: el diccionario debe tener al menos un elemento
    post: el paciente es eliminado del sistema
    """
    print("esta función da de baja a un paciente del sistema")


def consultar_paciente(pacientes: dict[int:list]) -> None:
    """
    muestra los datos de un paciente

    pre: el diccionario debe tener al menos un elemento
    post:muestra por pantalla los datos del paciente
    """
    print("permite consultar los datos de un paciente")


def listar_pacientes(pacientes: dict[int:list]) -> None:
    """
    muestra a todos los pacientes del sistema

    pre: el diccionario debe tener al menos un elemento
    post: muestra por pantalla a todos los pacientes
    """
    print("lista a todos los pacientes del sistema")


def gestionar_pacientes(pacientes: dict[str, dict]) -> None:
    while True:
        print("---------menú de pacientes-------")
        menu_pacientes()

        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                registrar_paciente(pacientes)
            case "2":
                modificar_paciente(pacientes)
            case "3":
                eliminar_paciente(pacientes)
            case "4":
                consultar_paciente(pacientes)
            case "5":
                listar_pacientes(pacientes)
            case "0":
                break
            case _:
                print("Opción no válida")
