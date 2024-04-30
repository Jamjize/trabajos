import customtkinter

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ventana principal")
        #self.geometry("600x400")
        
        contenedor_pestañas = customtkinter.CTkTabview(self)
        contenedor_pestañas.grid(row=0, column=0)

        contenedor_pestañas.add("menú")
        contenedor_pestañas.add("venta")

        boton = customtkinter.CTkButton(contenedor_pestañas.tab("menú"))
        boton.grid(row=1, column=0)






app = app()
app.mainloop()
