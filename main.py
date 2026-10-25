from historial import mostrar_historial
from interfaz import consola
from calculo import calculo
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
            mostrar_historial()
        else:
            consola.imprimir_error(f"La opción: {opcion} no existe.")
            consola.pausa()
        
if __name__ == "__main__":
    main()