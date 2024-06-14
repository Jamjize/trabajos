import customtkinter
from ui.components.label_entry import LabelEntryFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

    def create_label_entry(self):
        label_entry = LabelEntryFrame(self, text="Hola", font_size="12", alignment="center", entry_width=30, num_components=1)
        label_entry.pack()  # Asegúrate de empaquetar el componente en la interfaz gráfica


app = App()
app.create_label_entry()
app.run()