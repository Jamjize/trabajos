import customtkinter
from CTkTable import *

class MyTable(CTkTable):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.table = CTkTable(
            master=self, 
            row=kwargs.get("row"), 
            column=kwargs.get("column"), 
            values=kwargs.get("values")
        )


class FrameTabInventory(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #Creando widgets
        self.lbl_description = customtkinter.CTkLabel(
            self, 
            text="Aqui puedes cargar los alimentos que tienes disponibles en tu inventario",
        )
        self.lbl_name = customtkinter.CTkLabel(
            self, text="Nombre del producto"
        )
        self.lbl_quantity = customtkinter.CTkLabel(
            self, text="Cantidad en inventario"
        )
        self.lbl_g = customtkinter.CTkLabel(self, text="g")

        self.tb_name = customtkinter.CTkEntry(self, placeholder_text="Ej Tomate")
        self.tb_quantity = customtkinter.CTkEntry(self, placeholder_text="Ej 100")
        
        self.btn_add = customtkinter.CTkButton(self, text="Ingresar", command=self.get_data)
        self.btn_clear = customtkinter.CTkButton(self, text="Limpiar")


        #Colocando los widgets
        self.lbl_description.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.lbl_name.grid(row=1, column=0, padx=10)
        self.lbl_quantity.grid(row=1, column=1, padx=10)
        self.lbl_g.grid(row=1, column=2, padx=(0, 5), sticky="w")

        self.tb_name.grid(row=2, column=0, padx=10)
        self.tb_quantity.grid(row=2, column=1, padx=(10,0))

        self.btn_add.grid(row=3, column=0, padx=10, pady=20)
        self.btn_clear.grid(row=3, column=1, padx=(10, 0), pady=20)

        #Tabla
        values, amout_row = self.get_data()
        self.table = MyTable(master=self, row=amout_row, column=2, values=values)
        self.table.grid(row=4, column=0, columnspan=3, padx=20, pady=20, sticky="nesw")

    def get_data(self):
        #product_name = self.tb_name.get()
        #product_quantity = self.tb_quantity.get()
        values = [["Nombre", "apellido"],
                  ["Leo", "Pucheta"],
                  ["Maxi", "Acuña"],
                  ["Pedro", "Picapiedra"],
                  ["Jugan", "Gomes"],
                  ["San", "Nicolas"],
                  ["Nicola", "Tezla"],]
        return values, 7
