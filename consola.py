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

def formatear_texto(tokens):
    if not tokens:
        return ""
    resultado = []
    espacio_derecha = {";", ","}
    for i, token in enumerate(tokens):
        valor = str(token.valor)
        if valor == "None":
            continue
        if i == 0:
            resultado.append(valor)
            continue
        token_anterior = str(tokens[i - 1].valor)
        if token_anterior in ("var", "del", "clear"):
            resultado.append(f" {valor}")
        elif valor in espacio_derecha:
            resultado.append(f"{valor} ")
        else:
            resultado.append(valor)
    return "".join(resultado)