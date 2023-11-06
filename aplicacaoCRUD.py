import tkinter as tk
from tkinter import ttk
import crud as crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.lblCodigo=tk.Label(win, text="Código do Produto: ")
        self.lblNome=tk.Label(win, text="Nome do produto: ")
        self.lblPreco=tk.Label(win, text="Preço: ")

        self.txtCodigo=tk.Entry(bd=3)
        self