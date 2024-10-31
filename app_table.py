import tkinter as tk
from tkinter import ttk

class AppTable:
    def __init__(self, parent):
        # Crear la tabla
        self.table = ttk.Treeview(parent, columns=("ID", "Canción", "Género", "Origen", "Artista"), show="headings", height=15)
        self.setup_table()

        # Crear la barra de desplazamiento
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)

        # Ubicar la tabla y la barra de desplazamiento
        self.table.grid(row=1, column=0, columnspan=4, sticky="nsew")
        scrollbar.grid(row=1, column=4, sticky="ns")

        # Estilo de colores pastel para la tabla
        style = ttk.Style()
        style.configure("Treeview", background="#e6f0fa", fieldbackground="#e6f0fa", foreground="#333")
        style.map('Treeview', background=[('selected', '#c0d9f7')])

    def setup_table(self):
        # Configurar los encabezados
        self.table.heading("ID", text="ID")
        self.table.heading("Canción", text="Canción")
        self.table.heading("Género", text="Género")
        self.table.heading("Origen", text="Origen")
        self.table.heading("Artista", text="Artista")

        # Ajuste de ancho de columnas
        self.table.column("ID", width=50, anchor="center")
        self.table.column("Canción", width=200)
        self.table.column("Género", width=150)
        self.table.column("Origen", width=150)
        self.table.column("Artista", width=150)

    def load_data(self, data):
        # Limpiar datos previos
        for row in self.table.get_children():
            self.table.delete(row)

        # Insertar nuevos datos
        for item in data:
            song_id = item.get("ID", "N/A")
            name = item.get("Cancion", "N/A")
            genre = item.get("Genero", "N/A")
            origin = item.get("Origen", "N/A")
            artist = item.get("Artista", "N/A")

            self.table.insert("", "end", values=(song_id, name, genre, origin, artist))
