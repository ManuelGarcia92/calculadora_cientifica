import math  

class TablaDeSimbolos:
    def __init__(self):
        self.memoria = {
            "pi" : math.pi,
            "e"  : math.e
        }
        
    def obtener(self, nombre):
        if not nombre in self.memoria:
            raise Exception(f"La variable {nombre} no existe, solo se pueden usar pi y e.")
        return self.memoria[nombre]
    
  