

import tkinter as tk
root =tk.Tk()
frame = tk.Frame(root)
frame.pack()
global gaeste
gaeste =[]
class GUIGast():
    def __init__(self):
        self.vname_w =tk.StringVar()
        self.entryv =None
        self.nname_w =tk.StringVar()
        self.entryn =None
        self.gastitem ={'vname':'defaultv','nname':'defaultn'}

    def speichern(self):
        global gaeste
        self.gastitem['vname']=self.vname_w.get()
        self.gastitem['nname']=self.nname_w.get()
        print(gastitem)
        gaeste.append(self.gastitem)

        return self.gastitem

    def entryform(self, rootpane):
        self.entryv = tk.Entry(rootpane,textvariable=self.vname_w)
        self.entryn = tk.Entry(rootpane,textvariable=self.nname_w)
        button = tk.Button(rootpane,text='add',command=self.speichern)
        self.entryv.pack()
        self.entryn.pack()
        button.pack()
        return(self.gastitem)

gast = GUIGast()
gastitem= gast.entryform(frame)

root.mainloop()
print(gaeste)