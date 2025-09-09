import customtkinter as ctk
from tkinter import filedialog
import os

def selecionar_arquivo():
    ctk.set_appearance_mode("system")  # "dark" ou "light"
    root = ctk.CTk()  
    root.withdraw()

    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[
            ("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp;*.svg"),
            ("Todos os arquivos", "*.*")
        ]
    )

    # Retorna o caminho completo
    if caminho_arquivo:
        return caminho_arquivo
    return None
