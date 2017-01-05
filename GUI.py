from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox

def buttonpress():
    entrytext = entry1.get()
    print entrytext
    tkMessageBox.showinfo("Alert", entrytext)


def addtolist():
    entrytext = entry1.get()
    listbox1.insert(END, entrytext)
    
def addtolist2(event):
    entrytext = entry1.get()
    listbox1.insert(END, entrytext)




root = Tk() #gives us a blank canvas object to work with
root.title("My first GUI program with Tkinter")

button1 = Button(root, text="Button 1", bg="red", command=addtolist)
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", addtolist2)

label1 = Label(root, text="Dont Push the red Button", bg="blue", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

listbox1 = Listbox(root)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW)


listbox1.insert(END, "Bob")
listbox1.insert(END, "John")
listbox1.insert(END, "Erick")


mainloop() #causes the windows to display on the screen until program closes