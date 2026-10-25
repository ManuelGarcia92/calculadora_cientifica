from arbol.nodos import NodoUnario

class AccionesGramaticales:
    def __init__(self, flujo):
        self.flujo = flujo

    def parsear_parentesis(self, metodo_expresion):
        self.flujo.avanzar()
        nodo = metodo_expresion()
        self.flujo.consumir("PAREN_DER", "No cerraste un paréntesis")
        return nodo
    
    def parsear_unario(self, metodo_potencia):
        signo = self.flujo.avanzar()
        if self.flujo.coincide("SUMA", "RESTA"):
            self.flujo.levantar_error("Operador repetido")
        return NodoUnario(signo.valor, metodo_potencia())
        
    def parsear_argumentos(self, metodo):
        argumentos = []
        self.flujo.consumir("PAREN_IZQ", "Falta el paréntesis de apertura ( en los argumentos")
        if not self.flujo.coincide("PAREN_DER"):
            argumentos = self._parsear_secuencia(metodo)
        self.flujo.consumir("PAREN_DER", "Falta el paréntesis de cierre ) en los argumentos")
        return argumentos
    
    def _parsear_secuencia(self, metodo):
        instruccion = [metodo()]
        while self.flujo.coincide("COMA"):
            self.flujo.avanzar()
            instruccion.append(metodo())
        return instruccion  