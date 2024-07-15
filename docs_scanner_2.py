from docx import Document
from bs4 import BeautifulSoup
import pandas as pd
from docx.shared import RGBColor


def fp_interpreter():
    forbidden_phrases = print("File Location:")
    df = pd.read_csv(forbidden_phrases)
    forbidden_phrases_csv = df['phrase'].tolist()
    return forbidden_phrases_csv

forbidden_phrases_csv = fp_interpreter()

def highlight_phrases(forbidden_phrases, html_file, output_doc):
    df = pd.read_csv(forbidden_phrases_csv)
    forbidden_phrases = set(df['phrase'])

    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text()

    doc = Document()
    for line in text_content.splitlines():
        # Add the line to the document
        paragraph = doc.add_paragraph(line)

        # Highlight the forbidden phrases in the line
        for phrase in forbidden_phrases:
            start = 0
            while True:
                start = line.lower().find(phrase.lower(), start)
                if start == -1:
                    break
                paragraph.runs[start:start+len(phrase)].font.highlight_color = RGBColor(255, 255, 0)
                start += len(phrase)

    doc.save(output_doc)
    # ask user for path where they want to save this doc

forbidden_phrases_test = r"C:\Code Repository\Code Bin Python\Style Guide Phrases.csv"
html_file = r"C:\Code Repository\Code Bin Python\example.html"
output_doc = r"C:\\Code Repository\Code Bin Python\Style Guide Phrases.csv"
highlight_phrases(forbidden_phrases_test, html_file, output_doc)

#first ask for variable "Doc" which will be the file path. 

def get_user_input():
    user_input = input("Please enter something: ")
    return user_input

