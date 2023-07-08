
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

logFile = (Path.cwd() / "bio.csv")

currentTime = datetime.now().strftime("%a,%Y-%m-%d,%I:%M %p")

if logFile.exists():
    logWrite = open(logFile, "a") 
    print("Log file exists. Proceeding.")
else: 
    logWrite = open(logFile, "w")
    print("Creating new log file.") 
    
def logWriteFile(): 
    logWrite.write(currentTime + "\n")
    print(currentTime + "\n")
    
def logReadFile(event):
    logRead = open(Path.cwd() / "bio.csv")
    for i in logRead.readlines(): 
        print(i)   
    
def logClose():
    logWrite.close()
    print("Log closed")

def logDelete():
    if logFile.exists():
        os.remove(logFile)
        print("Log file deleted.")
    else:
        print("Log file does not exist.")

#TODO: Error checking: File must be closed before it can be deleted. 


root = tk.Tk()

#TK Button interface

writeButton = ttk.Button(root, text = "Write", command = logWriteFile)
writeButton.pack()

closeButton = ttk.Button(root, text = "Close", command = logClose)
closeButton.pack()

deleteButton = ttk.Button(root, text = "Delete Log", command = logDelete)
deleteButton.pack()

root.mainloop()
    
#def write_button():
#    keyboard.on_press_key("p", logWriteFile)
    
#def read_button():
#    keyboard.on_press_key("r", logReadFile)

#def close_button():
#    keyboard.on_press_key("c", logClose)

#write_button()
#close_button()
#read_button()


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

