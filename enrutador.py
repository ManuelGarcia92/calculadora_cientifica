import consola
from persistencia import cargar_historial, agregar_al_historial, borrar_historial, eliminar_registro_historial
from entorno import TablaDeSimbolos
from lexer import Lexer 
from parser import Parser
from evaluador import Evaluador

def ejecutar_linea(texto: str, memoria: TablaDeSimbolos):
    lexer = Lexer(texto)
    tokens = lexer.tokenizar()
    parser = Parser(tokens)
    arbol = parser.parsear()

    if arbol:
        evaluador = Evaluador(arbol)
        resultado = evaluador.evaluar(memoria)
        if resultado is not None:
            texto_formateado = consola.formatear_texto(tokens)
            agregar_al_historial(texto_formateado, resultado)
            print(resultado) 

def calculo() -> None:
    memoria = TablaDeSimbolos()
    while True:
        consola.limpiar_terminal()
        print("Ingrese el comando [break] para salir.")
        memoria.imprimir_memoria()

        texto = consola.pedir_dato(">>> : ")
        if texto.lower() == "break":
            break
        if not texto:
            continue

        try:
            ejecutar_linea(texto, memoria)
        except Exception as error:
            consola.mostrar_mensaje(f"[Error de Ejecución]: {error}.")     
        consola.pausa()

def procesar_comando_historial(texto: str) -> bool:
    entrada = texto.strip().lower()
    if entrada == "clear":
        borrar_historial()
        print("Historial borrado con éxito.")
        return True
    
    if entrada.startswith("del "):
        partes = entrada.split()
        if len(partes) == 2 and partes[1].isdigit():
            num_registro = int(partes[1])
            if eliminar_registro_historial(num_registro):
                print(f"Registro [{num_registro}] eliminado.")
            else:
                print(f"El registro [{num_registro}] no existe.")
            return True
        return False
    
def ver_historial() -> None:
    while True:
        consola.limpiar_terminal()
        consola.mostrar_titulo("Registro de operaciones.")
        historial = cargar_historial()
        if historial:
            consola.mostrar_registro(historial)
            print("Ingrese el comando [del] y el número de la operación para borrarla del historial.")
            print("Ingrese el comando [clear] si desea borrar todo el historial.")
            print("Ingrese el comando [break] para salir.")
        else:
            consola.mostrar_mensaje("El historial esta vacío.")
            consola.pausa()
            break
        comando = consola.pedir_dato(">>> : ")
        if comando.lower() == "break":
            break
        if comando:
            if not procesar_comando_historial(comando):
                consola.mostrar_error(f"El comando {comando} no existe.")
            consola.pausa()
