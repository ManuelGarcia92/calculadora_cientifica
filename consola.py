from historial import mostrar_historial
from interfaz import interfaz
from calculo import calculo

def iniciar_consola() -> None:
    while True:
        interfaz.limpiar_terminal()
        interfaz.mostrar_titulo("Calculadora Científica")
        interfaz.mostrar_menu()
        opcion = interfaz.pedir_dato(">>> : ")
        if opcion == "3":
            interfaz.imprimir("Saliendo...")
            break
        elif opcion == "1":
            calculo()
        elif opcion == "2":
            mostrar_historial()
        else:
            interfaz.imprimir_error(f"La opción: {opcion} no existe.")
            interfaz.pausa()