from CTkTable import *

class MyTable(CTkTable):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.table = CTkTable(
            master, 
            row=kwargs.get("row"), 
            column=kwargs.get("column"), 
            values=kwargs.get("values")
        )
