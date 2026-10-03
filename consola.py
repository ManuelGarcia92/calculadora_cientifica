def limpiar_terminal() -> None:
    import os
    os.system("cls" if os.name == "nt" else "clear")

def pausa() -> None:
    input("Presione ENTER para continuar...")

def pedir_dato(mensaje: str) -> str:
    return input(f"\n{mensaje}").strip()

def mostrar_mensaje(mensaje: str) -> None:
    print(f"\n{mensaje}")

def mostrar_error(mensaje: str) -> None:
    print(f"\nERROR: {mensaje}")

def mostrar_titulo(titulo: str) -> None:
    print(f"\n{'=' * 40}")
    print(titulo.center(40))
    print('=' * 40)

def mostrar_menu() -> None:
    print("1. Calculo")
    print("2. Registro de operaciones")
    print("3. Salir")
    print('=' * 40)

def mostrar_registro(registros: list[dict]) -> None:
    for i, registro in enumerate(registros):
        print(f"[{i+1}]: {registro["expresion"]} = {registro["resultado"]}")
    print(f"\n{'=' * 40}")