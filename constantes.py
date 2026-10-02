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

FUNCIONES = {
    "abs"  : lambda x: abs(x),
    "sin"  : lambda x: math.sin(x),
    "asin" : lambda x: math.asin(x),
    "cos"  : lambda x: math.cos(x),
    "acos" : lambda x: math.acos(x),  
    "tan"  : lambda x: math.tan(x), 
    "atan" : lambda x: math.atan(x), 
    "log"  : lambda x: math.log10(x), 
    "ln"   : lambda x, base: math.log(x, base), 
}

PALABRAS_RESERVADAS = {
    "var"   : "VAR",
    "del"   : "DEL",
    "clear" : "CLEAR",
    "abs"   : "FUN",
    "sin"   : "FUN",
    "asin"  : "FUN",
    "cos"   : "FUN",
    "acos"  : "FUN",
    "tan"   : "FUN",
    "atan"  : "FUN",
    "log"   : "FUN",
    "ln"    : "FUN",
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
    "="  : "IGUAL",
    ","  : "COMA", 
    ";"  : "PUNTO_Y_COMA",
}

OPERADORES_DOBLES = {
    "**" : "POTENCIA",
    "//" : "DIV_ENTERA",
}