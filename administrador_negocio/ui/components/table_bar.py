import customtkinter
from CTkTable import *


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
    def __init__(self, master, table_values: list):
        super().__init__(master)
        #Variables
        self.header_values = [["Item", "Cantidad", "Unidad"]]
        self.table_values = table_values
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


