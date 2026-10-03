import json
import os

def ruta_actual(nombre_archivo):
    carpeta_actual = os.path.dirname(__file__)
    ruta_actual = os.path.join(carpeta_actual, nombre_archivo)
    return ruta_actual

DIRECTORIO_DATOS = ruta_actual("data")

def _garantizar_carpeta():
    if not os.path.exists(DIRECTORIO_DATOS):
        os.makedirs(DIRECTORIO_DATOS)
    
def guardar_memoria(variables: dict, nombre_archivo="memoria.json"):
    _garantizar_carpeta()
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(variables, f, indent=4)

def cargar_memoria(nombre_archivo="memoria.json") -> dict:
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    if not os.path.exists(ruta):
        return {}
    try:
        with open(ruta, "r", encoding="utf=8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def agregar_al_historial(expresion: str, resultado, nombre_archivo="historial.json"):
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    historial = cargar_historial()
    historial.append({
        "expresion": expresion,
        "resultado": resultado
    })
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4)

def cargar_historial(nombre_archivo="historial.json"):
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def borrar_historial(nombre_archivo="historial.json") -> bool:
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    _garantizar_carpeta()
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
    return True

def eliminar_registro_historial(indice: int, nombre_archivo="historial.json") -> bool:
    historial = cargar_historial(nombre_archivo)
    if 1 <= indice <= len(historial):
        historial.pop(indice - 1)
        ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=4)
        return True
    return False 