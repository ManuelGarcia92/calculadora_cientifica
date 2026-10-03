import consola
from persistencia import cargar_historial, agregar_al_historial
from entorno import TablaDeSimbolos
from lexer import Lexer 
from parser import Parser
from evaluador import Evaluador

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
            lexer = Lexer(texto)
            tokens = lexer.tokenizar()
            parser = Parser(tokens)
            arbol = parser.parsear()
            if arbol:
                evaluador = Evaluador(arbol)
                resultado = evaluador.evaluar(memoria)
                if resultado is not None:
                    agregar_al_historial(texto, resultado)
                    print(resultado)
        except Exception as error:
            consola.mostrar_mensaje(f"[Error de Ejecución]: {error}")     
        consola.pausa()

def main():
    while True:
        consola.limpiar_terminal()
        consola.mostrar_titulo("Calculadora Cientifica")
        consola.mostrar_menu()
        opcion = consola.pedir_dato(">>> : ")
        if opcion == "3":
            consola.mostrar_mensaje("Saliendo...")
            break
        elif opcion == "1":
            calculo()
        elif opcion == "2":
            consola.limpiar_terminal()
            consola.mostrar_titulo("Registro de operaciones.")
            historial = cargar_historial()
            if historial:
                consola.mostrar_registro(historial)
        else:
            consola.mostrar_error(f"La opción: {opcion} no existe.")
        consola.pausa()
        
if __name__ == "__main__":
    main()