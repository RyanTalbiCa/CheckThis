from pathlib import Path

class ReportType:

    def __init__(self, file_format : str):
        self.file_format = file_format

    def load(self, filename: Path):
        if self.file_format == "pdf":
            ...

