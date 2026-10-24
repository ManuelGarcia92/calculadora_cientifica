from .stream import TokenStream
from .grammar_rules import GrammarRules

class Parser:
    def __init__(self, tokens):
        self.stream = TokenStream(tokens)
        self.rules = GrammarRules(self.stream)

    def parsear(self):
        arbol = self.rules.expr()

        if self.stream.peek() and not self.stream.match("FIN"):
            self.stream.levantar_error("Esperaba un operador")

        return arbol