from arbol.nodos import NodoNumero, NodoIdentificador, NodoBinario, NodoFuncion
from .acciones_gramaticales import AccionesGramaticales

class ReglasGramaticales:
    def __init__(self, flujo):
        self.flujo = flujo
        self.acciones = AccionesGramaticales(self.flujo)

    def expresion(self):
        nodo = self._termino()
        while self.flujo.coincide("SUMA", "RESTA"):
            operador = self.flujo.avanzar()
            derecha = self._termino()
            nodo = NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _termino(self):
        nodo = self._potencia()
        while self.flujo.coincide("MULTI", "DIV", "DIV_ENTERA", "MOD"):
            operador = self.flujo.avanzar()
            derecha = self._potencia()
            nodo = NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _potencia(self):
        nodo = self._factor()
        if self.flujo.coincide("POTENCIA", "RAIZ_ENESIMA"):
            operador = self.flujo.avanzar()
            derecha = self._potencia()
            nodo = NodoBinario(operador.valor, nodo, derecha)
        return nodo

    def _factor(self):
        if self.flujo.coincide("PAREN_IZQ"):
            return self.acciones.parsear_parentesis(self.expresion)

        elif self.flujo.coincide("SUMA", "RESTA"):
            return self.acciones.parsear_unario(self._potencia)
        
        elif self.flujo.coincide("IDENTIFICADOR"):
            token_identificador = self.flujo.avanzar()
            return NodoIdentificador(token_identificador.valor)
        
        elif self.flujo.coincide("NUMERO"):
            token_numero = self.flujo.avanzar()
            return NodoNumero(token_numero.valor)

        elif self.flujo.coincide("FUN"):
            token_funcion = self.flujo.avanzar()
            argumentos = self.acciones.parsear_argumentos(self.expresion)
            return NodoFuncion(token_funcion.valor, argumentos) 
        
        else:
            self.flujo.levantar_error("Esperaba un número")
         
    
    