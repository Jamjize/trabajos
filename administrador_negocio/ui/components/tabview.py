import customtkinter
from ui.components.inventory_tab import FrameInventoryTab #Importamos GUI inventario


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)

        # Creando pestañas
        self.add("menú")
        self.add("ventas")
        self.add("inventario")
        self.add("ganancias")

        # GUI del inventario en la pestaña correspondiente
        self.inventory_frame = FrameInventoryTab(master=self.tab("inventario"))
        self.inventory_frame.grid(row=0, column=0)