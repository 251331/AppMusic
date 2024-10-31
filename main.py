# main.py
import tkinter as tk
from music_app import MusicApp

def main():
    root = tk.Tk()
    app = MusicApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
