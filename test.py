import csv
import sys

def load_forbidden_words(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        forbidden_words = [row[0] for row in reader]  # assuming each forbidden word is on a new line
    return forbidden_words

def find_forbidden_words_in_html(forbidden_words, html_file):
    with open(html_file, 'r') as file:
        lines = file.readlines()
        
    results = []
    
    for i, line in enumerate(lines):
        for word in forbidden_words:
            if word in line:
                results.append(f"{word}: line {i + 1}")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <forbidden_words.csv> <document.html>")
        sys.exit(1)

    forbidden_words_file = sys.argv[1]
    html_file = sys.argv[2]
    
    forbidden_words = load_forbidden_words(forbidden_words_file)
    results = find_forbidden_words_in_html(forbidden_words, html_file)
    
    if results:
        for result in results:
            print(result)
    else:
        print("No forbidden words/phrases found.")


#csv_file = "C:\\Code Repository\\Code Bin Python\\Style Guide Phrases.csv"
#forbidden_words = load_forbidden_words(csv_file)
#html_file = "C:\\Code Repository\\Code Bin Python\\example.html"
#find_forbidden_words_in_html(forbidden_words, html_file)
