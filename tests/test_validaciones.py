#Para correr los test, uso el comanto python -m pytest -v

from validaciones import generar_id_turno, horario_ocupado, ordenar_turnos


def test_generar_id_con_diccionario_vacio():
    assert generar_id_turno({}) == "0001"

def test_generar_id_devuelve_el_siguiente():
    turnos = {"0001": ["12345678", "01/01/2099", "9:00"]}
    assert generar_id_turno(turnos) == "0002"

def test_generar_id_reutiliza_id_libre():
    turnos = {
        "0001": ["12345678", "01/01/2099", "9:00"],
        "0003": ["12345678", "01/01/2099", "10:00"],
    }
    assert generar_id_turno(turnos) == "0002"

def test_horario_ocupado_misma_fecha_y_hora():
    turnos = {"0001": ["12345678", "01/01/2099", "9:00"]}
    assert horario_ocupado(turnos, "01/01/2099", "9:00") == True

def test_horario_libre_con_otra_hora():
    turnos = {"0001": ["12345678", "01/01/2099", "9:00"]}
    assert horario_ocupado(turnos, "01/01/2099", "9:30") == False

def test_horario_libre_con_otra_fecha():
    turnos = {"0001": ["12345678", "01/01/2099", "9:00"]}
    assert horario_ocupado(turnos, "02/01/2099", "9:00") == False

def test_horario_libre_con_diccionario_vacio():
    assert horario_ocupado({}, "01/01/2099", "9:00") == False

def test_horario_ocupado_ignora_el_turno_excluido():
    turnos = {"0001": ["12345678", "01/01/2099", "9:00"]}
    assert horario_ocupado(turnos, "01/01/2099", "9:00", "0001") == False

def test_ordenar_turnos_por_fecha():
    turnos = {
        "0001": ["12345678", "02/01/2026", "9:00"],
        "0002": ["12345678", "01/12/2025", "9:00"],
    }
    assert list(ordenar_turnos(turnos)) == ["0002", "0001"]

def test_ordenar_turnos_por_hora_en_el_mismo_dia():
    turnos = {
        "0001": ["12345678", "01/01/2026", "10:00"],
        "0002": ["12345678", "01/01/2026", "9:00"],
    }
    assert list(ordenar_turnos(turnos)) == ["0002", "0001"]