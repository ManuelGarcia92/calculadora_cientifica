from extras import limpiar_terminal, pausa
from entorno import TablaDeSimbolos
from lexer import Lexer 
from parser import Parser
from evaluador import Evaluador

def main() -> None:
    memoria = TablaDeSimbolos()

    while True:
        limpiar_terminal()
        print("Ingrese break para salir.")
        memoria.imprimir_memoria()
        texto = input(">>> : ").strip()
        if texto.lower() == "break":
            break
        if not texto:
            continue
        try:
            lexer = Lexer(texto)
            tokens = lexer.tokenizar()
            parser = Parser(tokens)
            arbol = parser.parsear()
            if arbol:
                evaluador = Evaluador(arbol)
                resultado = evaluador.evaluar(memoria)
                if resultado is not None:
                    print(resultado)
        except Exception as error:
            print(f"\n[Error de Ejecución]: {error}")     

        pausa()
        
if __name__ == "__main__":
    main()