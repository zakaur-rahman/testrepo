from pdfminer.high_level import extract_text
import subprocess
import sys
import re
import fnmatch
from pickle import TRUE
import PIL
from PIL import Image
import tkinter
from tkinter import MULTIPLE, messagebox
from tkinter import filedialog
import os
import textractplus as tp

# Define path to image
path_to_images = filedialog.askopenfilename(multiple=True)  # saving path of the file location

#Iterate over each file_name in the folder
for file_name in path_to_images:
   
    
    path = r"{}".format(file_name)     # Changing path into String
    
    pdf = re.findall(".pdf", path)           # Checkin for PDF file
     
    docx = re.findall(".docx", path)          # Checking for Docx formated files
    
    doc = re.findall(".doc", path)             # Checking for Doc formated files
    
    PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')   #Regular expression for phone no
    
    def extract_phone_number(resume_text):      #function for phone Number
        phone = re.findall(PHONE_REG, resume_text)
 
        if phone:
           number = ''.join(phone[0])
 
           if resume_text.find(number) >=0  and len(number) < 16:
              return number
        return None
    
    if pdf:
        def extract_text_from_pdf(path):
            return extract_text(path)
        if __name__ == '__main__':
           text = extract_text_from_pdf(path)  # Extracted data from pdf files
           print(text)
           phone_number=extract_phone_number(text)
           print(phone_number)
    
    elif docx or doc:
        def extract_text_from_doc_docx(path):  #Extract data from doc or docx files
          text = tp.process(path)
          return text.decode("utf-8")
        if __name__ == '__main__':
           text=extract_text_from_doc_docx (path)
           phone_number=extract_phone_number(text)
           print(phone_number)
    else:
      print("Enter file in correct formatt.")