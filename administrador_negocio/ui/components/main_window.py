import customtkinter
from ui.components.tabview import MyTabView

#Ventana principal
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Config ventana
        customtkinter.set_appearance_mode("system")  # default
        self.title("Ventana principal")

        #TabView 4 pestañas
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0)
