import tkinter as tk
from Controller import Controller
from screens.HomeScreen import HomeScreen
from screens.AddTestScreen import AddTestScreen
from screens.UpdateTestScreen import UpdateTestScreen

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

        pantallas = (HomeScreen, AddTestScreen, UpdateTestScreen)
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

    def home_to_update(self):
        new_options = self.get_test_names()
        self.frames[UpdateTestScreen].options.update_options(new_options)
        self.show_frame(UpdateTestScreen)

    
    ## Aqui empiezan los metodos de la BBDD

    def get_test_names(self):
        return self.controller.get_test_names()
    
    def add_question(self, test_name,question_text, question_choices, correct_choice):
        self.controller.add_question(test_name,question_text, question_choices, correct_choice)
