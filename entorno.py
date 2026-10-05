from persistencia import cargar_memoria, guardar_memoria
import math 

class TablaDeSimbolos:
    CONSTANTES = {"pi" : math.pi, "e"  : math.e}

    def __init__(self):
        datos_guardados = cargar_memoria()
        self.memoria = self.CONSTANTES.copy()
        self.memoria.update(datos_guardados)

    def _sincronizar_json(self):
        variables_usuario = {
            k: v for k, v in self.memoria.items() if k not in self.CONSTANTES
        }
        guardar_memoria(variables_usuario)

    def declarar(self, nombre, valor):
        if nombre in self.CONSTANTES:
            raise Exception(f"La variable {nombre} no puede ser modificada")
        self.memoria[nombre] = valor
        self._sincronizar_json()

    def obtener(self, nombre):
        if not nombre in self.memoria:
            raise Exception(f"La variable {nombre} no esta definida")
        return self.memoria[nombre]
    
    def eliminar(self, nombre):
        if nombre not in self.memoria:
            raise Exception(f"La variable {nombre} no esta definida")
        if nombre in self.CONSTANTES:
            raise Exception(f"La variable {nombre} no puede ser eliminada")
        del self.memoria[nombre]
        self._sincronizar_json()
            
    def limpiar(self):
        if not self.memoria:
            raise Exception("La memoria esta vacía.")
        self.memoria = self.CONSTANTES.copy()
        self._sincronizar_json()

    def imprimir_memoria(self):
        if self.memoria:
            print(":::::MEMORIA:::::")
            for variable, valor in self.memoria.items():
                print(f"{variable} = {valor}")