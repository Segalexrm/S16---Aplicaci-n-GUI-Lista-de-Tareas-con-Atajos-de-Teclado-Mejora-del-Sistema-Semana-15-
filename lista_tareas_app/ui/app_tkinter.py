import tkinter as tk
from tkinter import messagebox

class TareaApp(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("To-Do List Pro - Semana 16")
        self.geometry("450x550")
        self.configure(bg="#f8f9fa")

        self._configurar_ui()
        self._configurar_atajos()
        self._refrescar_lista()

    def _configurar_ui(self):
        # Campo de entrada
        tk.Label(self, text="Escribe una tarea y presiona Enter:", bg="#f8f9fa", font=("Arial", 10)).pack(pady=(10,0))
        self.entrada = tk.Entry(self, font=("Arial", 12), width=35)
        self.entrada.pack(pady=10, padx=20)
        self.entrada.focus_set()

        # Botones con comandos de clic
        frame_btns = tk.Frame(self, bg="#f8f9fa")
        frame_btns.pack(pady=5)

        tk.Button(frame_btns, text="Añadir (Enter)", command=self._accion_agregar, bg="#28a745", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btns, text="Completar (C)", command=self._accion_completar, bg="#007bff", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btns, text="Eliminar (Del/D)", command=self._accion_eliminar, bg="#dc3545", fg="white").pack(side=tk.LEFT, padx=5)

        # Listbox
        self.lista_visual = tk.Listbox(self, font=("Arial", 11, "bold"), width=45, height=15, selectmode=tk.SINGLE)
        self.lista_visual.pack(pady=15, padx=20)
        
        tk.Label(self, text="Atajos: [C] Completar | [D/Supr] Eliminar | [Esc] Salir", 
                 font=("Arial", 8, "italic"), bg="#f8f9fa", fg="#6c757d").pack()

    def _configurar_atajos(self):
        # Eventos de teclado solicitados
        self.entrada.bind("<Return>", lambda e: self._accion_agregar()) # Enter en el Entry
        self.bind("<Escape>", lambda e: self.destroy())                # Esc para salir
        
        # Atajos globales (funcionan cuando la ventana tiene el foco)
        self.bind("<KeyPress-c>", lambda e: self._accion_completar())
        self.bind("<KeyPress-C>", lambda e: self._accion_completar())
        self.bind("<KeyPress-d>", lambda e: self._accion_eliminar())
        self.bind("<KeyPress-D>", lambda e: self._accion_eliminar())
        self.bind("<Delete>", lambda e: self._accion_eliminar())

    def _accion_agregar(self):
        try:
            texto = self.entrada.get()
            self.servicio.agregar_tarea(texto)
            self.entrada.delete(0, tk.END)
            self._refrescar_lista()
        except ValueError as e:
            messagebox.showwarning("Atención", str(e))

    def _accion_completar(self):
        seleccion = self.lista_visual.curselection()
        if seleccion:
            self.servicio.marcar_completada(seleccion[0])
            self._refrescar_lista()

    def _accion_eliminar(self):
        seleccion = self.lista_visual.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self._refrescar_lista()

    def _refrescar_lista(self):
        self.lista_visual.delete(0, tk.END)
        for i, t in enumerate(self.servicio.obtener_todas()):
            item_texto = f" {t.descripcion}"
            if t.completada:
                self.lista_visual.insert(tk.END, f" ✔ {item_texto} [HECHO]")
                self.lista_tareas_estilo(i, "#d4edda", "#155724") # Verde
            else:
                self.lista_visual.insert(tk.END, f" ○ {item_texto}")
                self.lista_tareas_estilo(i, "white", "black")

    def lista_tareas_estilo(self, indice, fondo, texto):
        self.lista_visual.itemconfig(indice, {'bg': fondo, 'fg': texto})