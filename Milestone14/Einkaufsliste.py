

import tkinter as tk

root =tk.Tk()
frame = tk.Frame(root)
frame.pack()

global zettel
zettel =[]
class EListe():
    def __init__(self):
        self.name_w =tk.StringVar()
        self.entryn =None
        self.zahl_w =tk.StringVar()
        self.entryz =None
        self.eliste =[]

    def speichern(self):
        global zettel
        zettel.append((self.name_w.get(),self.zahl_w.get()))


    def entryform(self, rootpane):
        lab1 = tk.Label(rootpane,text='Was willst du kaufen?')
        self.entryn = tk.Entry(rootpane, textvariable=self.name_w)
        lab2 = tk.Label(rootpane,text='Wie viel?')
        self.entryz = tk.Entry(rootpane, textvariable=self.zahl_w)
        button = tk.Button(rootpane,text='add',command=self.speichern)
        lab1.pack()
        self.entryn.pack()
        lab2.pack()
        self.entryz.pack()
        button.pack()
        return(self.eliste)

    def clentry(self):
        global zettel
        item=''
        while(item.lower()!='nichts'):
            item=input('Was willst du kaufen?')
            nr=input('Wie viel davon brauchst du?')
            zettel.append((item,nr))
            print('Hinzugefügt. Schreibe "nichts" zum beenden')

einkauf = EListe()
ezettel= einkauf.entryform(frame)
if(input('GUI? y/n').lower()=='y'):
    root.mainloop()
else:
    einkauf.clentry()
printz =[]
for i in zettel:
    printz.append(':'.join(i))
print('\n'.join(printz))