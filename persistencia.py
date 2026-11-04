import json


def leer_datos(nombre_archivo: str) -> dict:
    """
    Lee un archivo JSON y devuelve su contenido como diccionario.

    Contrato:
    - Abre 'nombre_archivo', lo deserializa y devuelve el diccionario.
    - Si el archivo no existe (por ejemplo, la primera vez que se usa el
      sistema), se considera que todavía no hay datos y devuelve un diccionario vacío.

    Precondiciones:
    - 'nombre_archivo' es un string con el nombre (o ruta) de un archivo JSON.

    Postcondiciones:
    - Devuelve el diccionario guardado en el archivo, o {} si no existe.
    - No modifica el archivo.
    """
    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}


def guardar_datos(nombre_archivo: str, datos: dict) -> None:
    """
    Guarda un diccionario completo en un archivo JSON.

    Contrato:
    - Serializa datos y reescribe 'nombre_archivo' con ese contenido
      (crea el archivo si no existe).

    Precondiciones:
    - 'nombre_archivo' es un string con el nombre (o ruta) de un archivo JSON.
    - 'datos' es un diccionario cuyas claves son str y cuyos valores pueden
      convertirse a JSON.

    Postcondiciones:
    - Si se pudo escribir, el archivo contiene exactamente datos e informa
      que se guardaron.
    - Si no se pudo escribir (sin permisos, ruta inexistente, etc.), informa
      el error y el archivo no se considera actualizado.
    - No modifica datos.
    """
    try:
        with open(nombre_archivo, "wt", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"No se pudieron guardar los datos: {error}")
    else:
        print(f"Datos guardados con éxito.")
