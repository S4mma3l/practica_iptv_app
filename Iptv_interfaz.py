import subprocess
import streamlink
import tkinter as tk
from tkinter import ttk

class ReproductorIPTVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor IPTV")

        # Crear variables de control
        self.url_var = tk.StringVar()
        self.nombre_canal_var = tk.StringVar()
        self.canales_var = tk.StringVar(value=["Canal 1", "Canal 2", "Canal 3"])  # Puedes inicializar con tus canales

        # Crear widgets
        self.label_url = ttk.Label(root, text="URL de la transmisión IPTV:")
        self.label_url.pack(pady=5)

        self.entry_url = ttk.Entry(root, textvariable=self.url_var, width=40)
        self.entry_url.pack(pady=5)

        self.boton_reproducir = ttk.Button(root, text="Reproducir", command=self.reproducir)
        self.boton_reproducir.pack(pady=5)

        self.label_canales = ttk.Label(root, text="Lista de Canales:")
        self.label_canales.pack(pady=5)

        self.lista_canales = tk.Listbox(root, listvariable=self.canales_var, selectmode=tk.SINGLE)
        self.lista_canales.pack(pady=5)

        # Agregar scrollbar para la lista de canales
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.lista_canales.yview)
        self.lista_canales.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Entrada para el nombre del canal
        self.label_nombre_canal = ttk.Label(root, text="Nombre del Canal:")
        self.label_nombre_canal.pack(pady=5)

        self.entry_nombre_canal = ttk.Entry(root, textvariable=self.nombre_canal_var, width=40)
        self.entry_nombre_canal.pack(pady=5)

        # Botón para agregar canal
        self.boton_agregar_canal = ttk.Button(root, text="Agregar Canal", command=self.agregar_canal)
        self.boton_agregar_canal.pack(pady=5)

    def obtener_url_transmision(self, url):
        streams = streamlink.streams(url)
        if streams:
            return streams['best'].url

        return None

    def reproducir(self):
        url_transmision_iptv = self.url_var.get()
        canal_seleccionado = self.lista_canales.curselection()

        if not canal_seleccionado:
            print("Selecciona un canal.")
            return

        nombre_canal = self.lista_canales.get(canal_seleccionado)
        print(f"Reproduciendo {nombre_canal} desde {url_transmision_iptv}")

        url_transmision = self.obtener_url_transmision(url_transmision_iptv)

        if url_transmision:
            subprocess.call(["C:/Program Files/VideoLAN/VLC/vlc.exe", url_transmision])  # Requiere VLC instalado
        else:
            print("No se pudo obtener la transmisión.")

    def agregar_canal(self):
        nuevo_canal = self.nombre_canal_var.get()
        if nuevo_canal:
            canales_actuales = self.canales_var.get()
            canales_actuales.append(nuevo_canal)
            self.canales_var.set(canales_actuales)
            self.nombre_canal_var.set("")
        else:
            print("Ingresa un nombre para el canal.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReproductorIPTVApp(root)
    root.mainloop()