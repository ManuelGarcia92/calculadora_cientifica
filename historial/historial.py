from interfaz import interfaz
from . import persistencia

def mostrar_historial() -> None:
    while True:
        interfaz.limpiar_terminal()
        interfaz.mostrar_titulo("Registro de operaciones.")
        registros = persistencia.cargar_historial()
        if registros:
            interfaz.mostrar_registro(registros)
            interfaz.imprimir("Ingrese el comando [:del  ] y el número de la operación para borrarla del historial.")
            interfaz.imprimir("Ingrese el comando [:clear] para borrar todo el historial.")
            interfaz.imprimir("Ingrese el comando [:break] para salir.")
        else:
            interfaz.imprimir("El historial esta vacío.")
            interfaz.pausa()
            break
        comando = interfaz.pedir_dato(">>> : ")
        if comando.lower() == ":break":
            break
        if comando:
            if not procesar_comando(comando):
                interfaz.imprimir_error(f"El comando [{comando}] no es válido.")
            interfaz.pausa()

def procesar_comando(texto: str) -> bool:
    entrada = texto.strip().lower()
    if entrada == ":clear":
        comando_clear()
        return True
            
    elif entrada.startswith(":del "):
        if comando_del(entrada):
            return True
        
    return False

def comando_clear() -> None:
    if interfaz.confirmacion("¿Borrar todo el historial?"):
        persistencia.borrar_historial()
        interfaz.imprimir("Historial eliminado con éxito.")
          
def comando_del(entrada) -> bool:
    partes = entrada.split()
    if len(partes) == 2 and partes[1].isdigit():
        num_registro = int(partes[1])
        if interfaz.confirmacion(f"¿Borrar el registro [{num_registro}]?"):
            if persistencia.eliminar_registro_historial(num_registro):
                interfaz.imprimir(f"Registro [{num_registro}] eliminado con éxito.")
                
            else:
                interfaz.imprimir_error(f"El registro [{num_registro}] no existe.")

        return True
        
    return False

