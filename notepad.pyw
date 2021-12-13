from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os
root=Tk()
root.title("Text Editor")
root.geometry("900x900")
def pankaj():
    root.destroy()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))

def new ():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)

    
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
             
            f = open(file,"w")
            f.write(text.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file,"w")
        f.write(text.get(1.0, END))
        f.close()


 

#filemenu
filemenu =Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="New File" , command=new)
m1.add_command(label=" Open", command=openfile)
m1.add_command(label = "Save", command=saveFile)
root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu = m1)



m3=Menu(filemenu,tearoff=0)
m3.add_command(label="Cut   ",command=cut)
m3.add_command(label="Copy",command=copy)
m3.add_command(label="Paste   ",command=paste)
root.config(menu=filemenu)
filemenu.add_cascade(label="Edit",menu=m3)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT , fill=Y)
text=Text(root,height="900",yscrollcommand=scrollbar.set)

text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

m2=Menu(filemenu,tearoff=0)
m2.add_command(label="Exit", command=pankaj)
root.config(menu=filemenu)
filemenu.add_cascade(label="Exit",menu=m2)

 





















































root.mainloop()
