from constantes import OPERACIONES
class NodoBinario:
    def __init__(self, operador, izquierda, derecha):
        self.operador = operador
        self.izquierda = izquierda 
        self.derecha = derecha

    def evaluar(self, memoria):
        val_izquierda = self.izquierda.evaluar(memoria)
        val_derecha = self.derecha.evaluar(memoria)
        resultado = OPERACIONES[self.operador](val_izquierda, val_derecha)
        return resultado

class NodoNumero:
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self, memoria):
        return self.valor

class NodoPositivo(NodoNumero):
    def evaluar(self, memoria):
        return self.valor.evaluar(memoria)
    
class NodoNegativo(NodoNumero):
    def evaluar(self, memoria):
        return -self.valor.evaluar(memoria)

class NodoAsignacion:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def evaluar(self, memoria):
        return memoria.declarar(self.nombre, self.valor.evaluar(memoria))
    
class NodoIdentificador:
    def __init__(self, nombre):
        self.nombre = nombre

    def evaluar(self, memoria):
        return memoria.obtener(self.nombre)