
def menu_pacientes() -> None:

    print("---------menu de pacientes-------")
    print("1-registrar paciente")
    print("2-modificar paciente")
    print("3-dar de baja a un paciente")
    print("4-consultar paciente")
    print("5-listar pacientes")
    print("0-volver al menu principal")
    print(" ")

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
