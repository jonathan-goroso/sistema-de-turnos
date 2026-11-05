#validaciones y auxiliares
from gestion_pacientes import pedir_dato_valido, validar_dni
from datetime import datetime
from tabulate import tabulate

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
    
    while True:
        hora = input(mensaje).strip()
        if hora == "0":
            return None
        if hora in horarios:
            return hora
        
        print("El horario seleccionado no es válido.")


def pedir_fecha(permitir_pasadas: bool = True) -> str:
    """
    Solicita una fecha valida con formato DD/MM/AAAA.
    
    Pre: permitir_pasados indica si se aceptan fechas anteriores a hoy.
    Post: Devuelve una fecha existente en el calendario, en forma de string. Agrega 0
    a la izquierda en caso de tener 1 solo digito, para asi quedar todas con el mismo formato.
    """
    while True:
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ").strip()
        
        try:
            fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")
            continue
        
        if not permitir_pasadas and fecha_valida.date() < datetime.today():
            print("La fecha no puede ser anterior a hoy.")
            continue
        
        return fecha_valida.strftime("%d/%m/%Y")
            
            
def pedir_dni_existente(pacientes: dict[str, dict]) -> str | None:
    """
    Función para usar cuando se requiere ver si hay paciente 
    registrado cuando se ingresa DNI.
    
    Pre: Recibe "pacientes", diccionario: {dni: {datos}}
    Post: Devuelve un string, el "dni". Si no existe, informa y
    devuelve None
    """
    dni = pedir_dato_valido("Ingresa el DNI del paciente: ", validar_dni,
                            "El numero de DNI ingresado no es válido (Intente sin puntos.)")
    
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

def horario_ocupado(turnos: dict[str, list[str]], fecha: str, hora: str, id_excluido: str = "") -> bool:
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
        
def mostrar_turnos(turnos: dict[str, list[str]], pacientes: dict[str, dict]) -> None:
    """
    Muestra por pantalla una tabla con los datos de los turnos recibidos.

    Arma una fila por turno con ID, DNI, nombre, fecah y horario
    y la imprime como tabla con encabezados.

    Pre: "turnos" es un diccionario con al menos un turno.

    Post: Se imprime la tabla con todos los turnos.
    """
    filas = []
    
    for id_turno, datos in turnos.items():
        dni = datos[0]
        
        if dni in pacientes:
            paciente = f"{pacientes[dni]['nombre']} {pacientes[dni]['apellido']}"

        filas.append([id_turno, dni, paciente, datos[1], datos[2]])
    encabezados = ["ID", "DNI", "Nombre y Apellido", "Fecha", "Horario"]
    print(
        tabulate(
            filas, headers=encabezados, tablefmt="simple_grid", disable_numparse=True
        )
    )
    
def ordenar_turnos(turnos: dict[str, list[str]]) -> dict[str, list[str]]:
    """
    Ordena los turnos por fecha y hora, del más próximo al más lejano.

    Pre: "turnos" es un diccionario {id: [dni, fecha, hora]}, con fecha
    DD/MM/AAAA y hora H:MM.
    Post: Devuelve un diccionario nuevo con los mismos turnos ordenados.
    No modifica "turnos".
    """
    lista = []
    for id_turno, datos in turnos.items():
        dia, mes, anio = datos[1].split("/")
        hora, minutos = datos[2].split(":")
        clave = (int(anio), int(mes), int(dia), int(hora), int(minutos))
        lista.append((clave, id_turno))

    lista.sort()

    ordenados = {}
    for clave, id_turno in lista:
        ordenados[id_turno] = turnos[id_turno]
    return ordenados