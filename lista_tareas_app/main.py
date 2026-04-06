from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import TareaApp

def main():
    # Inicializamos las capas
    servicio = TareaServicio()
    # Inyectamos el servicio en la UI
    app = TareaApp(servicio)
    app.mainloop()

if __name__ == "__main__":
    main()