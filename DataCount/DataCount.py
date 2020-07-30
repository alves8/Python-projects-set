
############ extract_doc_info.py  ##################

from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

import re

# Open the file and save it in a variable (wordCount) to obtain the string.
with open('text.txt', 'r') as file1:
    wordCount = file1.read()

print(type(wordCount))

print(wordCount)
# index each element by a value.
y = []
# separate letters by space
x = re.sub('[:,.!@#$]', '', wordCount)

x = wordCount.split()
print(type(x))
size = len(x)


print("Number of times the word is repeated")
for i in range(0, size):
    k=1
    for j in range(0, size):
        
        
        if (x[i] != " " and x[j] != " " and x[i] == x[j]):
           k += 1    
        
    print(x[i], ":", k, "x", ((k/size)*100),"%")

