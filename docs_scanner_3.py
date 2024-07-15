from bs4 import BeautifulSoup
import pandas as pd
import csv
import sys

def fp_interpreter(file_path):
    #forbidden_phrases = input("File Location:") <- maybe add this as a future feature where the user is asked Do you want to use default list: y/n
    #if no, then the user is prompted with the input function above and can add their own file path/custom csv
    df = pd.read_csv(file_path, header=None)
    forbidden_phrases_csv = df[0].tolist()
    return forbidden_phrases_csv

forbidden_phrases_test = "C:\\Code Repository\\Code Bin Python\\Style Guide Phrases.csv"
forbidden_phrases_csv = fp_interpreter(forbidden_phrases_test)
doc= "C:\\Code Repository\\Code Bin Python\\example.html"

def doc_scanner(forbidden_phrases, doc):
    """This function scans each line in the html file "doc" and ensures there are no instances of any forbidden phrases in the "forbidden_phrases" list"""
    with open(doc, 'r') as file:
        lines = file.readlines()
    results = []
    for phrase in forbidden_phrases:
        forbidden_phrase = phrase
        for i in range(len(lines)):
            if forbidden_phrase in lines[i]:
                line = lines[i]
                index = 0
                while True:
                    #this checks for multiple instances of the same forbidden phrase on a single line in the html doc. The find method starts from index;
                    #at each instance of a forbidden phrase, the loop calls the find method again from the ending index of the previously found forbidden phrase.
                    #if the find method finds no forbidden phrases, index will == -1, which will break the infinite while loop.
                    index = line.find(forbidden_phrase, index)
                    if index < 0:
                        break
                    fp_result2 = forbidden_phrase + " : line " + str(index + 1)
                    results.append(fp_result2)
                    index += len(forbidden_phrase)
    return results

finalresult = doc_scanner(forbidden_phrases_csv, doc)
print(finalresult)



    

#use default csv? (respond Yes or No)
#if no enter file path. if yes 
