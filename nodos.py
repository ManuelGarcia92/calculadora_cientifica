from constantes import OPERACIONES, OPERACIONES_CIENTIFCAS
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

class NodoOperacion:
    def __init__(self, operador, argumentos):
        self.operador = operador
        self.argumentos = argumentos

    def evaluar(self, memoria):
        valores = [valor.evaluar(memoria) for valor in self.argumentos]

        func = OPERACIONES_CIENTIFCAS.get(self.operador)
        if not func:
            raise Exception(f"Error: Operador desconocido : {self.operador}")

        try:
            return func(*valores)
        except TypeError:
            raise Exception(f"Error: N;umero incorrecto de argumentos para {self.operador}")

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