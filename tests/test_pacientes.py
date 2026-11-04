from gestion_pacientes import (
    validar_dni,
    validar_nombre,
    validar_correo,
    validar_telefono,
)
from persistencia import leer_datos


# -------------validar DNI-------------------
def test_validar_dni_acepta_8_digitos():
    assert validar_dni("12345678") == True


def test_validar_dni_acepta_7_digitos():
    assert validar_dni("1234567") == True


def test_validar_dni_rechaza_6_digitos():
    assert validar_dni("123456") == False


def test_validar_dni_rechaza_9_digitos():
    assert validar_dni("123456789") == False


def test_validar_dni_rechaza_cero_inicial():
    assert validar_dni("02345678") == False


def test_validar_dni_rechaza_letras():
    assert validar_dni("12ABC678") == False


def test_validar_dni_rechaza_puntos():
    assert validar_dni("12.345.678") == False


def test_validar_dni_rechaza_cadena_vacia():
    assert validar_dni("") == False


def test_validar_dni_rechaza_espacios():
    assert validar_dni(" 12345678 ") == False


# -------------Validar nombres y apellidos-----------


def test_validar_nombre_acepta_nombre_simple():
    assert validar_nombre("Luis") == True


def test_validar_nombre_acepta_nombre_compuesto_y_con_tildes():
    assert validar_nombre("De la Torre")
    assert validar_nombre("José Luis") == True


def test_validar_nombre_acepta_apostrofe():
    assert validar_nombre("D'abundo") == True


def test_validar_nombre_acepta_dieresis():
    assert validar_nombre("Güemes") == True


def test_validar_nombre_acepta_enie():
    assert validar_nombre("Muñoz") == True


def test_validar_nombre_rechaza_cadena_vacia():
    assert validar_nombre("") == False


def test_validar_nombre_rechaza_numeros():
    assert validar_nombre("Carlos123") == False


def test_validar_nombre_rechaza_simbolos():
    assert validar_nombre("Ana@!#%") == False


def test_validar_nombre_rechaza_espacios_consecutivos():
    assert validar_nombre("José   Luis") == False


def test_validar_nombre_rechaza_guiones():
    assert validar_nombre("José-Luis") == False


# -------------valida correo electrónico--------------
def test_validar_correo_acepta_correo_habitual():
    assert validar_correo("juan@gmail.com") == True


def test_validar_correo_acepta_puntos_y_signo_mas_en_usuario():
    assert validar_correo("juan.perez+turnos@gmail.com") == True


def test_validar_correo_acepta_guion_en_dominio():
    assert validar_correo("juan@mi-dominio.com") == True


def test_validar_correo_acepta_subdominio():
    assert validar_correo("juan@consultorio.ejemplo.com") == True


def test_validar_correo_rechaza_cadena_vacia():
    assert validar_correo("") == False


def test_validar_correo_rechaza_sin_arroba():
    assert validar_correo("juangmail.com") == False


def test_validar_correo_rechaza_sin_usuario():
    assert validar_correo("@gmail.com") == False


def test_validar_correo_rechaza_sin_dominio():
    assert validar_correo("juan@") == False


def test_validar_correo_rechaza_sin_extension():
    assert validar_correo("juan@gmail") == False


def test_validar_correo_rechaza_extension_de_una_letra():
    assert validar_correo("juan@gmail.c") == False


def test_validar_correo_rechaza_espacios():
    assert validar_correo("jose luis@gmail.com") == False


def test_validar_correo_rechaza_puntos_consecutivos_en_dominio():
    assert validar_correo("juan@dominio..com") == False


def test_validar_correo_rechaza_dos_arrobas():
    assert validar_correo("juan@@gmail.com") == False


def test_validar_correo_rechaza_numeros_en_extension():
    assert validar_correo("juan@gmail.c1") == False


# ----------------validar teléfono-----------------


def test_validar_telefono_acepta_numero_habitual():
    assert validar_telefono("1155558482") == True


def test_validar_telefono_acepta_primer_digito_uno():
    assert validar_telefono("1123456789") == True


def test_validar_telefono_rechaza_9_digitos():
    assert validar_telefono("115555848") == False


def test_validar_telefono_rechaza_11_digitos():
    assert validar_telefono("11555584820") == False


def test_validar_telefono_rechaza_cero_inicial():
    assert validar_telefono("01155558482") == False


def test_validar_telefono_rechaza_letras():
    assert validar_telefono("1155ABcd82") == False


def test_validar_telefono_rechaza_guiones():
    assert validar_telefono("115555-842") == False


def test_validar_telefono_rechaza_espacios():
    assert validar_telefono("115555 8548") == False


def test_validar_telefono_rechaza_cadena_vacia():
    assert validar_telefono("") == False


# -------------lectura del archivo--------------
def test_leer_datos_devuelve_diccionario_vacio_si_el_archivo_no_existe():
    assert leer_datos("archivo_que_no_existe.json") == {}
