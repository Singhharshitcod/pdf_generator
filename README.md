Script Description: Multi-File PDF Story Generator
This Python script allows users to create multiple PDF files, each containing user-entered story content, and automatically saves them in a specified folder. It uses the reportlab library for PDF generation and textwrap for word wrapping.
⚙️ How It Works
1)Folder Creation
The user is prompted to enter the name of a folder where the generated PDF files will be stored.
If the folder does not exist, it is automatically created using os.makedirs().
2)Number of Files
The user specifies how many PDF files (STORY 1.pdf, STORY 2.pdf, …) should be created inside the chosen folder.
3)Content Input
For each file, the user types the story content (multi-line input).
Input ends when the user presses Enter on a blank line.
4)Text Formatting
The script starts drawing text from coordinates (50, 800) in the PDF.
Each paragraph is word-wrapped to a maximum width of 90 characters using textwrap.wrap().
A blank line is inserted between paragraphs for readability.
5)PDF Generation
A reportlab.canvas object is created for each story.
The wrapped content is written into the PDF.
The file is saved with the name STORY <i>.pdf inside the specified folder.
6)Verification Message
After each file is created, a confirmation message is printed to the terminal.
