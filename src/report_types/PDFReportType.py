from report_types.ReportType import ReportType

class PDFReportType(ReportType):

    def __init__(self):
        super().__init__(self, report_type = "pdf")
