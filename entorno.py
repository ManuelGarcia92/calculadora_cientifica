import math 

class TablaDeSimbolos:
    def __init__(self):
        self.memoria = {
            "pi" : math.pi,
            "e"  : math.e
        }

    def declarar(self, nombre, valor):
        if nombre in ("pi","e"):
            raise Exception(f"La variable {nombre} no puede ser modificada.")
        self.memoria[nombre] = valor

    def obtener(self, nombre):
        if not nombre in self.memoria:
            raise Exception(f"la variable {nombre} no esta definida.")
        return self.memoria[nombre]
    
    def eliminar(self, nombre):
        if not nombre in self.memoria:
            raise Exception(f"La variable {nombre} no esta definida.")
        if nombre in ("pi","e"):
            raise Exception(f"La variable {nombre} no puede ser eliminada.")
        del self.memoria[nombre]
            
    def limpiar(self):
        if not self.memoria:
            raise Exception("La memoria esta vacía.")
        self.memoria.clear()

    def imprimir_memoria(self):
        if self.memoria:
            print(":::::MEMORIA:::::")
            for variable, valor in self.memoria.items():
                print(f"{variable} = {valor}")
            print()