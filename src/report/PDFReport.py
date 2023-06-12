import pdfplumber


import Report

class PDFReport(Report):

    def __init__(self, path : str = ""):
        super().__init__(report_type = "pdf", path = path)

    def load(self):
        self.report_content = pdfplumber.open(self.path)
        return self.report_content