from report_types.ReportType import ReportType


from report.Report import Report

class ReportBreaker:
    """ This class is meant to be the base class to specialized report breakers.
        A report breaker takes a file as input (matching a well known ReportType) then extract and classify its content based on data types.
        Such a breaker could for instance take PDF reports as inputs and break their content down into images, texts, arrays lists... 
    """

    def __init__(self, report_type : ReportType):
        self.report_type = report_type

    def load_report(self, report : Report):
        self.report = report.get_report_content()

    def check_report_type(self):
        if self.report.report_type is self.report_type:
            return
        raise TypeError("The report type does not mach the breaker expected input.")

    def extract_content(self):
        raise NotImplemented("This function must be redefined in ReportBreaker subclasses.")