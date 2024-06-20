import customtkinter
from ui.components.label_entry import LabelEntryFrame
from styles.fonts import Font, Size


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

app = App()
app.mainloop()