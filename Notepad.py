import tkinter
from tkinter import filedialog
from tkinter import messagebox
def New_File():
    global path
    if textarea.get("1.0", tkinter.END).strip():
       if messagebox.askyesno("Save:","Save:\nDo you want to save the file?"):
           Save()
    textarea.delete("1.0", tkinter.END)
    root.title("Untitled - Notepad")
def Open_File():
    global path
    path = filedialog.askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),("Text Document", "*.txt")])
    if path:
        root.title(f"{path} - Notepad")
        textarea.delete("1.0", tkinter.END)
        with open(f"{path}", "r")as file:
            textarea.insert(tkinter.END, file.read())
def Save():
    global path
    if path:
        with open(path, "w") as file:
            file.write(textarea.get("1.0", tkinter.END))
        root.title(f"{path} - Notepad")
    else:
        Save_as()
def Save_as():
    global path
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if path:
        with open(path, "w+") as file:
            file.write(textarea.get("1.0", tkinter.END))
        root.title(f"{path} -NotePad")
def undo():
    textarea.edit_undo()
def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")
def Help():
    messagebox.showinfo("Help", "Help:\nHarsh Vardhan will definitely help you out!")
def Exit():
    if textarea.get("1.0", tkinter.END).strip():
        if messagebox.askyesno("Save", "Do you want to save the file?"):
            Save()
    quit()
root = tkinter.Tk()
# basic
root.geometry("600x700")
root.title("Untitled - Notepad")
root.wm_iconbitmap("notepad.ico")
path = None
# menu
Main_menu = tkinter.Menu(root)
# file
file_menu = tkinter.Menu(Main_menu, tearoff=0)
file_menu.add_command(label="New File", command=New_File, font="arial 10")
file_menu.add_command(label="Open File", command=Open_File, font="arial 10")
file_menu.add_separator()
file_menu.add_command(label="Save", command=Save, font="arial 10")
file_menu.add_command(label="Save As", command=Save_as, font="arial 10")
Main_menu.add_cascade(menu=file_menu, label="File")
# edit
edit_menu = tkinter.Menu(Main_menu, tearoff=0)
edit_menu.add_command(label="Undo", command=undo, font="arial 10")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut, font="arial 10")
edit_menu.add_command(label="Copy", command=copy, font="arial 10")
edit_menu.add_command(label="Paste", command=paste, font="arial 10")
Main_menu.add_cascade(menu=edit_menu, label="Edit")
# help
help_menu = tkinter.Menu(Main_menu, tearoff=0)
help_menu.add_command(label="Help", command=Help, font="arial 10")
Main_menu.add_cascade(menu=help_menu, label="Help")
# exit
Main_menu.add_command(label="Exit", command=Exit)
root.config(menu=Main_menu)
# TextArea
textarea = tkinter.Text(root, font="arial 12")
textarea.pack(fill=tkinter.BOTH, expand=True)
scroll = tkinter.Scrollbar(textarea, orient=tkinter.VERTICAL)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)

root.mainloop()