class GramaticalActions:
    def __init__(self, flujo):
        self.flujo = flujo

    def parsear_parentesis(self, metodo_expre):
        self.flujo.advance()
        nodo = metodo_expre()
        self.flujo.consumir("PAREN_DER", "No cerraste un paréntesis")
        return nodo
    
    def parsear_negativos_y_positivos(self, metodo_power, nodo_unario):
        operador = self.flujo.advance()
        if self.flujo.match("SUMA", "RESTA"):
            self.flujo.levantar_error("Operador repetido")
        return nodo_unario(operador.valor, metodo_power())
        
    def parsear_argumentos(self, metodo):
        argumentos = []
        self.flujo.consumir("PAREN_IZQ", "Falta el paréntesis de apertura ( en los argumentos")
        if not self.flujo.match("PAREN_DER"):
            argumentos = self._parsear_secuencia(metodo)
        self.flujo.consumir("PAREN_DER", "Falta el paréntesis de cierre ) en los argumentos")
        return argumentos
    
    def parsear_secuencia(self, metodo):
        instruccion = [metodo()]
        while self.flujo.match("COMA"):
            self.flujo.advance()
            instruccion.append(metodo())
        return instruccion  