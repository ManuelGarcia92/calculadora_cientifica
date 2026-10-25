from .reglas_gramaticales import ReglasGramaticales
from .flujo import FlujoDeTokens

class Parser:
    def __init__(self, tokens):
        self.flujo = FlujoDeTokens(tokens)
        self.reglas = ReglasGramaticales(self.flujo)

    def parsear(self):
        if self.flujo.coincide("FIN"):
            self.flujo.levantar_error("Expresión vacia")

        arbol = self.reglas.expresion()

        if self.flujo.mirar() and not self.flujo.coincide("FIN"):
            self.flujo.levantar_error("Esperaba un operador")

        return arbol