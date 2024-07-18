#NOTES:
#some words are split incorrectly, i believe it's because of the way the text is extracted from the pdf? not sure though

import PyPDF2
import os

path = os.path.dirname(os.path.abspath(__file__))
file_handle = open(path + "/Sense-and-Sensibility-by-Jane-Austen.pdf", "rb") 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 

frequency_table = dict() #new dictionary to store keys

def is_not_chapter(word):  #checks if word is a chapter heading
    if "CHAPTER" in word:
        return False
    else:
        return True
    
def is_not_link(word):  #checks is word is a link
    if "www" in word:
        return False
    else:
        return True
    
def remove_non_alpha(word):  #removes non alphabetical parts of words
    return ''.join([char for char in word if char.isalpha()])

for i in range(page_number):
    lines = pdfReader.pages[i].extract_text().split('\n')   #split each page into lines
    for line in lines:
        words = line.split()  #split lines into a list of words
        for word in words:   
            word = remove_non_alpha(word)   #remove non alphabetical parts
            if word and is_not_chapter(word) and is_not_link(word):   #check if word is a chapter or link
                word = word.lower()  #lowercase to simplify
                if word in frequency_table:
                    frequency_table[word] += 1   # +1 to value if key already exists in dictionary
                else:
                    frequency_table[word] = 1  #else set value of new key to 1

for word in frequency_table:
    print(f'{word} : {frequency_table[word]}') #cut output since i think the terminal can't handle that many lines?

print(frequency_table) #full output