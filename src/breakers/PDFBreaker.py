import ReportBreaker
import report_types.ReportType as ReportType

class PDFBreaker(ReportBreaker):

    def __init__(self, report_type : ReportType):
        super().__init__(report_type)

    def extract_content(self):
        texts = self.extract_texts()
        images = self.extract_images()
        arrays = self.extract_arrays()
        return {'texts' : texts, 'images' : images, 'arrays' : arrays}

    def extract_texts(self):
        ...

    def extract_images(self):
        ...

    def extract_arrays(self):
        ...