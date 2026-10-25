import math

def ln(x):
    if x <= 0:
        raise Exception("El logaritmo natural (ln) requiere un valor mayor a 0")
    return math.log(x)

def logaritmo(x, base=10):
    if x <= 0 or base <= 0:
        raise Exception("El logaritmo (log) y la base deben ser mayores a 0")
    if base == 1:
        raise Exception("La base de un logaritmo no puede ser 1")
    return math.log(x, base)

def arcoseno(x):
    if x < -1 or x > 1:
        raise Exception("El arcoseno (asin) solo acepta valores entre -1 y 1")
    return math.asin(x)

def arcocoseno(x):
    if x < -1 or x > 1:
        raise Exception("El arcocoseno (acos) solo acepta valores entre -1 y 1")
    return math.acos(x)

def division(x, y):
    if y == 0:
        raise Exception("No se puede dividir por 0")
    return x / y
    
def division_entera(x, y):
    if y == 0:
        raise Exception("No se puede dividir por 0")
    return x // y
    
def modulo(x, y):
    if y == 0:
        raise Exception("Módulo no se puede dividir por 0")
    return x % y

def raiz_enesima(x, y):
    if y < 0 and x % 2 != 0:
        return -(-y ** x)
    return y ** (1 / x)