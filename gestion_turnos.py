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
