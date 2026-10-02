from constantes import OPERADORES_SIMPLES, OPERADORES_DOBLES, PALABRAS_RESERVADAS
class Token:
    def __init__(self, tipo, valor, col_inicio, col_fin):
        self.tipo = tipo
        self.valor = valor
        self.col_inicio = col_inicio
        self.col_fin = col_fin

class Lexer:
    def __init__(self, texto: str):
        self.texto = texto
        self.limite = len(texto)
        self.pos = 0

    def advance(self) -> str:
        str_actual = self.texto[self.pos]
        self.pos += 1
        return str_actual
        
    def peek(self, pasos=0) -> str:
        return self.texto[self.pos + pasos]
        
    def leer_palabra(self) -> Token:
        col_inicio = self.pos + 1
        buffer = ""
        while self.pos < self.limite and (self.peek().isalnum() or self.peek() == "_"):
            buffer += self.advance()

        if buffer in PALABRAS_RESERVADAS:
            tipo_token = PALABRAS_RESERVADAS[buffer] 
        else:
            tipo_token = "IDENTIFICADOR"

        col_fin = self.pos
        return Token(tipo_token, buffer, col_inicio, col_fin) 
    
    def leer_numero(self) -> Token:
        col_inicio = self.pos + 1
        contador_punto_decimal = 0
        buffer = ""
        while self.pos < self.limite and (self.peek().isdigit() or self.peek() == "."):
            if self.peek() == ".":
                contador_punto_decimal += 1
            buffer += self.advance()

        col_fin = self.pos
        if contador_punto_decimal > 1:
            raise Exception(f"Error: Un número tiene varios puntos decimales : Token {buffer} : Columna {col_inicio}-{col_fin}")
        
        if contador_punto_decimal:
            if buffer == ".":
                buffer = "0.0"
            elif buffer[0] == ".":
                buffer = "0" + buffer
            elif buffer[-1] == ".":
                buffer += "0"
            valor_token = float(buffer)
        else:
            valor_token = int(buffer)

        return Token("NUMERO", valor_token, col_inicio, col_fin)

    def leer_simbolo(self) -> Token:
        if self.pos < self.limite:
            col_inicio = self.pos + 1

            if self.pos < self.limite - 1 and self.peek() + self.peek(1) in OPERADORES_DOBLES:
                valor_token = self.advance()
                valor_token += self.advance()
                tipo_token = OPERADORES_DOBLES[valor_token]
            else:
                valor_token = self.advance()
                tipo_token = OPERADORES_SIMPLES[valor_token]

            col_fin = self.pos
            return Token(tipo_token, valor_token, col_inicio, col_fin)

    def tokenizar(self) -> list:
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
                raise Exception(f"Error: Caracter desconocido : Token {char_actual} : Columna {self.pos}-{self.pos}")
            
        tokens.append(Token("FIN", None, col_inicio=self.pos+1, col_fin=self.pos+1))
        return tokens

