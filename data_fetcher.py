# data_fetcher.py
import requests
from tkinter import messagebox

class DataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            # Imprime la estructura de datos para depuración
            print(data)
            return data
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Error al obtener datos: {e}")
            return []
