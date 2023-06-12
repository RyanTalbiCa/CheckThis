import ReportType

class PDFReportType(ReportType):

    def __init__(self):
        super().__init__(report_type = "pdf")
