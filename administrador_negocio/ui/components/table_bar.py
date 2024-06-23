import customtkinter
from CTkTable import *


table_values = [
    ["pizza", 30, "u"],
    ["Manaos cola", 20, "Ltrs"],
    ["pan", 2, "kg"],
    ["queso", 0.5, "kg"],
    ["tomate", 1, "kg"],
    ["lechuga", 0.3, "kg"],
    ["pollo", 1, "kg"],
    ["mayonesa", 0.2, "kg"],
    ["ketchup", 0.2, "kg"],
    ["mostaza", 0.1, "kg"],
    ["hamburguesa", 1, "u"],
    ["teta", 2, "3"]
]


class TableAndScrollbar(customtkinter.CTkScrollableFrame):
    def __init__(self, master, values: list):
        super().__init__(master)
        self.table_values = values
        self.table = CTkTable(
            self,
            row=len(self.table_values),
            column=3,
            values=self.table_values,
            corner_radius=1
        )
        self.table.grid(row=0, column=0)


class TableFrameContainer(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        #Variables
        self.header_values = [["Item", "Cantidad", "Unidad"]]
        #Widgets
        self.decorator_table = CTkTable(
            self,
            values=self.header_values,
            header_color="red",
            corner_radius=1
        )
        self.table_bar = TableAndScrollbar(self, values=table_values)
        #Grid
        self.decorator_table.grid(row=0, column=0)
        self.table_bar.grid(row=1, column=0, sticky="we")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.table = TableFrameContainer(self)
        self.table.grid(row=0, column=0)
        self.table2 = TableFrameContainer(self)
        self.table2.grid(row=0, column=1)
        self.table3 = TableFrameContainer(self)
        self.table3.grid(row=1, column=0)


app = App()
app.mainloop()