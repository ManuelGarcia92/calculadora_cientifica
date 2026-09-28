from nodos import NodoBinario, NodoNumero
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.limite = len(tokens)
        self.pos = 0

    def levantar_error(self, mensaje, pasos=0):
        raise Exception(f"Error: {mensaje}: Token: {self.peek(pasos)}")
    
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
        if self.match("Fin"):
            self.levantar_error("Error: Expresión vacia")

        instrucion = self.expr()

        if self.peek() and not self.match("FIN"):
            self.levantar_error("Quedan tokens sin procesar")

        return instrucion

    def expr(self):
        nodo = self.term()
        while self.match("SUMA") or self.match("RESTA"):
            operador = self.advance()
            derecha = self.term()
            nodo = NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def term(self):
        nodo = self.power()
        while self.match("MULTI") or self.match("DIV") or self.match("DIV_ENTERA")or self.match("MOD"):
            operador = self.advance()
            derecha = self.power()
            nodo = NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def power(self):
        nodo = self.factor()
        if self.match("POTENCIA") or self.match("RAIZ_ENESIMA"):
            operador = self.advance()
            derecha = self.power()
            nodo = NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def factor(self):
        if self.match("PAREN_IZQ"):
            self.advance()
            nodo = self.expr()
            self.consumir("PAREN_DER", "No cerraste un paréntesis")
            return nodo
        
        if self.match("NUMERO"):
            token = self.advance()
            return NodoNumero(token.valor)

        self.levantar_error("Esperaba un número")
