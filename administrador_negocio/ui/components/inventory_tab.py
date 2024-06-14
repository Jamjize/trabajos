import customtkinter
from ui.components.my_table import MyTable

#Se pide ingrediente y cantidad
class LabelEnrtyInput(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_name = customtkinter.CTkLabel(self, text="Nombre del producto")
        self.label_quantity = customtkinter.CTkLabel(self, text="Cantidad en inventario")
        self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Ej Tomate")
        self.entry_quantity = customtkinter.CTkEntry(self, placeholder_text="Ej 100")

        #Posición
        self.label_name.grid(row=0, column=0, padx=10)
        self.label_quantity.grid(row=0, column=1, padx=10)
        self.entry_name.grid(row=1, column=0, padx=10)
        self.entry_quantity.grid(row=1, column=1, padx=(10, 0))

    def clear_enrty(self):
        self.entry_name.delete(0, "end")
        self.entry_quantity.delete(0, "end")


class ButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, master, label_entry):
        super().__init__(master)

        self.btn_add = customtkinter.CTkButton(self, text="Ingresar")
        self.btn_remove = customtkinter.CTkButton(self, text="Quitar")
        self.btn_clear = customtkinter.CTkButton(
            self,
            text="Limpiar texto",
            command=label_entry.clear_enrty
        )

        self.btn_add.grid(row=0, column=0, padx=10, pady=20)
        self.btn_remove.grid(row=0, column=1, padx=10, pady=20)
        self.btn_clear.grid(row=0, column=2, padx=10, pady=20)
    

class FrameInventoryTab(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_description = customtkinter.CTkLabel(
            self,
            text="Aquí puedes cargar los alimentos que tienes disponibles en tu inventario",
        )

        self.label_enrty_input = LabelEnrtyInput(master=self)
        self.buttons_frame = ButtonsFrame(master=self, label_entry=self.label_enrty_input)
        self.table = MyTable(master=self, row=2, column=2, values=[["Ingrediente", "Cantidad"]])

        #Aca donde colocamos la cosas
        self.label_description.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.label_enrty_input.grid(row=1, column=0)
        self.buttons_frame.grid(row=2, column=0)
        self.table.grid(row=3, column=0, columnspan=3, padx=20, pady=20, sticky="nesw")