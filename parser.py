import nodos

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.limite = len(tokens)
        self.pos = 0

    def levantar_error(self, mensaje, pasos=0):
        raise Exception(f"Error: {mensaje} : Token {self.peek(pasos).valor} : Columna {self.peek(pasos).columna}")
    
    def advance(self):
        if self.pos < self.limite:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
    
    def peek(self, pasos=0):
        if self.pos + pasos < self.limite:
            return self.tokens[self.pos + pasos]
        
    def match(self, tipo, pasos=0):
        token = self.peek(pasos)
        return token is not None and token.tipo == tipo
    
    def consumir(self, tipo, mensaje_error):
        if self.match(tipo):
            return self.advance()
        self.levantar_error(mensaje_error)    

    def parsear(self):
        instrucciones = []
        
        if self.match("FIN"):
            raise Exception("Expresión vacia")
        
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
            return self.parsear_asignacion_de_variables()
        
        elif self.match("DEL"):
            self.advance()
            return self.parsear_eliminacion()
        
        elif self.match("CLEAR"):
            self.advance()
            return nodos.NodoLimpieza()
        
        else:
            return self.expr()

    def expr(self):
        nodo = self.term()
        while self.match("SUMA") or self.match("RESTA"):
            operador = self.advance()
            derecha = self.term()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def term(self):
        nodo = self.power()
        while self.match("MULTI") or self.match("DIV") or self.match("DIV_ENTERA") or self.match("MOD"):
            operador = self.advance()
            derecha = self.power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def power(self):
        nodo = self.factor()
        if self.match("POTENCIA") or self.match("RAIZ_ENESIMA"):
            operador = self.advance()
            derecha = self.power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def factor(self):
        if self.match("PAREN_IZQ"):
           return self.parsear_parentesis()
        
        if self.match("SUMA") or self.match("RESTA"):
            return self.parsear_numeros_negativos_y_positivos()
            
        if self.match("IDENTIFICADOR"):
           token_id = self.advance()
           return nodos.NodoIdentificador(token_id.valor)
        
        if self.match("OPC"):
            operador = self.advance()
            argumentos = self.parsear_argumentos()
            return nodos.NodoOperacion(operador.valor, argumentos)
        
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
        if self.match("SUMA") or self.match("RESTA"):
            self.levantar_error("Operador repetido")
        elif operador.tipo == "SUMA":
            return nodos.NodoPositivo(self.power())
        else:
            return nodos.NodoNegativo(self.power())
        
    def _parsear_una_asignacion(self):
        token_id = self.consumir("IDENTIFICADOR", "Falta el nombre de la variable")
        self.consumir("ASIGNACION", "Falta el signo de asignación = ")
        nodo = self.expr()
        return nodos.NodoAsignacion(token_id.valor, nodo)

    def parsear_asignacion_de_variables(self):
        asignacion = [self._parsear_una_asignacion()]
        while self.match("COMA"):
           self.advance()
           asignacion.append(self._parsear_una_asignacion())
        self.consumir("PUNTO_Y_COMA", "Se debe finalizar la asignación de variables con ; ")
        return asignacion 
    
    def parsear_eliminacion(self):
        token_id = self.consumir("IDENTIFICADOR", "Falta el nombre de la variable que desea eliminar")
        return nodos.NodoEliminacion(token_id.valor)

    def parsear_argumentos(self):
        argumentos = []
        self.consumir("PAREN_IZQ", "Falta el paréntesis de apertura ( en los argumentos")
        if not self.match("PAREN_DER"):
            argumentos.append(self.expr())
            while self.match("COMA"):
                self.advance()
                argumentos.append(self.expr())
        self.consumir("PAREN_DER", "Falta el paréntesis de cierre ) en los argumentos")
        return argumentos