# -------------menus----------------
def menu_principal() -> None:

    print("-----menu principal-----")
    print("1-gestionar pacientes")
    print("2-gestionar turnos")
    print("3-gestionar horarios")
    print("4-consultas")
    print("0-salir")
    print(" ")


def menu_pacientes() -> None:

    print("---------menu de pacientes-------")
    print("1-registrar paciente")
    print("2-modificar paciente")
    print("3-dar de baja a un paciente")
    print("4-consultar paciente")
    print("5-listar pacientes")
    print("0-volver al menu principal")
    print(" ")


def menu_turnos() -> None:

    print("---------menu de turnos---------")
    print("1-registrar turno")
    print("2-modificar turno")
    print("3-cancelar turno")
    print("4-consultar turno")
    print("5-listar turnos")
    print("6-consultar turnos de un paciente")
    print("7-consultar disponibilidad de los turnos de un dia")
    print("0-volver al menu principal")
    print(" ")


# -----------gestion de pacientes-------------
def registrar_paciente(pacientes: dict[int:list]) -> None:
    """
    registra un nuevo paciente al sistema

    pre:
    post: el paciente queda registrado en el sistema
    """
    print("esta funcion permite registrar a un nuevo paciente")


def modificar_paciente(pacientes: dict[int:list]) -> None:
    """
    modica un dato del paciente

    pre: el diccionario debe terner almenos un elemento
    post: los datos del pacientes son modificados
    """
    print("esta funcion permite modifica un dato del paciente")


def eliminar_paciente(pacientes: dict[int:list]) -> None:
    """
    elimina a un paciete del sistema

    pre: el diccionario debe tener almenos un elemento
    post: el paciente es eliminado del sistema
    """
    print("esta funcion da de baja a un paciente del sistema")


def consultar_paciente(pacientes: dict[int:list]) -> None:
    """
    muestra los datos de un paciente

    pre: el diccionario debe tener almenos un elemento
    post:muestra por pantalla los datos del paciente
    """
    print("permite consultar los datos de un paciente")


def listar_pacientes(pacientes: dict[int:list]) -> None:
    """
    muestra a todos los pacientes del sistema

    pre: el diccionario debe tener almenos un elemento
    post: muestra por pantalla a toos los pacientes
    """
    print("lista a todos los pacientes del sistema")


def gestionar_pacientes(pacientes: dict[int:list]) -> None:
    while True:

        menu_pacientes()

        opcion = input("elija una opcion: ")

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
                print("opcion invalida")


# ---------------gestion de turnos--------------


def registrar_turno(
    turnos: dict[int:list], pacientes: dict[int:list], horarios: list[str]
) -> None:
    """
    registra un nuevo turno al sistema

    pre:
    post: el turno queda registrado en el sistema
    """
    print("esta funcion registra un nuevo turno al sistema")


def modificar_turno(
    turnos: dict[int:list], pacientes: dict[int:list], horarios: list[str]
) -> None:
    """
    modifica un dato de un turno

    pre: el diccionario turno debe tener almenos un elemento
    post: los datos del turno queda modificado
    """
    print("esta funcion permite modificar un dato de un turno")


def eliminar_turno(turnos: dict[int:list]) -> None:
    """
    elimina un turno del sistema

    pre:el diccionario turnos debe tener almenos un elemento
    post:elimina un turno del sistema
    """
    print("esta funcion permite cancelar un turno del sistema")


def consultar_turno(turnos: dict[int:list]) -> None:
    """
    muestra el turno consultado

    pre:el diccionario turnos debe tener almenos un elemento
    post: muestra por pantalla el turno consultado
    """
    print("esta funcion permite buscar un turno")


def listar_turnos(turnos: dict[int:list]) -> None:
    """
    muestra todos los turno del sistema

    pre:el diccionario turnos debe tener almenos un elemento
    post: muestra por pantalla todos los turnos
    """
    print("esta funcion muestra todos los turnos del sistema")


def turnos_paciente(turnos: dict[int:list], pacientes: dict[int:list]) -> None:
    """
    muestra los tunos de un paciente

    pre:el diccionario turnos y paciente deben tener almenos un elemento
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
    turnos: dict[int:list[int,int,str]], pacientes: dict[int:list[str,int,str]], horarios: list[str]
) -> None:
    while True:

        menu_turnos()

        opcion = input("elija una opcion: ")

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


# ------------gestion de horarios-------------


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
