from .constantes_lexer import OPERADORES_SIMPLES, OPERADORES_DOBLES, PALABRAS_RESERVADAS
from .token import Token

class Lexer:
    def __init__(self, texto: str):
        self.texto = texto
        self.pos = 0

    def tokenizar(self) -> list:
        tokens  = [] 
        while self.pos < len(self.texto):
            char_actual = self._peek()
            if char_actual.isspace():
                self._advance()
            elif char_actual.isalpha() or char_actual == "_":
                tokens.append(self._leer_palabra())
            elif char_actual in OPERADORES_SIMPLES:
                tokens.append(self._leer_simbolo())
            elif char_actual.isdigit() or char_actual == ".":
                tokens.append(self._leer_numero())  
            else:
                raise Exception(f"Caracter desconocido : Token {char_actual} : Columna {self.pos+1}")
        tokens.append(Token("FIN", None, columna=self.pos+1))
        return tokens

    def _advance(self) -> str:
        char = self.texto[self.pos]
        self.pos += 1
        return char
            
    def _peek(self, pasos=0) -> str:
        return self.texto[self.pos + pasos]
 
    def _leer_numero(self) -> Token:
        col_inicio = self.pos + 1
        contador_punto_decimal = 0
        buffer = ""
        while self.pos < len(self.texto) and (self._peek().isdigit() or self._peek() == "."):
            if self._peek() == ".":
                contador_punto_decimal += 1
            buffer += self._advance()

        col_fin = self.pos
        if contador_punto_decimal > 1:
            raise Exception(f"Un número tiene varios puntos decimales : Token {buffer} : Columna {col_inicio}-{col_fin}")
        
        return Token("NUMERO", buffer, columna=f"{col_inicio}-{col_fin}")

    def _leer_simbolo(self) -> Token:
        if self.pos < len(self.texto):
            col_inicio = self.pos + 1
            if self.pos < len(self.texto) - 1 and self._peek() + self._peek(1) in OPERADORES_DOBLES:
                valor_token = self._advance()
                valor_token += self._advance()
                tipo_token = OPERADORES_DOBLES[valor_token]
            else:
                valor_token = self._advance()
                tipo_token = OPERADORES_SIMPLES[valor_token]
                
            col_fin = self.pos
            return Token(tipo_token, valor_token, columna=f"{col_inicio}-{col_fin}")

    def _leer_palabra(self) -> Token:
        col_inicio = self.pos + 1
        buffer = ""
        while self.pos < len(self.texto) and (self._peek().isalnum() or self._peek() == "_"):
            buffer += self._advance()

        if buffer in PALABRAS_RESERVADAS:
            tipo_token = PALABRAS_RESERVADAS[buffer] 
        else:
            tipo_token = "IDENTIFICADOR"

        col_fin = self.pos
        return Token(tipo_token, buffer, columna=f"{col_inicio}-{col_fin}")