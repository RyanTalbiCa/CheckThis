from report.finance.Factsheet import Factsheet
from breakers.PDFBreaker import PDFBreaker

if __name__ == '__main__':
    sample_factsheet_path = "samples/Finance/Factsheets/Dynasty-Global-Convertibles-Monthly-Report-April-2023.pdf"
    sample_factsheet = Factsheet(path = sample_factsheet_path)
    sample_factsheet.load()
    
    pdf_breaker = PDFBreaker()
    pdf_breaker.load_report(sample_factsheet)
    pdf_breaker.extract_content()