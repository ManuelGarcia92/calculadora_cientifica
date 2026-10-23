import persistencia
import consola

def historial() -> None:
    while True:
        consola.limpiar_terminal()
        consola.mostrar_titulo("Registro de operaciones.")
        historial = persistencia.cargar_historial()
        if historial:
            consola.mostrar_registro(historial)
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
                consola.imprimir_error(f"El comando {comando} no existe.")
            consola.pausa()

def procesar_comando(texto: str) -> bool:
    entrada = texto.strip().lower()
    if entrada == ":clear":
        comando_clear()
        return True
    
    if entrada.startswith(":del "):
        comando_del(entrada)
        return True
    
    return False

def comando_clear():
    persistencia.borrar_historial()
    consola.imprimir("Historial borrado con éxito.")

def comando_del(entrada):
    partes = entrada.split()
    if len(partes) == 2 and partes[1].isdigit():
        num_registro = int(partes[1])
        if persistencia.eliminar_registro_historial(num_registro):
            consola.imprimir(f"Registro [{num_registro}] eliminado.")
        else:
            consola.imprimir(f"El registro [{num_registro}] no existe.")



