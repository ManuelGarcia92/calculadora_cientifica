from .stream import TokenStream
from .grammar_rules import GrammarRules

class Parser:
    def __init__(self, tokens):
        self.stream = TokenStream(tokens)
        self.rules = GrammarRules(self.stream)

    def parsear_instrucciones(self):
        if self.stream.match("VAR"):
            self.stream.advance()
            instrucion = self.rules.parsear_secuencia(self.rules.parsear_asignacion)
            self.stream.consumir("PUNTO_Y_COMA", "La secuencia debe finalizar con ; ")
            return instrucion
        
        elif self.stream.match("DEL"):
            self.stream.advance()
            instrucion = self.rules.parsear_secuencia(self.rules.parsear_eliminacion)
            self.stream.consumir("PUNTO_Y_COMA", "La secuencia debe finalizar con ; ")
            return instrucion
        
        elif self.stream.match("CLEAR"):
            self.stream.advance()
            instrucion = self.rules.parsear_limpieza()
            return instrucion
        
        else:
            return self.rules.expr()

    def parsear(self):
        instrucciones = []
        while not self.stream.match("FIN"):
            try:
                instruccion = self.parsear_instrucciones()
                instrucciones.append(instruccion)
            except SyntaxError as error:
                print(f"Error: {error}")
                self.stream.sincronizar()

        if self.stream.peek() and not self.stream.match("FIN"):
            raise Exception("Quedan tokens sin procesar")

        return instrucciones