import os
from reportlab.pdfgen import canvas
import textwrap
name=input("ENTER THE NAME OF FOLDER IN WHICH PDF FILES WILL BE CREATED: ") #name of folder
os.makedirs(name,exist_ok=True)# create folder in default directory

no_of_files=int(input("THE NUMBER OF PDF FILES REQUIRED: "))
for i in range(1,no_of_files+1):
    filename=os.path.join(name,f"STORY {i}.pdf")#cretae file in folder with its name and format
    c=canvas.Canvas(filename) #To detremine the template
    # Multiline input
    print(f"ENTER THE CONTENT OF STORY {i}: ")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    content = "\n".join(lines)
    # Set up text object for multi-line drawing
    text_obj = c.beginText(50, 800)  # Start position (x=50, y=800)

    # Wrap and write each paragraph
    for paragraph in content.split('\n'):
        wrapped = textwrap.wrap(paragraph, width=90)  # Word-wrap
        for line in wrapped:
            text_obj.textLine(line)
        text_obj.textLine("")  # Add blank line between paragraphs

    
    c.drawText(text_obj)#object call
    c.save()  #save all files 
    print(f"{i} File Created in folder {name}") # verification
    print('\n')