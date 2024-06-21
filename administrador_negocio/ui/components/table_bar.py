import customtkinter
from CTkTable import *


table_values = [
    ["Item", "Cantidad", "Unidad"],
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
    ["hamburguesa", 1, "u"]
    ]


class TableScrollbar(customtkinter.CTkScrollableFrame):
    def __init__(self, master, values: list, width: int=600, height: int=600, header_color: str="red"):
        super().__init__(master, width, height)
        #Configs
        self.values = values
        self.header_color = header_color
        #widget
        self.table = CTkTable(self, row=12, column=3, values=self.values, header_color=self.header_color)
        self.table.grid(row=0, column=0, padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Config
        self.geometry("600x600")
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1), weight=1)
        #Widget
        table_bar = TableScrollbar(self, values=table_values)
        table_bar.grid(row=0, column=0)

        table_bar2 = TableScrollbar(self, values=table_values)
        table_bar2.grid(row=1, column=0)

app = App()
app.mainloop()

