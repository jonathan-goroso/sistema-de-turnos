from persistencia import guardar_datos
from validaciones import (
    pedir_horario,
    pedir_fecha,
    pedir_dni_existente,
    pedir_turno_existente,
    generar_id_turno,
    horario_ocupado,
    pedir_confirmacion,
    pedir_dato_valido,
    validar_dni,
)


def menu_turnos() -> None:
    """
    Muestra por pantalla las opciones disponibles del menú de turnos

    Pre: None
    Post: Imprime las opciones en pantalla.
    """
    print("---------Menú de turnos---------") 
    opciones = {
        "1": "Registrar turno",
        "2": "Modificar turno",
        "3": "Cancelar turno",
        "4": "Consultar turno",
        "5": "Listar turnos",
        "6": "Consultar turnos de un paciente",
        "7": "Consultar disponibilidad de los turnos de un día",
        "0": "volver al menú principal"
    }
    for clave, valor in opciones.items():
        print(f"{clave}-{valor}")
    print()


def registrar_turno(
    turnos: dict[str, list[str]], pacientes: dict[str, dict], horarios: list[str]
) -> bool:
    """
    registra un nuevo turno al sistema

    Pre: Recibe "turnos", diccionario: {id: [dni, fecha, hora]}
    "pacientes", diccionario: {dni: {datos}}
    "horarios" es una lista con elementos string

    Post: Si pasa por todos los datos correctamente, el turno queda registrado en
    el sistema. Devuelve un booleano para actualizar el JSON.
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return False
    if len(horarios) == 0:
        print("No hay horarios disponibles en el sistema.")
        return False

    dni = pedir_dni_existente(pacientes)
    if dni is None:
        return False
    
    fecha = pedir_fecha(permitir_pasadas = False)
        
    hora = pedir_horario(horarios, "Ingrese el horario del turno: ")
    if hora is None:
        return False
    
    if horario_ocupado(turnos, fecha, hora):
        print("El horario ya esta ocupado para esa fecha.")
        return False

    id_turno = generar_id_turno(turnos)

    if id_turno is None:
        print("No quedan ID disponibles para registrar turnos.")
        return False

    turnos[id_turno] = [dni, fecha, hora]

    print("Turno registrado correctamente.")
    print(f"ID del turno: {id_turno}")
    return True


def modificar_turno(
    turnos: dict[str, list[str]], pacientes: dict[str, dict], horarios: list[str]
) -> bool:
    """
    Modifica un dato de un turno

    Pre: Recibe "turnos", diccionario: {id: [dni, fecha, hora]}
    "pacientes", diccionario: {dni: {datos}}
    "horarios" es una lista con elementos string

    Post: Se modifica el dato seleccionado si es válido. Devuelve un booleano para actualizar el JSON. 
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return False

    id_turno = pedir_turno_existente(turnos,"Ingrese el ID del turno a modificar: ")
    if id_turno is None:
        return False

    print("--- Dato a modificar ---")
    print("1- Paciente")
    print("2- Fecha")
    print("3- Horario\n")
    
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            dni = pedir_dni_existente(pacientes)
            if dni is None:
                return False

            turnos[id_turno][0] = dni
            print("Paciente del turno modificado con éxito.")
            return True

        case "2":
            fecha = pedir_fecha(permitir_pasadas = False)
            hora_actual = turnos[id_turno][2]

            if horario_ocupado(turnos, fecha, hora_actual, id_turno):
                print("Ese horario ya esta ocupado para esa fecha.")
                return False

            turnos[id_turno][1] = fecha
            print("Fecha del turno modificada.")
            return True

        case "3":
            hora = pedir_horario(horarios, "Ingrese el nuevo horario: ")
            if hora is None:
                return False
            if hora is None:
                return False
            
            fecha_actual = turnos[id_turno][1]
            if horario_ocupado(turnos, fecha_actual, hora, id_turno):
                print("Ese horario ya esta ocupado para esa fecha.")
                return False

            turnos[id_turno][2] = hora
            print("Horario del turno modificado.")
            return True

        case _:
            print("Opción no válida.")
            return False
            
