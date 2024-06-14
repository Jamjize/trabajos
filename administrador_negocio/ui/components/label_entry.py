import customtkinter
from styles.fonts import Font, Size


class LabelEntryFrame(customtkinter.CTkFrame):
    def __init__(
            self, 
            master,
            text: str="papaya",
            font_style: tuple=(Font.DEFAULT, Size.DEFAULT),
            alignment: str="left",
            entry_width: int=40,
            #num_components: int=1
        ):
        super().__init__(master)

        # self.text = text
        # self.font_style = font_style
        # #self.num_components = num_components
        # self.alignment = alignment
        # self.entry_width = entry_width


        self.label = customtkinter.CTkLabel(
            master=self,
            text=text,
            font=font_style,
            anchor=alignment
        )
        self.label.grid(row=0, column=0)

        self.entry = customtkinter.CTkEntry(master=self, width=entry_width)
        self.entry.grid(row=1, column=0)
