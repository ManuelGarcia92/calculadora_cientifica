import consola
from persistencia import cargar_historial, agregar_al_historial
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
        print("Ingrese break para salir.")
        memoria.imprimir_memoria()

        texto = consola.pedir_dato(">>> : ")
        if texto.lower() == "break":
            break
        if not texto:
            continue

        try:
            ejecutar_linea(texto, memoria)
        except Exception as error:
            consola.mostrar_mensaje(f"[Error de Ejecución]: {error}")     
        consola.pausa()

def ver_historial() -> None:
    consola.limpiar_terminal()
    consola.mostrar_titulo("Registro de operaciones.")
    historial = cargar_historial()
    if historial:
        consola.mostrar_registro(historial)
    else:
        consola.mostrar_mensaje("El historial esta vacío")
    consola.pausa()
