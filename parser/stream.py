class TokenStream:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def levantar_error(self, mensaje):
        raise SyntaxError(f"{mensaje}: Token {self.peek().valor} : Columna {self.peek().columna}")
    
    def peek(self):
        if self.pos < len(self.tokens):
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

    def sincronizar(self):
        while not self.match("FIN"):
            if self.pos > 0 and self.tokens[self.pos - 1].tipo == "PUNTO_Y_COMA":
                return
            if self.match("VAR", "DEL", "CLEAR"):
                return
            self.advance()
        