from . import operaciones
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
    "asin" : lambda x: operaciones.arcoseno(x),
    "cos"  : lambda x: math.cos(x),
    "acos" : lambda x: operaciones.arcocoseno(x),  
    "tan"  : lambda x: math.tan(x), 
    "atan" : lambda x: math.atan(x), 
    "ln"   : lambda x: operaciones.ln(x), 
    "log"  : lambda x, base: operaciones.logaritmo(x, base), 
}