import tkinter as tk
import tkinter.messagebox

from sqlite3 import ProgrammingError
from style import styles
from components.MainMenu import MainMenu

class AddTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.manager = manager
        self.init_widgets()
    def init_widgets(self):
        tk.Label(
            self,
            text="Introduce el nombre del nuevo test",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
##      Para entrar el nuevo test
        self.test_entry = tk.Entry(
            self,
            justify=tk.CENTER,
            **styles.STYLE
        )
        self.test_entry.pack(
            **styles.PACK
        )
##      Para utilizar el enter del teclado
        self.test_entry.bind("<Return>", self.add_test)
##      Menu de navegacion
        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )
##  Metodo para ejecutar la entrada de texto
    def add_test(self, event):
        test_name = self.test_entry.get()
        if test_name =="":
            tk.messagebox.showinfo(
                title="ERROR",
                message="El nombre de test no puede estar vacio"
            )
        else:
            try:
                self.manager.controller.create_empty_test(test_name)
                tk.messagebox.showinfo(
                    title="SUCCESS",
                    message=f"El test {test_name} ha sido creado"
                )
            except ProgrammingError:
                tk.messagebox.showinfo(
                    title="ERROR",
                    message="Ya existe un test con este nombre. Prueba otro"
                )
            finally:
                print(test_name)



