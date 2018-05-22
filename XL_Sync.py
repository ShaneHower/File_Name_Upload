from openpyxl import Workbook
import os
from Tkinter import *

class XLSync:
    def __init__(self, path, name):
        print("Initializing object")
        self.path = path
        self.name = name

    def execute(self):
        wb = Workbook()
        print("Workbook created")
        ws = wb.active
        print("Workbook activated")
        count = 0
        dir_count = 0
        for dir, subdir, file in os.walk(self.path):
            index=0
            dir_count += 1
            while count< len(file):
                ws.cell(row=count+1, column = 1, value=file[index])
                count+=1
                index+=1
            print("directory {0} uploaded".format(dir_count))

        wb.save("{0}.xlsx".format(self.name))
        print("excel file saved")

#create window
window = Tk()
#First input
frame1=Frame()
frame1.pack(fill= X)

path_label= Label(frame1, text= "File Path", width=6)
path_label.pack(side = LEFT, padx = 5, pady= 5)

entry1 = Entry(frame1)
entry1.pack(fill=X, padx=5, expand=True)

#Second Entry
frame2 = Frame()
frame2.pack(fill=X)

name_file = Label(frame2, text= "File Name", width = 10)
name_file.pack(side=LEFT, padx= 5, pady=5)

entry2 = Entry(frame2)
entry2.pack(fill=X, padx=5, expand=True)

def print_text():
    path = entry1.get()
    name = entry2.get()
    return path, name

def close_window():
    window.destroy()

def combine_functions():
    path, name = print_text()
    print("Path received: {0}".format(path))
    print("File name received: {0}".format(name_file))
    XLSync(path, name).execute()
    close_window()

#enter button
enter_button = Button(window, text="Enter", command=combine_functions)
enter_button.pack(side=RIGHT)

window.mainloop()
