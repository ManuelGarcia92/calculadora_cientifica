from prompt_toolkit import prompt

def limpiar_terminal() -> None:
    import os
    os.system("cls" if os.name == "nt" else "clear")

def pausa() -> None:
    input("Presione ENTER para continuar...")

def pedir_dato(mensaje: str) -> str:
    return input(mensaje)

def modificar_dato(mensaje, dato: str) -> str:
    return prompt(mensaje, default=dato)

def imprimir(mensaje: str) -> None:
    print(mensaje)

def imprimir_error(mensaje: str) -> None:
    print(f"ERROR: {mensaje}")

def mostrar_titulo(titulo: str) -> None:
    print(f"\n{'=' * 40}")
    print(titulo.center(40))
    print('=' * 40)

def mostrar_menu() -> None:
    print("1. Calculo")
    print("2. Registro de operaciones")
    print("3. Salir")
    print('=' * 40)

def ajustar_numero(numero, ancho):
    numero = str(numero)
    ancho = ancho - len(numero)
    return numero + ancho * " "

def mostrar_registro(registros: list[dict]) -> None:
    ancho = len(str(len(registros)))
    for i, registro in enumerate(registros):
        print(f"[{ajustar_numero(i+1, ancho)}]: {registro["expresion"]} = {registro["resultado"]}")
    print(f"\n{'=' * 40}")

