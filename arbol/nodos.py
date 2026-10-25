from .despacho import OPERACIONES, FUNCIONES

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
    
class NodoBinario:
    def __init__(self, operador, nodo_izquierdo, nodo_derecho):
        self.operador = operador
        self.nodo_izquierdo = nodo_izquierdo 
        self.nodo_derecho = nodo_derecho

    def evaluar(self, memoria):
        valor_izquierda = self.nodo_izquierdo.evaluar(memoria)
        valor_derecha = self.nodo_derecho.evaluar(memoria)
        resultado = OPERACIONES[self.operador](valor_izquierda, valor_derecha)
        return resultado
    
class NodoFuncion:
    def __init__(self, funcion, argumentos):
        self.funcion = funcion
        self.argumentos = argumentos

    def evaluar(self, memoria):
        valores = [valor.evaluar(memoria) for valor in self.argumentos]
        
        operacion = FUNCIONES.get(self.funcion)
        if not operacion:
            raise Exception(f"Función desconocida : {self.funcion}")
        
        try:
            return operacion(*valores)
        
        except TypeError:
            raise Exception(f"Número incorrecto de argumentos para {self.funcion}")



