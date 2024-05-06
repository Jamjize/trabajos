import customtkinter


#Frame con widgets que van dentro de los tabs
class FrameTabIventory(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.lbl_description = customtkinter.CTkLabel(
            self, 
            text="Aqui puedes cargar los alimentos que tienes disponibles en tu inventario",
        )
        #Label Nombre y cantidad
        self.lbl_name = customtkinter.CTkLabel(
            self, text="Nombre del producto"
        )
        self.lbl_quantity = customtkinter.CTkLabel(
            self, text="Cantidad en inventario"
        )
        self.lbl_g = customtkinter.CTkLabel(self, text="g")

        #Cajas de texto
        self.tb_name = customtkinter.CTkEntry(self, placeholder_text="Ej Tomate")
        self.tb_quantity = customtkinter.CTkEntry(self, placeholder_text="Ej 100")
        
        #Botones
        self.btn_add = customtkinter.CTkButton(self, text="Ingresar", command=self.get_data)
        self.btn_clear = customtkinter.CTkButton(self, text="Limpiar")

        #Colocando widgets
        self.lbl_description.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.lbl_name.grid(row=1, column=0, padx=10)
        self.lbl_quantity.grid(row=1, column=1, padx=10)
        self.lbl_g.grid(row=2, column=2, padx=(0, 5), sticky="w")

        self.tb_name.grid(row=2, column=0, padx=10)
        self.tb_quantity.grid(row=2, column=1, padx=(10,0))

        self.btn_add.grid(row=3, column=0, padx=10, pady=20)
        self.btn_clear.grid(row=3, column=1, padx=(10, 0), pady=20)

    def get_data(self):
        #Recuperar datos de los txtbox
        product_name = self.tb_name.get()
        product_quantity = self.tb_quantity.get()
        
        

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
        self.inventory_frame = FrameTabIventory(master=self.tab("inventario"))
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
