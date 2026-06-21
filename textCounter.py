# Frequency Counter: Description
# python -m pip install pypdf

### Define a Steing - Load the contents of the PDF into a string
from pypdf import PdfReader
import re


### Define the class for the task called 'TextAnalyzer' and its attributes
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        # make text lowercase
        formatted_text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        formatted_text = formatted_text.lower()
        self.text = formatted_text
        
    def freqAll(self):        
        # split text into words
        words_list = self.text.split()
        
        # Create dictionary
        word_freq = {}

        for word in set(words_list):
            word_freq[word] = words_list.count(word)

        return word_freq
    
    def freqOf(self, word):
        # get frequency map
        freq_dic = self.freqAll()
        if word in freq_dic:
            return freq_dic[word]
        else:
            return 0   


PDF_NAME = "mypdf.pdf"
def main():
    # Read a pdf
    reader = PdfReader(PDF_NAME)
    content = ""
    # take each page and concatenate with the string
    for page in reader.pages:
        text = page.extract_text()
        content += text

    # print string
    # print(content)
    
    word = 'Amay'
    text_analyzer = TextAnalyzer(content)
    print(f"String with text from PDF:\n\n {text_analyzer.text}\n\n")
    print(f"Frequency of the words in the PDF: \n\n {text_analyzer.freqAll()}\n\n")
    print(f"Frequency of the word: {word}, in the PDF:\n {text_analyzer.freqOf(word)}\n")

    
if __name__ == '__main__':
    main()