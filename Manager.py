import tkinter as tk
from Controller import Controller
from screens.HomeScreen import HomeScreen

from screens.AddTestScreen import AddTestScreen
from style import styles

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Exámenes de Submarinismo")
        self.controller = Controller()
        container = tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(
            background=styles.BACKGROUND
        )
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        self.frames = {}

        pantallas = (HomeScreen, AddTestScreen)
        for F in pantallas:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.show_frame(HomeScreen)
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    ## Aqui empiezan las transiciones de pantalla

    def home_to_create(self):
        self.show_frame(AddTestScreen)
