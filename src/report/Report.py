import report_types.ReportType as ReportType

class Report:
    """This class is meant to represent a concrete report instance.
        A report belongs to a ReportType and is loaded from its path.
    """

    def __init__(self, report_type : ReportType, path : str = ""):
        self.report_type = report_type
        self.path = path
        self.report_content = None

    def load(self):
        raise NotImplemented("The load method must be redefined in Report subclasses...")
    
    def get_report_content(self):
        return self.report_content