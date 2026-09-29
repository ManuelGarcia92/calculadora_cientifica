class TablaDeSimbolos:
    def __init__(self):
        self.memoria = {}

    def declarar(self, nombre, valor):
        self.memoria[nombre] = valor

    def obtener(self, nombre):
        if not nombre in self.memoria:
            raise Exception(f"Error semántico: Variable {nombre} no esta definida.")
        return self.memoria[nombre]
   