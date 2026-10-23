from .stream import TokenStream
from .grammar_rules import GrammarRules

class Parser:
    def __init__(self, tokens):
        self.stream = TokenStream(tokens)
        self.rules = GrammarRules(self.stream)

    def parsear(self):
        return self.rules.expr()

    