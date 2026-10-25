from .flujo import TokenStream
from .reglas_gramaticales import GrammarRules


class Parser:
    def __init__(self, tokens):
        self.flujo = TokenStream(tokens)
        self.reglas = GrammarRules(self.flujo)

    def parsear(self):
        arbol = self.reglas.expr()

        if self.flujo.peek() and not self.flujo.match("FIN"):
            self.flujo.levantar_error("Esperaba un operador")

        return arbol