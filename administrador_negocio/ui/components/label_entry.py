import customtkinter
from styles.fonts import Font, Size


class LabelEntryFrame(customtkinter.CTkFrame):
    def __init__(self, 
        master, 
        text: str="hello", 
        font: str=Font.DEFAULT.value, 
        size: str=Size.DEFAULT.value,
        text_position: str="center",
        entry_width: int=100,
        hint_text: str="your text"
        ):
        super().__init__(master)
        #--Parametros--
        #Label
        self.text = text
        self.font = (font, size)
        self.text_position = text_position
        #Entry
        self.entry_width = entry_width
        self.hint_text = hint_text
        #widget
        self.label = customtkinter.CTkLabel(self,
            text=self.text,
            font=self.font, 
            anchor=self.text_position
            )
        self.entry = customtkinter.CTkEntry(self,
            width=self.entry_width,
            placeholder_text=self.hint_text
            )
        #grid
        self.label.grid(row=0, column=0, sticky="we")
        self.entry.grid(row=1, column=0)
