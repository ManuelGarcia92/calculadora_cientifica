import nodos

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.limite = len(tokens)
        self.pos = 0

    def levantar_error(self, mensaje):
        raise Exception(f"{mensaje} : Token {self.peek().valor} : Columna {self.peek().col_inicio}-{self.peek().col_fin}")
    
    def peek(self):
        if self.pos < self.limite:
            return self.tokens[self.pos]
        return None
            
    def advance(self):
        token_actual = self.peek()
        if token_actual:
            self.pos += 1
            return token_actual
        return None
          
    def match(self, *tipos):
        token_actual = self.peek()
        if token_actual and token_actual.tipo in tipos:
            return token_actual
        return None
    
    def consumir(self, tipo_esperado, mensaje_error):
        if self.match(tipo_esperado):
            return self.advance()
        self.levantar_error(mensaje_error)    

    def parsear(self):
        instrucciones = []
        
        while not self.match("FIN"):
            instrucciones.append(self.parsear_instrucciones())
            if self.match("PUNTO_Y_COMA"):
                self.advance()

        if self.peek() and not self.match("FIN"):
            self.levantar_error("Quedan tokens sin procesar")

        return instrucciones
    
    def parsear_instrucciones(self):
        if self.match("VAR"):
            self.advance()
            instrucion = self.parsear_secuencia(self._parsear_asignacion)
            self.consumir("PUNTO_Y_COMA", "La secuencia debe finalizar con ; ")
            return instrucion
        
        elif self.match("DEL"):
            self.advance()
            instrucion = self.parsear_secuencia(self._parsear_eliminacion)
            self.consumir("PUNTO_Y_COMA", "La secuencia debe finalizar con ; ")
            return instrucion
        
        elif self.match("CLEAR"):
            self.advance()
            return nodos.NodoLimpieza()
        
        else:
            return self.expr()

    def expr(self):
        nodo = self.term()
        while self.match("SUMA", "RESTA"):
            operador = self.advance()
            derecha = self.term()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def term(self):
        nodo = self.power()
        while self.match("MULTI", "DIV", "DIV_ENTERA", "MOD"):
            operador = self.advance()
            derecha = self.power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def power(self):
        nodo = self.factor()
        if self.match("POTENCIA", "RAIZ_ENESIMA"):
            operador = self.advance()
            derecha = self.power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def factor(self):
        if self.match("PAREN_IZQ"):
            return self.parsear_parentesis()
        
        if self.match("SUMA", "RESTA"):
            return self.parsear_numeros_negativos_y_positivos()
        
        if self.match("OPC"):
            operador = self.advance()
            argumentos = self.parsear_argumentos()
            return nodos.NodoOperacion(operador.valor, argumentos)  
          
        if self.match("IDENTIFICADOR"):
            token_id = self.advance()
            return nodos.NodoIdentificador(token_id.valor)
        
        if self.match("NUMERO"):
            token = self.advance()
            return nodos.NodoNumero(token.valor)

        self.levantar_error("Esperaba un número")

    def parsear_parentesis(self):
        self.advance()
        nodo = self.expr()
        self.consumir("PAREN_DER", "No cerraste un paréntesis")
        return nodo
    
    def parsear_numeros_negativos_y_positivos(self):
        operador = self.advance()
        if self.match("SUMA", "RESTA"):
            self.levantar_error("Operador repetido")
        elif operador.tipo == "SUMA":
            return nodos.NodoPositivo(self.power())
        else:
            return nodos.NodoNegativo(self.power())
        
    def parsear_secuencia(self, metodo):
        instruccion = [metodo()]
        while self.match("COMA"):
            self.advance()
            instruccion.append(metodo())
        return instruccion  
     
    def parsear_argumentos(self):
        self.consumir("PAREN_IZQ", "Falta el paréntesis de apertura ( en los argumentos")
        if not self.match("PAREN_DER"):
            instruccion = self.parsear_secuencia(self.expr)
        self.consumir("PAREN_DER", "Falta el paréntesis de cierre ) en los argumentos")
        return instruccion
    
    def _parsear_asignacion(self):
        token_id = self.consumir("IDENTIFICADOR", "Falta el nombre de la variable")
        self.consumir("ASIGNACION", "Falta el signo de asignación = ")
        nodo = self.expr()
        return nodos.NodoAsignacion(token_id.valor, nodo)
    
    def _parsear_eliminacion(self):
        token_id = self.consumir("IDENTIFICADOR", "Falta el nombre de la variable que desea eliminar")
        return nodos.NodoEliminacion(token_id.valor)
    
    
    
     
    
    