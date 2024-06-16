import customtkinter
from ui.components.label_entry import LabelEntryFrame
from styles.fonts import Font, Size

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")

        self.label_entry_1 = LabelEntryFrame(self, [["hola", (Font.DEFAULT.value, Size.DEFAULT.value), "center", 100], ["hola", (Font.DEFAULT.value, Size.DEFAULT.value), "center", 100], ["hola", (Font.DEFAULT.value, Size.DEFAULT.value), "center", 100]], orientation="vert", padx=10, pady=5)
        self.label_entry_1.grid(row=0, column=0)



app = App()
app.mainloop()