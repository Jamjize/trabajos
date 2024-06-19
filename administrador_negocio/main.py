import customtkinter
from ui.components.label_entry import LabelEntryFrame
from styles.fonts import Font, Size

class ViewTest(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label_entry = LabelEntryFrame(self)
        label_entry2 = LabelEntryFrame(self)

        label_entry.grid(row=0, column=0, pady=5)
        label_entry2.grid(row=1, column=0, pady=5)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        view = ViewTest(self)
        view.grid(row=0, column=0)


app = App()
app.mainloop()