#requirments
#pip install pycryptodome
#pip install PyPDF2

import os
import PyPDF2

folder_path = r"C:\Users\muhammad\Desktop\files\Books-To-Print" #Change This
number_of_pages = []
pages_sum = 0
book_number = 1
# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            number_of_pages.append(num_pages)
            print(f"[{book_number}] {file_name}: {num_pages} pages")
        book_number += 1

for i in number_of_pages:
    pages_sum += i
print(f'[*] The Full Pages Sum is {pages_sum}')
