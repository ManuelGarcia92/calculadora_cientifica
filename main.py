from calculo import calculo
from historial import historial
import consola
import readline

def main():
    while True:
        consola.limpiar_terminal()
        consola.mostrar_titulo("Calculadora Científica")
        consola.mostrar_menu()
        opcion = consola.pedir_dato(">>> : ")
        if opcion == "3":
            consola.imprimir("Saliendo...")
            break
        elif opcion == "1":
            calculo()
        elif opcion == "2":
            historial()
        else:
            consola.imprimir_error(f"La opción: {opcion} no existe.")
            consola.pausa()
        
if __name__ == "__main__":
    main()