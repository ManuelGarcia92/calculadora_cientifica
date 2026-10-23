class Evaluador:
    def __init__(self, instruccion):
        self.instruccion = instruccion

    def evaluar(self, memoria):
        resultado = None
        if self.instruccion is not None:
            resultado = self.instruccion.evaluar(memoria)
        return resultado
       


