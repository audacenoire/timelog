#by Audie Lenoir
# https://github.com/audacenoire

"""Imports: 
	datetime: For managing the timestamp
	pathlib: For managing paths
	keyboard: for monitoring keypresses
	threading: for multithreading commands
	tkinter, ttk: For GUI
"""

import keyboard, os, threading
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk

#Create the initial .csv file in the current working directory and assign it to the logFile variable
logFile = (Path.cwd() / "bio.csv")

#Convert current time to a string and store it in the currentTime variable in the format: Day, YYYY-MM-DD, hh:mm:ss. 12-hour time format. 
currentTime = datetime.now().strftime("%a,%Y-%m-%d,%I:%M %p")

#If the log file exists in the current directory, open the log file. Otherwise, create a new file. 
if logFile.exists():
    logWrite = open(logFile, "a") 
    print("Log file exists. Proceeding.")
else: 
    logWrite = open(logFile, "w")
    print("Creating new log file.") 
	
#Write the current time to the log file with a newline, and print the line to the console for debugging purposes. 
def logWriteFile(): 
    logWrite.write(currentTime + "\n")
    print(currentTime + "\n")
    
#Print the current log file to the console. 
def logReadFile(event):
    logRead = open(Path.cwd() / "bio.csv")
    for i in logRead.readlines(): 
        print(i)   
    
#Close the log. 
def logClose():
    logWrite.close()
    print("Log closed")

#If the log file exists, delete it.
def logDelete():
    if logFile.exists():
        os.remove(logFile)
    else:
        print("Log file does not exist.")

#TODO: Error checking: File must be closed before it can be deleted. 


root = tk.Tk()

#TK Button interface

#Create the Write button. 
writeButton = ttk.Button(root, text = "Write", command = logWriteFile)
writeButton.pack()

#Create the Close button. 
closeButton = ttk.Button(root, text = "Close", command = logClose)
closeButton.pack()

#Create the Delete Log button. 
deleteButton = ttk.Button(root, text = "Delete Log", command = logDelete)
deleteButton.pack()

#Necessary for TKinter windows. 
root.mainloop()
    
#Set the W key to write to the file. 
#def write_button():
#    keyboard.on_press_key("w", logWriteFile)
    
#Set the R key to read the file. 
#def read_button():
#    keyboard.on_press_key("r", logReadFile)

#Set the C key to close the file. 
#def close_button():
#    keyboard.on_press_key("c", logClose)

#Invoke the keyboard functions. 
#write_button()
#close_button()
#read_button()

#Keeps the program open until manually closed by user. 
while True:
    pass
 
 









#Read/write file process
#
# from pathlib import Path
# 
# path = Path("your/path/here/file.txt")
#
# To write text: 
# path.write_text("your text here")
# 
# To read text:
# path.read_text()
#
#
# Opening files
#
# To open in read mode: 
# file = open("myfile.txt")  # A Path("path/to/file.ext") can be put here. Remember to import Path from pathlib! 
#
# To read file and output in console: 
# fileRead = file.read()
#
#To open a new file to write: 
# fileWrite = open("myfile.txt", "w")
#
#To open an existing file to append: 
# fileAppend = open("myfile.txt", "a")
#
#To write to an opened writable file: 
# fileWrite.write("text to write here")
#
# or
#
# fileAppend.write("text to write here")
#
# To close an opened file: 
#
# file.close() 





#record = []
#def do_stuff(event):
#    global record
#    time = datetime.now()
#    print(time)
#    record.append(time)

# keyboard.on_press_key("p", do_stuff)


 
#def timestamp_list():
#    timelist = []


#TODO: Add values for timestamp to timelist with append method

