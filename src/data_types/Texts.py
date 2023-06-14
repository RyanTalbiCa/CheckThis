from data_types.DataType import DataType


class Text(DataType):

    def __init__(self, font : str = None, font_size : int = None, text : str = None):
        self.font = font
        self.font_size = font_size
        self.text : str = text

    def get_font(self):
        return self.font

    def get_font_size(self):
        return self.font_size  
    
    