from .stream import TokenStream
from .grammar_rules import GrammarRules

class Parser:
    def __init__(self, tokens):
        self.stream = TokenStream(tokens)
        self.rules = GrammarRules(self.stream)

    def parsear(self):
        instrucciones = []
        while not self.stream.match("FIN"):
            try:
                instruccion = self.rules.parsear_instrucciones()
                instrucciones.append(instruccion)
                if self.stream.match("PUNTO_Y_COMA"):
                    self.stream.advance()
            except SyntaxError as error:
                print(f"Error: {error}")
                self.stream.sincronizar()

        if self.stream.peek() and not self.stream.match("FIN"):
            raise Exception("Quedan tokens sin procesar")

        return instrucciones