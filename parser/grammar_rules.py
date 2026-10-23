import nodos

class GrammarRules:
    def __init__(self, stream):
        self.stream = stream

    def expr(self):
        nodo = self._term()
        while self.stream.match("SUMA", "RESTA"):
            operador = self.stream.advance()
            derecha = self._term()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _term(self):
        nodo = self._power()
        while self.stream.match("MULTI", "DIV", "DIV_ENTERA", "MOD"):
            operador = self.stream.advance()
            derecha = self._power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _power(self):
        nodo = self._factor()
        if self.stream.match("POTENCIA", "RAIZ_ENESIMA"):
            operador = self.stream.advance()
            derecha = self._power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _factor(self):
        if self.stream.match("PAREN_IZQ"):
            return self._parsear_parentesis()

        if self.stream.match("SUMA", "RESTA"):
            return self._parsear_numeros_negativos_y_positivos()
        
        if self.stream.match("IDENTIFICADOR"):
            token_id = self.stream.advance()
            return nodos.NodoIdentificador(token_id.valor)
        
        if self.stream.match("NUMERO"):
            token = self.stream.advance()
            return nodos.NodoNumero(token.valor)

        if self.stream.match("ERROR"):
            error = self.stream.advance()
            return nodos.NodoError(error.valor)
        
        if self.stream.match("FUN"):
            operador = self.stream.advance()
            argumentos = self._parsear_argumentos()
            return nodos.NodoFuncion(operador.valor, argumentos) 

        self.stream.levantar_error("Esperaba un número")
         
    def _parsear_secuencia(self, metodo):
        instruccion = [metodo()]
        while self.stream.match("COMA"):
            self.stream.advance()
            instruccion.append(metodo())
        return instruccion  
    
    def _parsear_argumentos(self):
        argumentos = []
        self.stream.consumir("PAREN_IZQ", "Falta el paréntesis de apertura ( en los argumentos")
        if not self.stream.match("PAREN_DER"):
            argumentos = self._parsear_secuencia(self.expr)
        self.stream.consumir("PAREN_DER", "Falta el paréntesis de cierre ) en los argumentos")
        return argumentos
    
    def _parsear_parentesis(self):
        self.stream.advance()
        nodo = self.expr()
        self.stream.consumir("PAREN_DER", "No cerraste un paréntesis")
        return nodo
    
    def _parsear_numeros_negativos_y_positivos(self):
        operador = self.stream.advance()
        if self.stream.match("SUMA", "RESTA"):
            self.stream.levantar_error("Operador repetido")
        elif operador.tipo == "SUMA":
            return nodos.NodoPositivo(self._power())
        else:
            return nodos.NodoNegativo(self._power())
    