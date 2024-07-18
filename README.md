# About Docscanner
Docscanner allows you to streamline your documentation workflow by detecting words or phrases listed in a _.csv_ file in an inputted _.html_ file. If any words/phrases are detected, Docscanner returns both the word/phrase as well as the line number that it is located on. This helps eliminate human error when applying style guide content standards in a documentation project. 

The script is case insensitive and is also capable of finding duplicate words/phrases on the same line in the _.html_ file. 

## Installing Docscanner
If you haven't already, download Python [here](https://www.python.org/downloads/).  
Install Docscanner by running the following in a terminal:  
`pip install doc-scanner`

## Using Docscanner
1. Enter the following in your terminal:  
`python docscanner.py`  
2. You will be prompted with the following:  
`Use default csv file of forbidden phrases? (respond Y or N): `  
    - To use the default csv file, type "Y". It will automatically jump to the next argument where you input the _.html_ file path.  
    - To use a custom csv file, type "N". You will be prompted with the following:  
`Enter path of your custom csv file: `  
Copy the path from File Explorer by holding \<SHIFT\>, right-clicking your desired file, and selecting __Copy as path__. 
> **_NOTE:_** The path address is automatically stripped of unnecessary characters such as quotations marks or spaces. You do not have to format your file path after pasting it.

3. After choosing to use either the default or custom _.csv_ file, you will be prompted with the following:  
`Enter path of HTML file: `

4. Docscanner will return whatever words/phrases it found in your _.html_ file along with the line numbers on which it was found. 

### Data Formatting
Ensure that your _.csv_ file has no header columns, and that each individual word and phrase occupies a single row within the first column.

### Changing the Default File
_To change the default file:_
1. Locate the root directory storing docscanner.py. 
2. Open the _data_ folder. 
3. Delete or alter the existing _.csv_ file and save your changes. 
4. Open the _src_ folder.
5. Change the string for the variable __forbidden_phrases_path__ to match the name of your new default file in the _data_ folder. 
6. Save your changes. 
