import customtkinter

from GUI.inventory_tab import FrameTabInventory


#Clase con 4 pestañas
class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        
        #Creando pestaañs
        self.add("menú")
        self.add("ventas")
        self.add("inventario")
        self.add("ganancias")

        #Poniendo un frame para la pestaña inventario
        self.inventory_frame = FrameTabInventory(master=self.tab("inventario"))
        self.inventory_frame.grid(row=0, column=0)


#ventana principal y un tabview
class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system")  # default
        self.title("Ventana principal")

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0)


app = app()
app.mainloop()
