# About Docscanner
Docscanner allows you to streamline your documentation workflow by detecting words or phrases listed in a _.csv_ file in an inputted _.html_ file. If any words/phrases are detected, Docscanner returns both the word/phrase as well as the line number that it is located on. This helps eliminate human error when applying style guide content standards in a documentation project. 

The script is case insensitive and is also capable of finding duplicate words/phrases on the same line in the _.html_ file. 

## Installing Docscanner
If you haven't already, download Python [here](https://www.python.org/downloads/).  
> **_NOTE:_** If installing Python for the first time, make sure you select the __Add Python 3.7 to PATH__ checkbox.  

Install Docscanner by running the following in your Command Prompt terminal:  
`pip install doc-scanner`

## Using Docscanner
1. Start Docscanner by running the following in your Command Prompt terminal:  
`docscanner`  
You will be prompted with the following:  
`Use default csv file of forbidden phrases? (respond Y or N): `  
2. Choose whether to use the default _.csv_ file or to add a custom path:
    - To use the default csv file, enter "Y". The script will jump to the next argument where you input the _.html_ file path.  
    - To use a custom csv file, enter "N". You will be prompted with the following:  
`Enter path of your custom csv file: `  
Copy the path from File Explorer by holding \<SHIFT\>, right-clicking your desired file, and selecting __Copy as path__.

    After choosing to use either the default or custom _.csv_ file, you will be prompted with the following:  
`Enter path of html file: `  

3. Copy the path from File Explorer by holding \<SHIFT\>, right-clicking your desired file, and selecting __Copy as path__. 

4. Enter your _.html_ file path into your terminal.  
 Docscanner will return whatever words/phrases it found in your _.html_ file along with the line numbers on which they were found. 
  > **_NOTE:_** The path addresses are automatically stripped of unnecessary characters such as quotations marks or spaces. You do not have to format your file paths after pasting them in your terminal.

### Formatting Data 
Ensure that your _.csv_ file has no header columns and that each individual word/phrase occupies a single row within the first column.
#### Example _.CSV_ file: 
`word_1`    
`phrase 1`    
`word_2  `

### Changing the Default File
1. Locate the directory storing docscanner.py.  
    > **_NOTE:_** You can quickly find the file path where docscanner is stored by running the following in your terminal:  
    `pip show doc-scanner`
2. Click _docscanner_ > _data_ to open the _data_ folder. 
3. Replace or alter the existing _.csv_ file in the _data_ folder and save your changes. 
> **_NOTE:_** Steps 4-6 are only necessary if the _.csv_ file name was changed. It is recommended you keep the same file name. 
4. (Optional) Locate and open the _docscanner_ folder. 
5. (Optional) Open _docscanner.py_ in an IDE.
6. (Optional) Change all of the file names in the `get_forbidden_phrases_path` function starting on line 35 to match the name of your new default _.csv_ file in the _data_ folder. 
7. Save your changes. 

### Troubleshooting
If Docscanner is not running properly:
- Ensure that all file paths are correct.  
- Verify you are using a Command Prompt or Bash terminal, not PowerShell.
- Check whether the `docscanner` directory structure on your workstation matches what is on GitHub. 

### Uninstalling
Uninstall Docscanner by running the following in your terminal:  
`pip uninstall -y doc-scanner`

>[!NOTE]
>test.
