import nodos

class GrammarRules:
    def __init__(self, stream):
        self.stream = stream

    def parsear_instrucciones(self):
        if self.stream.match("VAR"):
            self.stream.advance()
            instrucion = self._parsear_secuencia(self._parsear_asignacion)
            self.stream.consumir("PUNTO_Y_COMA", "La secuencia debe finalizar con ; ")
            return instrucion
        
        elif self.stream.match("DEL"):
            self.stream.advance()
            instrucion = self._parsear_secuencia(self._parsear_eliminacion)
            self.stream.consumir("PUNTO_Y_COMA", "La secuencia debe finalizar con ; ")
            return instrucion
        
        elif self.stream.match("CLEAR"):
            self.stream.advance()
            instrucion = self._parsear_limpieza()
            return instrucion
        
        else:
            return self._expr()
            
    def _expr(self):
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
    
    def _parsear_asignacion(self):
        token_id = self.stream.consumir("IDENTIFICADOR", "Falta el nombre de la variable")
        self.stream.consumir("IGUAL", "Falta el signo de asignación = ")
        nodo = self._expr()
        return nodos.NodoAsignacion(token_id.valor, nodo)
    
    def _parsear_eliminacion(self):
        token_id = self.stream.consumir("IDENTIFICADOR", "Falta el nombre de la variable que desea eliminar")
        return nodos.NodoEliminacion(token_id.valor)
    
    def _parsear_limpieza(self):
        return nodos.NodoLimpieza()

    def _parsear_argumentos(self):
        self.stream.consumir("PAREN_IZQ", "Falta el paréntesis de apertura ( en los argumentos")
        if not self.stream.match("PAREN_DER"):
            instruccion = self._parsear_secuencia(self._expr)
        self.stream.consumir("PAREN_DER", "Falta el paréntesis de cierre ) en los argumentos")
        return instruccion
    
    def _parsear_parentesis(self):
        self.stream.advance()
        nodo = self._expr()
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
    