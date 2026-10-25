from .acciones_gramaticales import GramaticalActions
from arbol import nodos

class GrammarRules:
    def __init__(self, flujo):
        self.flujo = flujo
        self.acciones = GramaticalActions(self.flujo)

    def expr(self):
        nodo = self._term()
        while self.flujo.match("SUMA", "RESTA"):
            operador = self.flujo.advance()
            derecha = self._term()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _term(self):
        nodo = self._power()
        while self.flujo.match("MULTI", "DIV", "DIV_ENTERA", "MOD"):
            operador = self.flujo.advance()
            derecha = self._power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _power(self):
        nodo = self._factor()
        if self.flujo.match("POTENCIA", "RAIZ_ENESIMA"):
            operador = self.flujo.advance()
            derecha = self._power()
            nodo = nodos.NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _factor(self):
        if self.flujo.match("PAREN_IZQ"):
            return self.acciones._parsear_parentesis(self.expr)

        elif self.flujo.match("SUMA", "RESTA"):
            return self.acciones._parsear_negativos_y_positivos(self._power, nodos.NodoUnario)
        
        elif self.flujo.match("IDENTIFICADOR"):
            token_id = self.flujo.advance()
            return nodos.NodoIdentificador(token_id.valor)
        
        elif self.flujo.match("NUMERO"):
            token = self.flujo.advance()
            return nodos.NodoNumero(token.valor)

        elif self.flujo.match("FUN"):
            operador = self.flujo.advance()
            argumentos = self.acciones._parsear_argumentos(self.expr)
            return nodos.NodoFuncion(operador.valor, argumentos) 
        
        else:
            self.flujo.levantar_error("Esperaba un número")
         
    
    