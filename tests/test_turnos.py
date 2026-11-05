#Para correr los test, uso el comanto python -m pytest -v

from gestion_turnos import registrar_turno, modificar_turno, eliminar_turno

PACIENTES = {
    "12345678": {
        "nombre": "Juan",
        "apellido": "Perez",
        "correo": "juan@gmail.com",
        "telefono": "1155558428",
    }
}
HORARIOS = ["9:00", "9:30", "10:00"]

def test_registrar_turno_sin_pacientes_devuelve_false():
    assert registrar_turno({}, {}, HORARIOS) == False

def test_registrar_turno_sin_horarios_devuelve_false():
    assert registrar_turno({}, PACIENTES, []) == False

def test_registrar_turno_sin_datos_no_agrega_turnos():
    turnos = {}
    registrar_turno(turnos, {}, HORARIOS)
    assert turnos == {}

def test_modificar_turno_sin_turnos_devuelve_false():
    assert modificar_turno({}, PACIENTES, HORARIOS) == False

def test_eliminar_turno_sin_turnos_devuelve_false():
    assert eliminar_turno({}) == False

