import tkinter as tk
from app_table import AppTable
import requests
from tkinter import messagebox


class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MusicApp")

        # Crear el frame y la tabla
        self.table = AppTable(root)

        # Crear barra de búsqueda
        tk.Label(root, text="Buscar por ID:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        search_button = tk.Button(root, text="Buscar", command=self.search_by_id)
        search_button.grid(row=0, column=2, padx=5, pady=5)

        # Botón para mostrar todo
        show_all_button = tk.Button(root, text="Mostrar todo", command=self.load_all_data)
        show_all_button.grid(row=0, column=3, padx=5, pady=5)

        # Botón para refrescar
        refresh_button = tk.Button(root, text="Refrescar", command=self.load_all_data)
        refresh_button.grid(row=2, column=1, pady=5)

        # Cargar todos los datos al iniciar
        self.load_all_data()

    def load_all_data(self):
        """Obtiene todos los datos desde la API y los carga en la tabla."""
        try:
            response = requests.get("https://671be4322c842d92c381a5dc.mockapi.io/Music")
            response.raise_for_status()
            data = response.json()

            # Pasar los datos a la tabla
            self.table.load_data(data)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo obtener la información: {e}")

    def search_by_id(self):
        """Busca una canción específica por ID."""
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showwarning("Advertencia", "Ingrese el ID de la canción que desea buscar.")
            return

        try:
            response = requests.get(f"https://671be4322c842d92c381a5dc.mockapi.io/Music/{query}")
            response.raise_for_status()
            data = response.json()
            if data:
                # Asegúrate de pasar los datos en forma de lista
                self.table.load_data([data])
            else:
                messagebox.showinfo("Sin resultados", "No se encontró ninguna canción con ese ID.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo realizar la búsqueda: {e}")
