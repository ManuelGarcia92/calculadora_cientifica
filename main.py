from extras import limpiar_terminal, pausa
from lexer import Lexer 
from parser import Parser

def main() -> None:
    while True:
        limpiar_terminal()
        print("[Ingrese break para salir]")
        texto = input(">>> : ")
        if texto == "break":
            break
        try:
            lexer = Lexer(texto)
            tokens = lexer.tokenizar()
            parser = Parser(tokens)
            arbol = parser.parsear()
            resultado = arbol.evaluar()
            if resultado == None:
                print()
            else:
                print(resultado)
        except Exception as error:
            print(error)     
        pausa()
        
if __name__ == "__main__":
    main()