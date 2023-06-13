from breakers.ReportBreaker import ReportBreaker
from report.PDFReport import PDFReport

class PDFBreaker(ReportBreaker):

    def __init__(self):
        super().__init__(PDFReport)

    def extract_content(self):
        if self.report is None:
            return
        
        texts = self.extract_texts()
        images = self.extract_images()
        arrays = self.extract_arrays()
        return {'texts' : texts, 'images' : images, 'arrays' : arrays}

    def extract_texts(self):
        pages_texts = {}

        for index, page in enumerate(self.report.pages):
            pages_texts[index] = page.extract_text()

        return pages_texts

    def extract_images(self):
        pages_images = {}

        for index, page in enumerate(self.report.pages):
            pages_images[index] = page.images

        return pages_images

    def extract_arrays(self):
        pages_arrays = {}
        
        for index, page in enumerate(self.report.pages):
            pages_arrays[index] = page.images
        
        return pages_arrays
