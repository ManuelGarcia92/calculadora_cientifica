from lexer import Lexer 
from parser import Parser
from evaluacion import Evaluador, TablaDeSimbolos
from historial import agregar_al_historial
from interfaz import consola, formatear_tokens

def calculo() -> None:
    texto = ""
    memoria = TablaDeSimbolos()
    while True:
        consola.limpiar_terminal()
        consola.imprimir("Ingrese el comando [:break] para salir.")
        texto = consola.modificar_dato(">>> : ", texto)
        if texto.lower() == ":break":
            break
        if texto.strip() == "":
            continue
        try:
            texto = str(procesar_expresion(texto, memoria))
        except Exception as error:
            consola.imprimir(f"[Error de Ejecución]: {error}")     
        consola.pausa()

def procesar_expresion(texto: str, memoria: TablaDeSimbolos):
    lexer = Lexer(texto)
    tokens = lexer.tokenizar()
    parser = Parser(tokens)
    arbol = parser.parsear()
    evaluador = Evaluador(arbol)
    resultado = evaluador.evaluar(memoria)
    texto_formateado = formatear_tokens(tokens)
    if texto_formateado != str(resultado):   
        agregar_al_historial(texto_formateado, resultado)
    return resultado