#Import argv from sys module
from sys import argv

#set script and filename from argv
script, filename = argv

#Open file and define as txt variable
txt = open(filename)

#Print out filename and contents of file
print(f"Here's your file {filename}: ")
print(txt.read())
#Ask for the file again
print("Type the file name again:")
file_again = input("> ")
#Open file and define as txt_again
txt_again = open(file_again)

#Print out contents of file.
print(txt_again.read())