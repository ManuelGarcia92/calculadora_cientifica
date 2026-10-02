import nodos

class GrammarRules:
    def __init__(self, stream):
        self.stream = stream

    def expr(self):
        nodo = self.term()
        while self.stream.match("SUMA", "RESTA"):
            operador = self.stream.advance()
            derecha = self.term()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def term(self):
        nodo = self.power()
        while self.stream.match("MULTI", "DIV", "DIV_ENTERA", "MOD"):
            operador = self.stream.advance()
            derecha = self.power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def power(self):
        nodo = self.factor()
        if self.stream.match("POTENCIA", "RAIZ_ENESIMA"):
            operador = self.stream.advance()
            derecha = self.power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def factor(self):
        if self.stream.match("PAREN_IZQ"):
            return self.parsear_parentesis()

        if self.stream.match("SUMA", "RESTA"):
            return self.parsear_numeros_negativos_y_positivos()
        
        if self.stream.match("IDENTIFICADOR"):
            token_id = self.stream.advance()
            return nodos.NodoIdentificador(token_id.valor)
        
        if self.stream.match("NUMERO"):
            token = self.stream.advance()
            return nodos.NodoNumero(token.valor)

        if self.stream.match("FUN"):
            operador = self.stream.advance()
            argumentos = self.parsear_argumentos()
            return nodos.NodoFuncion(operador.valor, argumentos) 

        self.stream.levantar_error("Esperaba un número")
         
    def parsear_secuencia(self, metodo):
        instruccion = [metodo()]
        while self.stream.match("COMA"):
            self.stream.advance()
            instruccion.append(metodo())
        return instruccion  
    
    def _parsear_asignacion(self):
        token_id = self.stream.consumir("IDENTIFICADOR", "Falta el nombre de la variable")
        self.stream.consumir("IGUAL", "Falta el signo de asignación = ")
        nodo = self.expr()
        return nodos.NodoAsignacion(token_id.valor, nodo)
    
    def _parsear_eliminacion(self):
        token_id = self.stream.consumir("IDENTIFICADOR", "Falta el nombre de la variable que desea eliminar")
        return nodos.NodoEliminacion(token_id.valor)
    
    def _parsear_limpieza(self):
        return nodos.NodoLimpieza()

    def parsear_argumentos(self):
        self.stream.consumir("PAREN_IZQ", "Falta el paréntesis de apertura ( en los argumentos")
        if not self.stream.match("PAREN_DER"):
            instruccion = self.parsear_secuencia(self.expr)
        self.stream.consumir("PAREN_DER", "Falta el paréntesis de cierre ) en los argumentos")
        return instruccion
    
    def parsear_parentesis(self):
        self.stream.advance()
        nodo = self.expr()
        self.stream.consumir("PAREN_DER", "No cerraste un paréntesis")
        return nodo
    
    def parsear_numeros_negativos_y_positivos(self):
        operador = self.stream.advance()
        if self.stream.match("SUMA", "RESTA"):
            self.stream.levantar_error("Operador repetido")
        elif operador.tipo == "SUMA":
            return nodos.NodoPositivo(self.power())
        else:
            return nodos.NodoNegativo(self.power())
    