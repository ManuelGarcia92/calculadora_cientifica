from entorno import TablaDeSimbolos
from lexer import Lexer 
from parser import Parser
from evaluador import Evaluador
import persistencia
import consola

def calculo() -> None:
    texto = ""
    memoria = TablaDeSimbolos()
    while True:
        consola.limpiar_terminal()
        consola.imprimir("Ingrese el comando [:break] para salir.")
        texto = consola.modificar_dato(">>> : ", texto)
        if texto.lower() == ":break":
            break
        if not texto:
            continue
        try:
            texto = str(procesar_calculo(texto, memoria))
        except Exception as error:
            consola.imprimir(f"[Error de Ejecución]: {error}.")     
        consola.pausa()

def procesar_calculo(texto: str, memoria: TablaDeSimbolos):
    lexer = Lexer(texto)
    tokens = lexer.tokenizar()
    parser = Parser(tokens)
    arbol = parser.parsear()
    if arbol:
        evaluador = Evaluador(arbol)
        resultado = evaluador.evaluar(memoria)
        if resultado is not None:
            texto_formateado = lexer.formatear_tokens(tokens)
            if texto_formateado != str(resultado):   
                persistencia.agregar_al_historial(texto_formateado, resultado)
            return resultado