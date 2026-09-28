from constantes import OPERACIONES
class NodoBinario:
    def __init__(self, operador, izquierda, derecha):
        self.operador = operador
        self.izquierda = izquierda 
        self.derecha = derecha

    def evaluar(self):
        val_izquierda = self.izquierda.evaluar()
        val_derecha = self.derecha.evaluar()
        resultado = OPERACIONES[self.operador](val_izquierda, val_derecha)
        return resultado

class NodoNumero:
    def __inir__(self, valor):
        self.valor = valor

    def evaluar(self):
        return self.valor.evaluar()
    