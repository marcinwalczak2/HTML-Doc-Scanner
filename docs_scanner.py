import PyPDF2

def extract_text_from_pdf(fordbidden_phrases_file, new_pdf_file):
    #query user for forbidden_phrases_file (either create a list in terminal or preferably create an interpreter that generates list based on word doc)
    #for new_pdf_file, query user for path to pdf file
    with open(fordbidden_phrases_file, 'r') as f:
        #opens forbidden_phrases_file as alias f; 
        fordbidden_phrases = [line.strip() for line in f]
        #creates list of phrases from f

    pdf_writer = PyPDF2.PdfFileWriter()
    #should be changed to use pydocs or whatever its called; will be adding new text in word doc
    pdf_reader = PyPDF2.PdfFileReader(new_pdf_file)

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        text = page.extract_text()

        for phrase in forbidden_phrases:
            if phrase in text:
                # Add an overlay to highlight the text
                # This is a simplified example, actual implementation may vary
                page.merge_page(page)

        pdf_writer.addPage(page)

    with open('highlighted.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)



forbidden_phrases = []
for line in fordbidden_phrases_file:
    fordbidden_phrases = forbidden_phrases.append(line.strip())
