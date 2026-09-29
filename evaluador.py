class Evaluador:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def evaluar(self, memoria):
        resultado = None
        if self.instrucciones is not None:
            for instruccion in self.instrucciones:
                if isinstance(instruccion, list):
                    for sub_instrucion in instruccion:
                        resultado = sub_instrucion.evaluar(memoria)
                else:
                    resultado = instruccion.evaluar(memoria)
        return resultado
       


