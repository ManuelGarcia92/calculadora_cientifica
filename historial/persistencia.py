import json
import os

CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))

CARPETA_RAIZ = os.path.dirname(CARPETA_ACTUAL)

DIRECTORIO_DATOS = os.path.join(CARPETA_RAIZ, "data")

def _garantizar_carpeta():
    if not os.path.exists(DIRECTORIO_DATOS):
        os.makedirs(DIRECTORIO_DATOS)

def cargar_historial(nombre_archivo="historial.json"):
    _garantizar_carpeta()
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    
def agregar_al_historial(expresion: str, resultado, nombre_archivo="historial.json"):
    historial = cargar_historial()
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    historial.append({
        "expresion": expresion,
        "resultado": resultado
    })
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4)

def eliminar_registro_historial(indice: int, nombre_archivo="historial.json") -> bool:
    historial = cargar_historial()
    if 1 <= indice <= len(historial):
        historial.pop(indice - 1)
        ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=4)
        return True
    return False 

def borrar_historial(nombre_archivo="historial.json") -> bool:
    ruta = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
    return True