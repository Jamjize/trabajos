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
        self.label_entry2 = LabelEntryFrame(
            master=self, 
            text="Adios", 
            font_style=(Font.BASE.value, Size.DEFAULT.value), 
            alignment="w", 
            entry_width=300, 
            #num_components=1
        )
        self.label_entry3 = LabelEntryFrame(self)
        self.label_entry.grid(row=0, column=0)
        self.label_entry2.grid(row=0, column=1)
        self.label_entry3.grid(row=0, column=2)


app = App()
app.mainloop()