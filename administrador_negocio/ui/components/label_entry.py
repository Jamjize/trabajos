import customtkinter
from styles.fonts import Font, Size

"""
TODO: hacer que la clase sirva para crear varias instancias, a partir de listas
TODO: Si llegase el caso, que tengas que generar algo para que te pida si tenés
TODO: que pedir si se crean vertical u horizontal hacelo.
"""

class LabelEntryFrame(customtkinter.CTkFrame):
    def __init__(
            self, 
            master,
            text: str="papaya",
            font_style: tuple=(Font.DEFAULT.value, Size.DEFAULT.value),
            alignment: str="e",
            entry_width: int=100,
            #num_components: int=1
        ):
        super().__init__(master)

        #Widgets
        self.label = customtkinter.CTkLabel(
            master=self,
            text=text,
            font=font_style,
            anchor=alignment
        )
        self.label.grid(row=0, column=0)

        self.entry = customtkinter.CTkEntry(master=self, width=entry_width)
        self.entry.grid(row=1, column=0)
