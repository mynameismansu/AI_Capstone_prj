import PdfToTxt

print("Hello World")
obj = PdfToTxt.Dataset()
obj.pdf_to_text()
print(obj.path)
print(len(obj.docs.keys()))