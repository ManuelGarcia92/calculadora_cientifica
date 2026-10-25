from .despacho import OPERACIONES, FUNCIONES

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

class NodoFuncion:
    def __init__(self, operador, argumentos):
        self.operador = operador
        self.argumentos = argumentos

    def evaluar(self, memoria):
        valores = [valor.evaluar(memoria) for valor in self.argumentos]
        
        funcion = FUNCIONES.get(self.operador)
        if not funcion:
            raise Exception(f"Operador desconocido : {self.operador}")
        
        try:
            return funcion(*valores)
        except TypeError:
            raise Exception(f"Número incorrecto de argumentos para {self.operador}")

class NodoNumero:
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self, memoria):
        if "." in self.valor:
            valor = float(self.valor)
        else:
            valor = int(self.valor)
        return valor

class NodoUnario:
    def __init__(self, signo, valor):
        self.signo = signo
        self.valor = valor

    def evaluar(self, memoria):
        resultado = self.valor.evaluar(memoria)
        if self.signo == "-":
            return -resultado
        else:
            return resultado
    
class NodoIdentificador:
    def __init__(self, nombre):
        self.nombre = nombre

    def evaluar(self, memoria):
        return memoria.obtener(self.nombre)

