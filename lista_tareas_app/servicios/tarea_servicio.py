from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, texto: str):
        nueva = Tarea(texto)
        self._tareas.append(nueva)
        return nueva

    def marcar_completada(self, indice: int):
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].completada = True

    def eliminar_tarea(self, indice: int):
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)

    def obtener_todas(self):
        return self._tareas