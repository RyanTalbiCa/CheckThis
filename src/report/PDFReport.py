import pdfplumber


from report.Report import Report
from report_types.PDFReportType import PDFReportType

class PDFReport(Report):

    def __init__(self, path : str = ""):
        super().__init__(self, report_type = PDFReportType, path = path)

    def load(self):
        self.report_content = pdfplumber.open(self.path)
        return self.report_content