
from gestion_pacientes import pedir_dato_valido, validar_dni
from persistencia import guardar_datos
from validaciones import pedir_horario, pedir_fecha, pedir_dni_existente, pedir_turno_existente, generar_id_turno, horario_ocupado, pedir_confirmacion

def menu_turnos() -> None:
    """
    Muestra por pantalla las opciones disponibles del menú de turnos
    
    Pre: None
    Post: Imprime las opciones en pantalla.
    """
    print("---------Menú de turnos---------")
    print("1- Registrar turno")
    print("2- Modificar turno")
    print("3- Cancelar turno")
    print("4- Consultar turno")
    print("5- Listar turnos")
    print("6- Consultar turnos de un paciente")
    print("7- Consultar disponibilidad de los turnos de un dia")
    print("0- Volver al menu principal\n")
    
def registrar_turno(
    turnos: dict[str, list[str]],
    pacientes: dict[str, dict],
    horarios: list[str]
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

    dni = pedir_dato_valido("Ingrese el DNI del paciente: ", validar_dni, "El DNI ingresado no es válido.")
    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return False
    
    fecha = pedir_fecha()
    
    print("Horarios disponibles para seleccionar: ")
    for hora in horarios:
        print(hora)
        
    hora = pedir_horario(horarios, "Ingrese el horario del turno: ")
    
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
    turnos: dict[str, list[str]],
    pacientes: dict[str, dict],
    horarios: list[str]
) -> bool:
    """
    Modifica un dato de un turno

    pre: Recibe "turnos", diccionario: {id: [dni, fecha, hora]}
    "pacientes", diccionario: {dni: {datos}}
    "horarios" es una lista con elementos string

    post: Se modifica el dato seleccionado si es válido. Devuelve un booleano para actualizar el JSON. 
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return False

    id_turno = pedir_turno_existente(turnos,"Ingrese el ID del turno a modificar.")
    if id_turno is None:
        return False
    
    print("--- Dato a modificar ---")
    print("1- Paciente")
    print("2- Fecha")
    print(f"3- Horario\n")
    
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
            fecha = pedir_fecha()
            hora_actual = turnos[id_turno][2]
            
            if horario_ocupado(turnos, fecha, hora_actual, id_turno):
                print("Ese horario ya esta ocupado para esa fecha.")
                return False
            
            turnos[id_turno][1] = fecha
            print("Fecha del turno modificada.")
            return True
            
        case "3":
            print("Horarios disponibles para seleccionar: ")
            for hora in horarios:
                print(hora)
                
            hora = pedir_horario(horarios, "Ingrese el nuevo horario: ")
            
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
            
def eliminar_turno(turnos: dict[str, list[str]]) -> None:
    """
    elimina un turno del sistema

    pre: El turno que se desea cancelar debe existir.
    post:elimina un turno del sistema
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return
    
    id_turno = pedir_turno_existente(turnos, "Ingrese el ID del turno a cancelar: ")
    if id_turno is None:
        return False
    
    if not pedir_confirmacion("Está seguro que desea cancelar el turno: "):
        print("Cancelación cancelada.")
        return False
    
    del turnos[id_turno]
    print("Turno cancelado con éxito.")


def consultar_turno(turnos: dict[str, list[str]]) -> None:
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
        return False
    
    datos = turnos[id_turno]
    
    print("--- Datos del turno ---")
    print(f"ID: {id_turno} | DNI del paciente: {datos[0]} | Fecha: {datos[1]} | Horario: {datos[2]}")

def listar_turnos(turnos: dict[str, list[str]]) -> None:
    """
    Muestra todos los turnos registrados. Con sus datos correspondientes.

    Pre: Recibe "turnos", diccionario {id: [dni, fecha, hora]}
    Post: Muestra por pantalla todos los turnos
    """
    if len(turnos) == 0: 
        print("No hay turnos registrados.")
        return
    
    print("--- Listado de turnos ---")
    
    for id_turno, datos in turnos.items():
        print(f"ID: {id_turno} | DNI del paciente: {datos[0]} | Fecha: {datos[1]} | Horario: {datos[2]}\n")
        
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
    
    dni = pedir_dato_valido("Ingrese el DNI del paciente: ", validar_dni, "El DNI no es válido.")
    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return
    
    print(f"--- Turnos del paciente: {dni} ---")
    
    encontrados = 0
    for id_turno, datos in turnos.items():
        if datos[0] == dni:
            print(f"ID: {id_turno} | Fecha: {datos[1]} | Horario: {datos[2]}")
            encontrados += 1
            
    if encontrados == 0: 
        print("El paciente no tiene turnos registrados.")

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
    archivo: str) -> None:
    """
    Muestra el menú de turnos y accede a cada opcion a su función correspondiente.
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
                consultar_turno(turnos)
            case "5":
                listar_turnos(turnos)
            case "6":
                turnos_paciente(turnos, pacientes)
            case "7":
                disponibilidad_turnos(turnos, horarios)
            case "0":
                break
            case _:
                print("Opción inválida")