from report.PDFReport import PDFReport

class Factsheet(PDFReport):

    def __init__(self, path : str = ""):
        super().__init__(path = path)
    