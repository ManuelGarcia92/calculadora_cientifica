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
    "sin"  : lambda x: math.sin(x),
    "asin" : lambda x: math.asin(x),
    "cos"  : lambda x: math.cos(x),
    "acos" : lambda x: math.acos(x),  
    "tan"  : lambda x: math.tan(x), 
    "atan" : lambda x: math.atan(x), 
    "ln"   : lambda x, base: math.log(x, base), 
    "log"  : lambda x: math.log10(x), 
}

PALABRAS_RESERVADAS = {
    "var"   : "VAR",
    "del"   : "DEL",
    "clear" : "CLEAR",
    "abs"   : "OPC",
    "sin"   : "SIN",
    "asin"  : "OPC",
    "cos"   : "OPC",
    "acos"  : "OPC",
    "tan"   : "OPC",
    "atan"  : "OPC",
    "ln"    : "OPC",
    "log"   : "OPC",

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