from gestion_pacientes import gestionar_pacientes
from gestion_turnos import gestionar_turnos
from persistencia import leer_datos

ARCHIVO_PACIENTES = "data/pacientes.json"
ARCHIVO_TURNOS = "data/turnos.json"


# -------------menus----------------
def mostrar_menu_principal() -> None:
    """
    Muestra por pantalla las opciones disponibles del menú principal del sistema.

    Contrato:
    - Imprime en consola la lista numerada de opciones del sistema (del 1 al 4
      y la opción 0 para salir) seguida de una línea en blanco.

    Precondiciones:
    - Ninguna, No recibe parámetros.

    Postcondiciones:
    - Imprime las opciones en pantalla y una línea vacía al final.
    - No solicita datos por teclado, no retorna ningún valor y no modifica
      el estado del sistema.
    """
    opciones = {
        "1": "Gestionar pacientes",
        "2": "Gestionar turnos",
        "3": "Gestionar horarios",
        "4": "Consultas",
        "0": "Salir del programa",
    }
    for clave, valor in opciones.items():
        print(f"{clave}-{valor}")
    print()


def configurar_horarios() -> list[str]:
    """
    modifica el margen de horarios del sistema

    Contrato:
    - Solicita por teclado la hora de inicio y la hora de fin de la atención
      (valores numéricos enteros).
    - Genera y retorna una lista de horarios en intervalos de 30 minutos desde
      la hora de inicio hasta la hora de fin inclusive (en formato "H:00" y "H:30").

    Pre:
    - Ninguna, no recibe parámetros.

    post:
    - Devuelve una lista de strings con los horarios generados en intervalos de 30 min.
    - el nuevo margen es guardado en el sistema
    """

    comienzo = int(input("Ingrese a que hora empieza a atender: "))
    fin = int(input("Ingrese hasta que hora atiende: "))

    horarios = []
    for i in range(comienzo, fin):
        horarios.append(str(i) + ":00")
        horarios.append(str(i) + ":30")

    horarios.append(str(fin) + ":00")

    return horarios


def main() -> None:
    """
    Programa principal del sistema de turnos.

    Contrato:
    - Inicializa los horarios base y carga los datos existentes de pacientes y
      turnos desde sus respectivos archivos JSON.
    - Ejecuta un ciclo iterativo que muestra el menú principal y deriva el control
      al módulo correspondiente según la opción seleccionada (pacientes, turnos
      o configuración de horarios).
    - Finaliza la ejecución del programa cuando el usuario ingresa la opción "0".

    Precondiciones:
    - Ninguna. No recibe parámetros.

    Postcondiciones:
    - El programa finaliza limpiamente cuando el usuario elige salir ("0").
    - No retorna ningún valor.
    - Delega las modificaciones de datos y su persistencia en disco a los módulos
      correspondientes durante la ejecución.
    """
    horarios = ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00"]
    pacientes = leer_datos(ARCHIVO_PACIENTES)
    """
    ejemplo de como seria:
    pacientes = {
        "dni": {
            "nombre": "juan",
            "apellido": "Pérez",
            "correo": "juan@gmail.com",
            "telefono": "1155558428",
        }
    }
    """
    turnos = leer_datos(ARCHIVO_TURNOS)
    # ejemplo de como seria: turnos ={id:[dni,fecha,"hora"]}

    while True:
        print("-----menu principal-----")
        mostrar_menu_principal()
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                gestionar_pacientes(pacientes, ARCHIVO_PACIENTES)
                print()
            case "2":
                gestionar_turnos(turnos, pacientes, horarios, ARCHIVO_TURNOS)
                print()
            case "3":
                horarios = configurar_horarios()
                print(horarios)
                print()
            case "0":
                break
            case _:
                print("opción no válida")


if __name__ == "__main__":
    main()
