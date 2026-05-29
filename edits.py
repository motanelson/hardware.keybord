import tkinter as tk
from tkinter import filedialog


class myapp:
    def __init__(self,root:tk.Tk,tilte:str,backgrounds:str,foregrounds:str):
        self.root=root
        self.root.title(tilte)
        self.root.configure(background=backgrounds)
        self.txt= tk.Text(background=backgrounds,foreground=foregrounds)
        self.txt.pack(padx=10,pady=10)
        self.bt=tk.Button(background=backgrounds,foreground=foregrounds,text="save",command=self.saves)
        self.bt.pack(padx=10,pady=10)
        self.btl=tk.Button(background=backgrounds,foreground=foregrounds,text="load",command=self.loads)
        self.btl.pack(padx=10,pady=10)
        self.btc=tk.Button(background=backgrounds,foreground=foregrounds,text="clear",command=self.clears)
        self.btc.pack(padx=10,pady=10)

    def saves(self):
        f1=filedialog.asksaveasfile(defaultextension="*.*",confirmoverwrite=True,mode="w")
        f1.write(self.txt.get("1.0","end-1c"))
        f1.close()

    def loads(self):
        f1=filedialog.askopenfile(mode="r", defaultextension="*.txt")
        a=f1.read()
        f1.close()
        self.txt.delete("1.0","end-1c")
        self.txt.selection_clear()

        self.txt.insert("1.0",a)
    def clears(self):
        self.txt.delete("1.0","end-1c")
        self.txt.selection_clear()


def starts(tilte:str="editor",backgrounds:str="black",foregrounds:str="white"):
    root=tk.Tk()
    apps=myapp(root,tilte,backgrounds,foregrounds)
    root.mainloop()


starts()