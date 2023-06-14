from pathlib import Path

class ReportType:
    """ This class is intended to model a report type.
        A report type is defined by its file format, and a list of sections, each sections can hold one or several kind of data.
        The ReportType class is meant to be inherited, each subclass having to define the list of its sections and the content of thoses sections.
        For this the ReportType subclasses must define a dictionnary which holds a mapping linking sections names to fields name.

        An instance of such a report is given by the Factsheets which are marketing reports used in the financial industry.
        A factsheet make appears a monthly commentary which is a text, some plots, ...
    """
    
    def __init__(self, file_format : str):
        self.file_format = file_format
        

