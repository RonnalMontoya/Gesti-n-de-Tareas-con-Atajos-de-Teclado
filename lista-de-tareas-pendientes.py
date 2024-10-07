import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        # Lista de tareas
        self.tasks = []

        # Crear la interfaz
        self.create_widgets()

        # Configurar atajos de teclado
        self.root.bind('<Return>', self.add_task)  # Enter para agregar la tarea
        self.root.bind('<c>', self.mark_as_completed)  # C para completar la tarea
        self.root.bind('<Delete>', self.delete_task)  # Delete para eliminar la tarea
        self.root.bind('<d>', self.delete_task)  # D para eliminar la tarea
        self.root.bind('<Escape>', lambda e: self.root.quit())  # Escape para salir

    def create_widgets(self):
        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)

        # Botón para añadir tareas
        self.add_button = tk.Button(self.root, text="Agregar Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Botones para marcar como completada y eliminar tareas
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.mark_as_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.tasks.append(task)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Error de Entrada", "Por favor, ingrese una tarea.")

    def mark_as_completed(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            if not task.startswith("[Completada] "):
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, "[Completada] " + task)
        except IndexError:
            messagebox.showwarning("Error de Selección", "Por favor, seleccione una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Error de Selección", "Por favor, seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
