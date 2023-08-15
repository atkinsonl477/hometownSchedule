import tkinter as tk
from tkinter import filedialog
import PyPDF2 as reader


def takeFile():
    pdf = open(filedialog.askopenfilename(filetypes=[("pdf (*.pdf)", "*.pdf "), ("cumdog", "*.exe")]), 'rb')
    pdfreader = reader.PdfReader(pdf)
    sched = ''
    numOfPages = len(pdfreader.pages)
    for i in range(numOfPages):
        sched += pdfreader.pages[i].extract_text() + '\n'
    print(sched)

window = tk.Tk()
window.geometry("600x200")
greeting = tk.Label(
    text='Hello, Tkinter'
 
    
    
    )
interaction = tk.Button(window,
    text="hello I am a button",
    bg="yellow",
    fg="black",
    pady= '50',
    
    )

xbBrowse = tk.Button(
    window,
    text="Browse...",
    
    command=takeFile

    )


xbBrowse.pack()
window.mainloop()


