def ajustar_ancho(texto, ancho):
    texto = str(texto)
    ancho = ancho - len(texto)
    return texto + ancho * " "

def formatear_tokens(tokens):
    if not tokens:
        return ""
    resultado = []
    for i, token in enumerate(tokens):
        valor = str(token.valor)
        if valor == "None":
            continue
        if valor == ",":
            resultado.append(f"{valor} ")
        else:
            resultado.append(valor)
    return "".join(resultado)