import operaciones 
import math

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

OPERACIONES_CIENTIFCAS = {
    "abs"  : lambda x: abs(x),
    "asin" : lambda x: math.asin(x),
    "cos"  : lambda x: math.cos(x),
    "acos" : lambda x: math.acos(x),  
    "tan"  : lambda x: math.tan(x), 
    "atan" : lambda x: math.atan(x), 
    "log"  : lambda x: math.log10(x), 
    "logn" : lambda x, base: math.log(x, base), 
}

PALABRAS_RESERVADAS = {
    "var"  : "VAR",
    "abs"  : "OPC",
    "asin" : "OPC",
    "cos"  : "OPC",
    "acos" : "OPC",
    "tan"  : "OPC",
    "atan" : "OPC",
    "log"  : "OPC",
    "logn" : "OPC"
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
    "="  : "ASIGNACION",
    ","  : "COMA", 
    ";"  : "PUNTO_Y_COMA",
}

OPERADORES_DOBLES = {
    "**" : "POTENCIA",
    "//" : "DIV_ENTERA",
}