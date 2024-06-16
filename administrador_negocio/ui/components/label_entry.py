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
        widget_parameters_list: list=[[
            "text", 
            (Font.DEFAULT.value, Size.DEFAULT.value), 
            "center", 
            100,
        ]],
        orientation = "horiz",
        padx: int = 10,
        pady: int = 10
    ):
        super().__init__(master)
        self.widget_count: list = []
        self.orientation = orientation
        self.padx = padx
        self.pady = pady

        # --Creacion widgets--
        #* -parameters- es una lista[] con los parametros para el widget
        for i, parameters in enumerate(widget_parameters_list):
            self.label = customtkinter.CTkLabel(
                master=self,
                text=parameters[0],
                font=parameters[1],
                anchor=parameters[2]
            )
            self.entry = customtkinter.CTkEntry(master=self, width=parameters[3])
            # Acomodando widgets dentro del frame
            if self.orientation == "horiz":
                self.label.grid(row=0, column=i, padx=self.padx)
                self.entry.grid(row=1, column=i, padx=self.padx)
            else:
                self.label.grid(row=2*i+1, column=0, pady=(self.pady, 0))
                self.entry.grid(row=2*i+2, column=0, pady=(0, self.pady))
            self.widget_count.append((self.label, self.entry))
