import pdfplumber


import Report
import report_types.PDFReportType as PDFReportType

class PDFReport(Report):

    def __init__(self, path : str = ""):
        super().__init__(report_type = PDFReportType, path = path)

    def load(self):
        self.report_content = pdfplumber.open(self.path)
        return self.report_content