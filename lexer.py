from constantes import OPERADORES_SIMPLES, OPERADORES_DOBLES, PALABRAS_RESERVADAS
class Token:
    def __init__(self, tipo, valor, columna):
        self.tipo = tipo
        self.valor = valor
        self.columna = columna

class Lexer:
    def __init__(self, texto):
        self.texto = texto
        self.limite = len(texto)
        self.pos = 0

    def advance(self):
        str_actual = self.texto[self.pos]
        self.pos += 1
        return str_actual
        
    def peek(self, pasos=0):
        return self.texto[self.pos + pasos]
        
    def leer_palabra(self):
        buffer = ""
        while self.pos < self.limite and (self.peek().isalnum() or self.peek() == "_"):
            buffer += self.advance()
        if buffer in PALABRAS_RESERVADAS:
            tipo_token = PALABRAS_RESERVADAS[buffer]
            return Token(tipo_token, buffer, self.pos)  
        return Token("IDENTIFICADOR", buffer, self.pos) 
    
    def leer_numero(self):
        contador_punto_decimal = 0
        buffer = ""
        while self.pos < self.limite and (self.peek().isdigit() or self.peek() == "."):
            if self.peek() == ".":
                contador_punto_decimal += 1
            buffer += self.advance()

        if contador_punto_decimal > 1:
            raise Exception(f"Error: Un número tiene varios puntos decimales")
        
        if contador_punto_decimal:
            if buffer == ".":
                buffer = "0.0"
            elif buffer[0] == ".":
                buffer = "0" + buffer
            elif buffer[-1] == ".":
                buffer += "0"
            return Token("NUMERO", float(buffer), self.pos)
        return Token("NUMERO", int(buffer), self.pos)

    def leer_simbolo(self):
        if self.pos < self.limite:
            if self.pos < self.limite - 1 and self.peek() + self.peek(1) in OPERADORES_DOBLES:
                valor_token = self.advance()
                valor_token += self.advance()
                tipo_token = OPERADORES_DOBLES[valor_token]
            else:
                valor_token = self.advance()
                tipo_token = OPERADORES_SIMPLES[valor_token]
            return Token(tipo_token, valor_token, self.pos)

    def tokenizar(self):
        tokens  = [] 
        while self.pos < self.limite:
            char_actual = self.peek()
            if char_actual.isspace():
                self.advance()
            elif char_actual.isalpha() or char_actual == "_":
                tokens.append(self.leer_palabra())
            elif char_actual in OPERADORES_SIMPLES:
                tokens.append(self.leer_simbolo())
            elif char_actual.isdigit() or char_actual == ".":
                tokens.append(self.leer_numero())  
            else:
                raise Exception("Error: Caracter desconocido")
        tokens.append(Token("FIN", None, self.pos))
        return tokens

