import customtkinter
from ui.components.label_entry import LabelEntryFrame
from styles.fonts import Font, Size

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")

        self.label_entry = LabelEntryFrame(
            master=self, 
            text="Hola", 
            font_style=(Font.BASE.value, Size.VERY_BIG.value), 
            alignment="center", 
            entry_width=250, 
            #num_components=1
        )
        self.label_entry.grid(row=0, column=0) 


app = App()
app.mainloop()