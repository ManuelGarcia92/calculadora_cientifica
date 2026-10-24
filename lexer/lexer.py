from .constantes_lexer import PALABRAS_RESERVADAS, OPERADORES_SIMPLES, OPERADORES_DOBLES
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
                raise Exception(f"Caracter desconocido : {char_actual}")
        tokens.append(Token("FIN", None))
        return tokens
    
    def _advance(self) -> str:
        char = self.texto[self.pos]
        self.pos += 1
        return char
            
    def _peek(self, pasos=0) -> str:
        return self.texto[self.pos + pasos]
 
    def _leer_numero(self) -> Token:
        contador_punto_decimal = 0
        buffer = ""
        while self.pos < len(self.texto) and (self._peek().isdigit() or self._peek() == "."):
            if self._peek() == ".":
                contador_punto_decimal += 1
            buffer += self._advance()

        if contador_punto_decimal > 1:
            raise Exception(f"Número con varios puntos decimales : {buffer}")

        return Token("NUMERO", buffer)

    def _leer_simbolo(self) -> Token:
        if self.pos < len(self.texto):
            if self.pos < len(self.texto) - 1 and self._peek() + self._peek(1) in OPERADORES_DOBLES:
                valor_token = self._advance()
                valor_token += self._advance()
                tipo_token = OPERADORES_DOBLES[valor_token]

            else:
                valor_token = self._advance()
                tipo_token = OPERADORES_SIMPLES[valor_token]
                
            return Token(tipo_token, valor_token)

    def _leer_palabra(self) -> Token:
        buffer = ""
        while self.pos < len(self.texto) and (self._peek().isalnum() or self._peek() == "_"):
            buffer += self._advance()

        if buffer in PALABRAS_RESERVADAS:
            tipo_token = PALABRAS_RESERVADAS[buffer] 

        else:
            tipo_token = "IDENTIFICADOR"

        return Token(tipo_token, buffer)

    @staticmethod
    def formatear_tokens(tokens):
        if not tokens:
            return ""
        resultado = []
        for i, token in enumerate(tokens):
            valor = str(token.valor)
            if valor == "None":
                continue
            if valor == ",":
                resultado.append(f"{valor} ")
            else:
                resultado.append(valor)
        return "".join(resultado)