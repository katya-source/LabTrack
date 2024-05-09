import os
from PyPDF2 import PdfReader
from ux_functions import print_categories,print_valid_path

class FileManager:
    def __init__(self):
        self.filepath = ''

    @property
    def filepath(self):
        return self._filepath
    
    @filepath.setter
    def filepath(self,filepathname):
        self._filepath=filepathname

    def is_valid_path(path):
        is_valid = os.path.isdir(path)
        if is_valid:
            message = (f"\nFolder is found:\n{path}\n")
        else:
            message = (f"\nFolder is not found:\n{path}\n"
                       "Check and try again.")
        print_valid_path(is_valid, message)
        # return is_valid
        return is_valid, path if is_valid else None

    def is_valid_pdf(path):
        result = {"Valid": [],
                  "Invalid": []}

        for filename in os.listdir(path):
            if filename.endswith(".pdf"):
                try:
                    with open(os.path.join(path, filename), "rb") as file:
                        pdf = PdfReader(file)
                        info = pdf.metadata
                        if info.title == "E. sveikatos portalas":
                            result["Valid"].append(filename)
                        else:
                            result["Invalid"].append(filename)
                except Exception:
                    result["Invalid"].append(filename)
        if not any(result.values()):
            result["Message"] = ["Couldn\'t find any PDF file inside."]
        elif not result["Valid"]:
            result["Message"] = ["\nProvided PDFs don\'t meet requirements.\n"
                                 "Pls check README file. "
                                 "Otherwise, try again."]

        print_categories(result)
        return result