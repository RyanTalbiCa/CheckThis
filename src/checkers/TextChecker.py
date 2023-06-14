import Checker

class TextChecker(Checker):
    """" This class is meant to check integrity constraints on texts. """

    def __init__(self, texts : list = None, fonts : list = None, font_sizes : list = None):
        self.texts = texts

    def check(self):
        font_check = self.check_fonts()
        font_size_check  = self.check_font_sizes()
        return font_check and font_size_check

    def check_fonts(self):
        ...

    def check_font_sizes(self):
        ...
