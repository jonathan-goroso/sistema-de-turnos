from gestion_pacientes import gestionar_pacientes
from gestion_turnos import gestionar_turnos


# -------------menus----------------
def menu_principal() -> None:

    print("-----menu principal-----")
    print("1-gestionar pacientes")
    print("2-gestionar turnos")
    print("3-gestionar horarios")
    print("4-consultas")
    print("0-salir")
    print(" ")

    
def configurar_horarios() -> list[int]:
    """
    modifica el margen de horarios del sistema

    post:el nuevo margen es guardado en el sistema
    """
    print("esta funcion configura el margen de horarios disponible")


def main():

    horarios = ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00"]
    pacientes = {}
    # ejemplo de como seria: pacientes={dni:["nombre",edad,"correo"]}
    turnos = {}
    # ejemplo de como seria: turnos ={id:[dni,fecha,"hora"]}

    while True:
        menu_principal()
        opcion = input("elija una opcion: ")

        match opcion:
            case "1":
                gestionar_pacientes(pacientes)
            case "2":
                gestionar_turnos(turnos, pacientes, horarios)
            case "3":
                horarios = configurar_horarios()
            case "0":
                break
            case _:
                print("opcion invalida")


if __name__ == "__main__":
    main()
