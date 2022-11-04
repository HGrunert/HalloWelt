import tkinter as tk
root = tk.Tk() #create window object
#Variable für die Eingabe erzeugen.
eingabefeld_wert =tk.StringVar()
eingabefeld_wert.set('')
passwdfeld_wert = tk.StringVar()

#textausgabe erzeugen #bereitstellen der Befehle

label1 = tk.Label(root,text='Hallo Welt')
bild1=tk.PhotoImage(file='biene.png')
labelb1 =tk.Label(root, image=bild1)
label2 = tk.Label(root,text='Das hier ist die Biene.'+ eingabefeld_wert.get(),\
                  fg='#00f0f0',\
                  bg='#f0f0f0',\
                  font=('sans',20,'italic'))
#Eingabefelder
eingabefeld= tk.Entry(root, textvariable= eingabefeld_wert)
passwdfeld = tk.Entry(root,textvariable=passwdfeld_wert,show='X')#wanna show how to do the * thingies
##checkboxes
'''
checkbox1 =tk.Checkbutton(root)
checkbox1['text'] = 'checkbox'
checkbox1.pack()
checkbox1var=tk.BooleanVar()
checkbox1['variable'] = checkbox1var
##listboxes
choicelist= ['choice1','choice2','etc']
lbox=tk.Listbox(root)
lbox.pack()
for item in choicelist:
    lbox.insert('end',item) #insert an index and the elements

#im output dann:
def lboxoutput(lbox):
    lbox_output=lbox.curselection()
    return lbox_output
'''
#buttons
def exitbiene():
    exit()
def refresh():
    label2 = tk.Label(root, text='Das hier ist die Biene ' + eingabefeld_wert.get() +'.', \
                      fg='#00f0f0', \
                      bg='#f0f0f0', \
                      font=('sans', 20, 'italic'))
    label2.grid(row=2,column=1)

button1 =tk.Button(root, text = 'Name it!',command=refresh)
button2 =tk.Button(root, text = 'Kill it!',command=exitbiene)

#in das Fenster einbetten #Ausführen dieses befehls
#label1.pack()
#labelb1.pack(side='right')
#label2.pack()
##alternative in einem grid anordnen.
# # #Grid und pack verträgt sich nicht.# # #
def bienenpasswort():
    root.option_clear()
    label1.grid(row=0,column=0)
    labelb1.grid(row=1,column=1)
    label2.grid(row=2,column=1)
    eingabefeld.grid(row=3,column=1)
    passwdfeld.grid(row=4, column=1)
    button1.grid(row=5,column=1)
    button2.grid(row=5,column=2)
#build

bienenpasswort()

#open the window
root.mainloop()