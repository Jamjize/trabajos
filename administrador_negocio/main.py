import customtkinter
from ui.components.table_bar import *
from DB.sql_connect_example import *

"""
TODO: Programar boton para agregar cosas a la BD
TODO: Programar boton para quitar cosas de la DB
TODO: TABLE_BAR: HCAER QUE LA TABLA SE ACTUALICE
!TERMINAR: de hacer que se muestren los productos por consola
!Luego hacer que se muestren en la tabla
"""

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.label_nombre = customtkinter.CTkLabel(self, text="Nombre producto")
        self.label_cantidad = customtkinter.CTkLabel(self, text="Cantidad")
        self.label_simbolo = customtkinter.CTkLabel(self, text="Unidad")
        self.entry_nombre = customtkinter.CTkEntry(self, placeholder_text="queso")
        self.entry_cantidad = customtkinter.CTkEntry(self, placeholder_text="40")
        self.entry_unidad = customtkinter.CTkEntry(self, placeholder_text="kg/g/u")
        self.btn_agregar = customtkinter.CTkButton(self, text="Agregar", command=self.agregar_item)
        self.btn_eliminar = customtkinter.CTkButton(self, text="Eliminar", command=self.eliminar_item)

        self.label_nombre.grid(row=0, column=0)
        self.label_cantidad.grid(row=0, column=1)
        self.label_simbolo.grid(row=0, column=2)
        self.entry_nombre.grid(row=1, column=0)
        self.entry_cantidad.grid(row=1, column=1)
        self.entry_unidad.grid(row=1, column=2)
        self.btn_agregar.grid(row=2, column=0)
        self.btn_eliminar.grid(row=2, column=2)

    def agregar_item(self):
        #Obtener datos
        name = self.entry_nombre.get()
        cant = self.entry_cantidad.get()
        unidad = self.entry_unidad.get()
        #Abrir DB
        crear_tabla_productos()
        #Meter datos
        insertar_producto(nombre=name, cantidad=cant, unidad=unidad)
        #Cerrar DB

    def eliminar_item(self) -> None:
        None

app = App()
app.mainloop()