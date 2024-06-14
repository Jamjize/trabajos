import customtkinter

class LabelEntryFrame(customtkinter.CTkFrame):
    def __init__(
            self, 
            master,
            text: str="papaya",
            font_size: str=11,
            alignment: str="left",
            entry_width: int=40,
            num_components: int=1):
        super().__init__(master)
        self.text = text
        self.font_size = font_size
        self.num_components = num_components
        self.alignment = alignment
        self.entry_width = entry_width

    def create_component(self):
        for i in range(self.num_components):
            label = customtkinter.CTkLabel(
                master=self,
                text=self.text,
                font_size=self.font_size,
                anchor=self.alignment
            )
            entry = customtkinter.CTkEntry(master=self, width=self.entry_width)
