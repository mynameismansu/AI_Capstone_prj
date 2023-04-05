import fitz
import Config
import os


class Dataset:
    def __init__(self):
        self.path = os.getcwd()
        self.files = os.listdir(self.path + "/dataset")
        self.docs = {}

    def pdf_to_text(self):
        for file in self.files:
            doc = fitz.open(self.path + '/dataset/' + file)
            content = ""
            for page in doc:
                text = page.get_text().replace("\n", " ")
                text = text.replace("\xad", " ")  # deletion of unnecessary text
                content = content + text
            self.docs[file] = content

