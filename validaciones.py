from datetime import datetime
import re


# validaciones y auxiliares
def pedir_horario(horarios: list[str], mensaje: str) -> str | None:
    """
    Muestra una lista de horarios y pide que se elija uno.

    Pre: recibe una lista de tr con al menos un horario y un mensaje.
    Post: Devuelve el horario elegido si está en la lista. Si no, imprime
    un mensaje.
    """
    print("Horarios disponibles para seleccionar: ")
    for hora in horarios:
        print(hora)

    hora = input(mensaje).strip()
    if hora not in horarios:
        print("El horario seleccionado no es válido.")
        return None
    return hora


def pedir_fecha() -> str:
    """
    Solicita una fecha valida con formato DD/MM/AAAA.

    Pre: None
    Post: Devuelve una fecha existente en el calendario, en forma de string. Agrega 0
    a la izquierda en caso de tener 1 solo digito, para asi quedar todas con el mismo formato.
    """
    while True:
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ").strip()

        try:
            fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")
            return fecha_valida.strftime("%d/%m/%Y")

        except ValueError:
            print("Fecha inválida. Intente nuevamente.")


def pedir_dni_existente(pacientes: dict[str, dict]) -> str | None:
    """
    Función para usar cuando se requiere ver si hay paciente
    registrado cuando se ingresa DNI.

    Pre: Recibe "pacientes", diccionario: {dni: {datos}}
    Post: Devuelve un string, el "dni". Si no existe, informa y
    devuelve None
    """
    dni = pedir_dato_valido(
        "Ingresa el DNI del paciente: ",
        validar_dni,
        "El numero de DNI ingresado no es válido (Intente sin puntos.)",
    )

    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return None
    return dni


def pedir_turno_existente(turnos: dict[str, list[str]], mensaje: str) -> str | None:
    """
    Solicita el ID de un turno, lo pasa a 4 dígitos y verifica si existe.

    Pre: Recibe "turnos", diccionario: {id: [dni, fecha, hora]} y un mensaje.
    Post: Devuelve un string, el ID. Si no existe, imprime un mensaje.
    """

    id_turno = input(mensaje).strip().zfill(4)
    if id_turno not in turnos:
        print("No existe un turno con ese ID.")
        return None
    return id_turno


def generar_id_turno(turnos: dict[str, list[str]]) -> str | None:
    """
    Genera el primer ID de turno, de 4 digitos(0001 a 9999).
    Recorre del 1 al 9999 y devuelve el primero, con ceros a la izquierda.

    Pre: Recibe como parametro un diccionario. Su clave son los IDs.
    Post: Devuelve un str de 4 dígitos, verificando que no esta en "turnos".
    """

    for numero in range(1, 10000):
        id_turno = str(numero).zfill(4)

        if id_turno not in turnos:
            return id_turno

    return None


def horario_ocupado(
    turnos: dict[str, list[str]], fecha: str, hora: str, id_excluido: str = ""
) -> bool:
    """
    Indica si un horario esta ocupado en una fecha correspondiente.

    Pre: Recibe un diccionario.

    Post: Retorna un booleano. False si esta libre, True si no.
    """
    for id_turno, datos in turnos.items():
        if id_turno != id_excluido:
            if datos[1] == fecha and datos[2] == hora:
                return True

    return False


def pedir_confirmacion(mensaje: str) -> bool:
    """
    Pregunta al usuario si si o no. Devuelve True si responde S
    y False si responde N.
    Repite la pregunta hasta recibir una respuesta válida.

    Pre: Recibe un string con la pregunta.
    Post: Devuelve booleano.
    """
    while True:
        respuesta = input(f"{mensaje} (S/N): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Respuesta inválida. Ingrese S o N.")


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
      por ejemplo ("12345678", validar_dni).

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
    - 'dni' debe ser un string.

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
    - 'nombre' debe ser un string.

    Postcondiciones:
    - Devuelve True si 'nombre' cumple el formato descrito.
    - Devuelve False en cualquier otro caso (vacío, números, símbolos, etc.)
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
    - 'correo' debe ser string.

    Postcondiciones:
    - Devuelve True si 'correo' tiene un usuario, una arroba, un dominio y una
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
    - 'telefono' debe ser un string.

    Postcondiciones:
    - Devuelve True si 'telefono' son 10 dígitos (0-9) y el primero no es 0.
    - Devuelve False en cualquier otro caso (vacío, letras, guiones, otra
      longitud, 0 inicial).
    - No se modifica 'telefono'.
    """
    patron_telefono = r"[1-9][0-9]{9}"
    return bool(re.fullmatch(patron_telefono, telefono))