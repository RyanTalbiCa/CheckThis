import Checker
from checkers.TextChecker import TextChecker

class ArrayChecker(Checker):
    """" This class is meant to check integrity constraints on arrays. """

    def __init__(self, arrays : list= None, fonts : list = None, font_sizes : list = None):
        self.arrays = arrays
        self.fonts = fonts
        self.font_sizes = font_sizes
        
        
    def check(self):
        ...

    def check_arrays_texts(self):
        tests_passed = True
        texts_to_check = []
        for array in self.arrays:
            for texts in array.get_texts():
                texts_to_check.append(texts)
        text_checker = TextChecker(texts = texts_to_check, fonts = self.fonts, font_sizes = self.font_sizes)
        return text_checker.check()
