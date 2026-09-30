class TablaDeSimbolos:
    def __init__(self):
        self.memoria = {
            "pi" : 3.1415926536,
            "e"  : 2.7182818285
        }

    def declarar(self, nombre, valor):
        self.memoria[nombre] = valor

    def obtener(self, nombre):
        if not nombre in self.memoria:
            raise Exception(f"Error semántico: Variable {nombre} no esta definida.")
        return self.memoria[nombre]
    
    def eliminar(self, clave):
        if clave in self.memoria:
            del self.memoria[clave]
            
    def limpiar(self):
        self.memoria.clear()

    def imprimir_memoria(self):
        if self.memoria:
            print(":::::MEMORIA:::::")
            for variable, valor in self.memoria.items():
                print(f"{variable} = {valor}")
            print()