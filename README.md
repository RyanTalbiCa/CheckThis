# CheckThis
This project aims to build an industry-level tool to automate reports comparison, integrity, errors and constraints checking on large amount of files in any given file format.

# Base pipeline
The project is organized around 4 main base classes. Those are the followings :
    Report : This class is intended to represent a concrete instance of a report to analyze. In particular it stores a reference to the content of a specific file.<br>
    ReportType : This class is intended to model a specific type of report, for instances factsheets, kid ucits or kid priips for finance.<br>
    ReportBreaker : This class is intended to extract predefined sections of a specific type of report. An instance of such an extraction is to extract images from a PDFReport.<br>
    Checker : This class performs a list of contraint checkings on a report instance of a specific report type.<br>
    Constraint : This class is intended to model any kind of integrity constraint that have to be checked on a specific type of report.<br>

Each of these classes have to be subclassed in order to be used.