def eliminar_turno(turnos: dict[str, list[str]]) -> bool:
    """
    Elimina un turno del sistema

    Pre: Recibe "turnos", diccionario. El turno que se desea cancelar debe existir.
    Post: Devuelve un booleano, que define que se actualizce el JSON.
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return False
    
    id_turno = pedir_turno_existente(turnos, "Ingrese el ID del turno a cancelar: ")
    if id_turno is None:
        return False
    
    if not pedir_confirmacion(f"¿Está seguro que desea cancelar el turno {id_turno}?"):
        print("Operación cancelada.")
        return False

    del turnos[id_turno]
    print("Turno cancelado con éxito.")
    return True
    return True


def consultar_turno(turnos: dict[str, list[str]], pacientes: dict[str, dict]) -> None:
    """
    Muestra los datos de un turno.

    pre: El diccionario turnos debe tener al menos un elemento, el turno
    que se desea consultar debe existir.

    post: muestra por pantalla el turno consultado
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return

    id_turno = pedir_turno_existente(turnos, "Ingrese el ID del turno a consultar: ")
    if id_turno is None: 
        return 
    
    datos = turnos[id_turno]

    print("--- Datos del turno ---")
    mostrar_turnos({id_turno: turnos[id_turno]}, pacientes)

def listar_turnos(turnos: dict[str, list[str]], pacientes: dict[str, dict]) -> None:
    """
    Muestra todos los turnos registrados. Con sus datos correspondientes.

    Pre: Recibe "turnos", diccionario {id: [dni, fecha, hora]}
    y "pacientes", diccionario.
    Post: Muestra por pantalla todos los turnos, ordenados cronologicamente.
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return

    print("--- Listado de turnos ---")
    mostrar_turnos(ordenar_turnos(turnos), pacientes)
    
def turnos_paciente(turnos: dict[str, list[str]], pacientes: dict[str, dict]) -> None:
    """
    Solicita el DNI de un paciente, y si existe muestra sus turnos.

    Pre: Recibe "turnos", diccionario: {id: [dni, fecha, hora]}
    "pacientes", diccionario: {dni: {datos}}

    Post: En caso del paciente tener turnos, se imprimen en pantalla.
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados")
        return
    
    dni = pedir_dni_existente(pacientes)
    if dni is None:
        return
    
    turnos_del_paciente = {}
    for id_turno, datos in turnos.items():
        if datos[0] == dni:
            turnos_del_paciente[id_turno] = datos
    
    if len(turnos_del_paciente) == 0:
        print("El paciente no tiene turnos registrados.")
        return
            
    print(f"--- Turnos del paciente: {dni} ---")
    mostrar_turnos(turnos_del_paciente, pacientes)
    
def disponibilidad_turnos(turnos: dict[str, list[str]], horarios: list[str]) -> None:
    """
    Muestra el estado de los turnos de un dia seleccionado.

    Pre: Recibe "turnos", diccionario: {id: [dni, fecha, hora]}
    "horarios" es una lista con elementos string.

    Post: Imprime en pantalla el estado de los turnos del día seleccionado.
    """
    if len(horarios) == 0:
        print("No hay horarios disponibles en el sistema.")
        return

    fecha = pedir_fecha()

    print(f"--- Disponibilidad del día {fecha} ---")
    for hora in horarios:
        if horario_ocupado(turnos, fecha, hora):
            estado = "Ocupado"
        else:
            estado = "Libre"
        print(f"{hora} - {estado}")


def gestionar_turnos(
    turnos: dict[str, list[str]],
    pacientes: dict[str, dict],
    horarios: list[str],
    archivo: str,
) -> None:
    """
    Muestra el menú de turnos y accede a cada opción a su función correspondiente.
    Se repite el menú hasta que el usuario seleccione 0. Si una opción que
    modifica turnos se completa con éxito, guarda "turnos" en "archivo".

    Pre; Recibe "turnos", diccionario: {id: [dni, fecha, hora]}
    "pacientes", diccionario: {dni: {datos}}
    "horarios" es una lista con elementos string
    "archivo" es el nombre del JSON donde se guardan los turnos.

    Post: Al terminar, "archivo" guarda los turnos acorde a la última
    modificación
    """

    while True:

        menu_turnos()
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                if registrar_turno(turnos, pacientes, horarios):
                    guardar_datos(archivo, turnos)
            case "2":
                if modificar_turno(turnos, pacientes, horarios):
                    guardar_datos(archivo, turnos)
            case "3":
                if eliminar_turno(turnos):
                    guardar_datos(archivo, turnos)
            case "4":
                consultar_turno(turnos, pacientes)
            case "5":
                listar_turnos(turnos, pacientes)
            case "6":
                turnos_paciente(turnos, pacientes)
            case "7":
                disponibilidad_turnos(turnos, horarios)
            case "0":
                break
            case _:
                print("Opción inválida")