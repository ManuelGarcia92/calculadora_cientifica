from interfaz import consola
from . import persistencia

def mostrar_historial() -> None:
    while True:
        consola.limpiar_terminal()
        consola.mostrar_titulo("Registro de operaciones.")
        registros = persistencia.cargar_historial()
        if registros:
            consola.mostrar_registro(registros)
            consola.imprimir("Ingrese el comando [:del  ] y el número de la operación para borrarla del historial.")
            consola.imprimir("Ingrese el comando [:clear] para borrar todo el historial.")
            consola.imprimir("Ingrese el comando [:break] para salir.")
        else:
            consola.imprimir("El historial esta vacío.")
            consola.pausa()
            break
        comando = consola.pedir_dato(">>> : ")
        if comando.lower() == ":break":
            break
        if comando:
            if not procesar_comando(comando):
                consola.imprimir_error(f"El comando [{comando}] no es válido.")
            consola.pausa()

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
    if consola.confirmacion("¿Borrar todo el historial?"):
        persistencia.borrar_historial()
        consola.imprimir("Historial eliminado con éxito.")
          
def comando_del(entrada) -> bool:
    partes = entrada.split()
    if len(partes) == 2 and partes[1].isdigit():
        num_registro = int(partes[1])
        if consola.confirmacion(f"¿Borrar el registro [{num_registro}]?"):
            if persistencia.eliminar_registro_historial(num_registro):
                consola.imprimir(f"Registro [{num_registro}] eliminado con éxito.")
                
            else:
                consola.imprimir_error(f"El registro [{num_registro}] no existe.")

        return True
        
    return False

