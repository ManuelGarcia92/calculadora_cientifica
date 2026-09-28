from constantes import OPERADORES_SIMPLES, OPERADORES_DOBLES
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
            return float(buffer)
        return int(buffer)

    def leer_simbolo(self):
        if self.pos < self.limite:
            if self.pos < self.limite - 1 and self.peek() + self.peek(1) in OPERADORES_DOBLES:
                operador = self.advance()
                operador += self.advance()
            else:
                operador = self.advance()
            return operador

    def tokenizar(self):
        tokens  = [] 
        while self.pos < self.limite:
            char_actual = self.peek()
            if char_actual.isspace():
                self.advance()
            elif char_actual.isdigit() or char_actual == ".":
                tokens.append(self.leer_numero())  
            elif char_actual in OPERADORES_SIMPLES:
                tokens.append(self.leer_simbolo())
            else:
                raise Exception("Error:Caracter desconocido")
            
        tokens.append("FIN")
        return tokens

