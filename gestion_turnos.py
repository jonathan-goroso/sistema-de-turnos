from datetime import datetime


def menu_turnos() -> None:

    print("---------Menú de turnos---------")
    print("1- Registrar turno")
    print("2- Modificar turno")
    print("3- Cancelar turno")
    print("4- Consultar turno")
    print("5- Listar turnos")
    print("6- Consultar turnos de un paciente")
    print("7- Consultar disponibilidad de los turnos de un dia")
    print("0- Volver al menu principal\n")
    
def generar_id_turno(turnos: dict[str, list[str]]) -> str: 
    for numero in range(1, 10000):
        id_turno = str(numero).zfill(4)
        
        if id_turno not in turnos:
            return id_turno
        
    return None
            
    
def pedir_fecha() -> str:
    """
    Solicita una fecha valida con formato DD/MM/AAAA.
    
    Pre: None
    Post: Devuelve una fecha existente en el calendario, en forma de string.
    """
    while True:
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
        
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        
        except ValueError:
            print("Fecha invalida. Intente nuevamente.")
            
def horario_ocupado(turnos: dict[str, list[str]], fecha: str, hora: str, id_excluido: str = "") -> bool:
    """
    Indica si un horario esta ocupado en una fecha correspondiente.
    
    Pre:
    
    Post: Retorna un booleano. True si esta libre, False si no.
    """
    for id_turno, datos in turnos.items():
        if id_turno != id_excluido:
            if datos[1] == fecha and datos[2] == hora:
                return True
    
    return False

def registrar_turno(
    turnos: dict[str, list[str]],
    pacientes: dict[str, dict],
    horarios: list[str]
) -> None:
    """
    registra un nuevo turno al sistema

    pre:
    post: el turno queda registrado en el sistema
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return
    if len(horarios) == 0:
        print("No hay horarios disponibles en el sistema.")
        return

    dni = input("Ingrese el DNI del paciente: ")
    
    if dni not in pacientes:
        print("No existe un paciente registrado con ese DNI.")
        return
    
    fecha = pedir_fecha()
    
    print("Horarios disponibles para seleccionar: ")
    for hora in horarios:
        print(hora)
        
    hora = input("Ingrese el horario del turno: ")
    if hora not in horarios:
        print("El horario seleccionado no es valido.")
        return
    
    if horario_ocupado(turnos, fecha, hora) == True:
        print("El horario ya esta ocupado para esa fecha.")
        return
    
    id_turno = generar_id_turno(turnos)
    
    if id_turno is None:
        print("No quedan ID disponibles para registrar turnos.")
        return
    
    turnos[id_turno] = [dni, fecha, hora]
    
    print("Turno registrado correctamente.")
    print(f"ID del turno: {id_turno}")
    

def modificar_turno(
    turnos: dict[str, list[str]],
    pacientes: dict[str, dict],
    horarios: list[str]
) -> None:
    """
    Modifica un dato de un turno

    pre: El diccionario turno debe tener almenos un elemento
    post: Se modifica el dato seleccionado si es válido.
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return

    id_turno = input("Ingrese el ID del turno a modificar: ")
    if id_turno not in turnos:
        print("No existe un turno con el ID ingresado")
        return
    
    print("--- Dato a modificar ---")
    print("1- Paciente")
    print("2- Fecha")
    print("3- Horario")
    
    opcion = input("Seleccione una opción: ")
    
    match opcion:
        case "1":
            dni = input("Ingrese el DNI del nuevo paciente: ")
            
            if dni not in pacientes:
                print("No existe un paciente registrado con ese DNI.")
                return
            
            turnos[id_turno][0] = dni
            print("Paciente del turno modificado con éxito.")
            
        case "2":
            fecha = pedir_fecha()
            hora_actual = turnos[id_turno][2]
            
            if horario_ocupado(turnos, fecha, hora_actual, id_turno):
                print("Ese horario ya esta ocupado para esa fecha.")
                return
            
            turnos[id_turno][1] = fecha
            print("Fecha del turno modificada.")
            
        case "3":
            print("Horarios disponibles para seleccionar: ")
            for hora in horarios:
                print(hora)
                
            hora = input("Ingrese el nuevo horario: ")
            if hora not in horarios:
                print("El horario seleccionado no es válido.")
                return
            
            fecha_actual = turnos[id_turno][1]
            if horario_ocupado(turnos, fecha_actual, hora, id_turno):
                print("Ese horario ya esta ocupado para esa fecha.")
                return
            
            turnos[id_turno][2] = hora
            print("Horario del turno modificado.")
        
        case _:
            print("Opción no válida.")
            
def eliminar_turno(turnos: dict[str, list[str]]) -> None:
    """
    elimina un turno del sistema

    pre: El turno que se desea cancelar debe existir.
    post:elimina un turno del sistema
    """
    if len(turnos) == 0:
        print("No hay turnos registrados.")
        return
    
    id_turno = input("Ingrese el ID del turno a cancelar: ")
    if id_turno not in turnos:
        print("No existe un turno con ese ID.")
        return
    
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
        
    id_turno = input("Ingrese el ID del turno a consultar: ")
    
    if id_turno not in turnos: 
        print("No existe un turno con ese ID.")
        return
    
    datos = turnos[id_turno]
    
    print("--- Datos del turno ---")
    print(f"ID: {id_turno}")
    print(f"DNI del paciente: {datos[0]}")
    print(f"Fecha: {datos[1]}")
    print(f"Horario: {datos[2]}")
    print("-----------------------")
    


def listar_turnos(turnos: dict[int:list]) -> None:
    """
    Muestra todos los turnos registrados.

    pre: Debe existir un diccionario de turnos
    post: Muestra por pantalla todos los turnos
    """
    if len(turnos) == 0: 
        print("No hay turnos registrados.")
        return
    
    print("--- Listado de turnos ---")
    
    for id_turno, datos in turnos.items():
        print(f"ID: {id_turno}")
        print(f"DNI del paciente: {datos[0]}")
        print(f"Fecha: {datos[1]}")
        print(f"Horario: {datos[2]}\n")


def turnos_paciente(turnos: dict[int:list], pacientes: dict[str, dict]) -> None:
    """
    Muestra los tunos de un paciente

    pre:el diccionario turnos y paciente deben tener al menos un elemento
    post:muestra por pantalla los turnos del paciente
    """
    print("esta funcion permite mostrar todos los turnos de un paciente")


def disponibilidad_turnos(turnos: dict[int:list], horarios: list[str]) -> None:
    """
    muestra el estado de los turnos de un dia seleccionado

    pre:la lista horarios debe tener almenos un elemento
    post:muestra por pantalla el estado de os turnos del dia
    """
    print(
        "esta funcion muestra todos los turnos de un dia y dice si estan libres u ocupados"
    )


def gestionar_turnos(
    turnos: dict[str, list[str]], pacientes: dict[str, dict], horarios: list[str]
) -> None:
    while True:

        menu_turnos()

        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                registrar_turno(turnos, pacientes, horarios)
            case "2":
                modificar_turno(turnos, pacientes, horarios)
            case "3":
                eliminar_turno(turnos)
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
                print("opcion invalida")