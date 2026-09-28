import operaciones 
OPERACIONES = {
    "**": lambda x, y: x ** y,
    "$" : lambda x, y: operaciones.raiz_enesima(x, y),
    "//": lambda x, y: operaciones.division_entera(x, y),
    "%" : lambda x, y: operaciones.modulo(x, y),
    "/" : lambda x, y: operaciones.division(x, y),
    "*" : lambda x, y: x * y,
    "-" : lambda x, y: x - y,
    "+" : lambda x, y: x + y
} 

OPERADORES_SIMPLES = {
    "+"  : "SUMA",
    "-"  : "RESTA",
    "*"  : "MULTI",
    "/"  : "DIV",
    "$"  : "RAIZ_ENESIMA",
    "%"  : "MOD",
    "("  : "PAREN_IZQ",
    ")"  : "PAREN_DER",
}

OPERADORES_DOBLES = {
    "**" : "POTENCIA",
    "//" : "DIV_ENTERA",
}