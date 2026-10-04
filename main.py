from enrutador import calculo, ver_historial
import consola

def main():
    while True:
        consola.limpiar_terminal()
        consola.mostrar_titulo("Calculadora Científica")
        consola.mostrar_menu()
        opcion = consola.pedir_dato(">>> : ")
        if opcion == "3":
            consola.mostrar_mensaje("Saliendo...")
            break
        elif opcion == "1":
            calculo()
        elif opcion == "2":
            ver_historial()
        else:
            consola.mostrar_error(f"La opción: {opcion} no existe.")
            consola.pausa()
        
if __name__ == "__main__":
    main()