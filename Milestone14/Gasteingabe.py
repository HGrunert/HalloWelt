

import tkinter as tk

class Gast:
    def __init__(self,vname='NA',nname=' ',email='not@given.nowhere',\
                 alter='-1', telephone_Nr='000000',\
                 passwordhash='pw',gender='unknown',passwordhash2='none'):
        self.vname= vname
        self.nname= nname
        self.email= email
        self.telephone_Nr= telephone_Nr
        self.alter = alter
        self.gender= gender
        self.passwordhash = passwordhash
        self.passwordhash2 =passwordhash2
    #region #getset...
    def set_nname(self,name):
        self.nname =name

    def get_nname(self):
        return self.nname

    def set_vname(self,name):
        self.vname =name

    def get_vname(self):
        self.vname =name

    def set_email(self, inp):
        self.email = inp

    def get_email(self):
        return self.email

    def set_alter(self, inp):
        self.alter = inp

    def get_alter(self):
        return self.alter

    def set_telephone_Nr(self, inp):
        self.telephone_Nr = inp

    def get_telephone_Nr(self):
        return self.telephone_Nr

    def set_gender(self, inp):
        self.gender = inp

    def get_gender(self):
        return self.gender

    def set_passwordhash(self, inp):
        self.passwordhash = inp

    def get_passwordhash(self):
        return self.passwordhash
    #endregion
    ##functions
gaesteliste = []
root = tk.Tk() #create window object
frame =tk.Frame(root) #make a frame in the window
frame.pack() #put it into the window
global curgast #a global guest that can hold the variables for all the entry fields
curgast = Gast(tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar())
#textausgabe erzeugen #bereitstellen der Befehle
def listall():
    n = 0  # to print guest numbers
    print(40 * '-')  # Format
    print('Nr:'.ljust(5) + 'Name:'.ljust(20) + 'Gender:')  # Tabellenkopf
    for guest in gaesteliste:
        namee = guest.vname + ' ' + guest.nname  # space for the name
        print(str(n).ljust(5), namee.center(20) + ":" + guest.gender.rjust(13))
        n += 1
    print(40 * '-')
#buttons
def exitreg():
    root.destroy()

def registersend():
    global curgast
    if(curgast.passwordhash.get()==curgast.passwordhash2.get()):
        choosegender()
    else:
        registeruser()

def addguest():
    global gaesteliste
    global curgast
    gaesteliste.append(Gast(curgast.vname.get(), curgast.nname.get(), curgast.email.get(), curgast.alter.get(), \
                            curgast.telephone.get(), curgast.passwordhash.get(),curgast.gender.get()))
    registeruser()




#build

def registeruser():
    global frame
    frame.destroy()
    frame = tk.Frame(root)  # make a frame in the window
    frame.pack()
    global curgast
    #make the entry fields
    offset= 25
    curgast.vname =tk.StringVar()
    einvname= tk.Entry(frame, textvariable= curgast.vname)
    labelnname =tk.Label(frame, text='Nachname:'.rjust(offset))
    curgast.nname =tk.StringVar()
    einnname= tk.Entry(frame, textvariable= curgast.nname)
    labelvname =tk.Label(frame, text='Vorname:'.rjust(offset))
    curgast.alter =tk.StringVar()
    einalter= tk.Entry(frame, textvariable= curgast.alter)
    labelalter =tk.Label(frame, text='Alter:'.rjust(offset))
    curgast.telephone =tk.StringVar()
    eintelnr= tk.Entry(frame, textvariable= curgast.telephone)
    labeltelnr =tk.Label(frame, text='Tel:'.rjust(offset))
    curgast.email =tk.StringVar()
    einemail= tk.Entry(frame, textvariable= curgast.email)
    labelemail =tk.Label(frame, text='Mail:'.rjust(offset))
    curgast.passworthash =tk.StringVar()
    einpw1= tk.Entry(frame, textvariable= curgast.passworthash, show='*')
    labelpw1 =tk.Label(frame, text='Passwort:'.rjust(offset))
    curgast.passworthash2 =tk.StringVar()
    einpw2= tk.Entry(frame, textvariable= curgast.passworthash2, show='*')
    labelpw2 =tk.Label(frame, text='Wiederholen:'.rjust(offset))
    #make the buttons
    registerbutton = tk.Button(frame, text='Register', command=registersend)
    button2 = tk.Button(frame, text='Kill it!', command=exitreg)
    #build the pw Window
    labelnname.grid(row=2 ,column=1)
    einnname.grid(row=2 ,column=3)

    labelvname.grid(row=3 ,column=1)
    einvname.grid(row=3 ,column=3)

    labelalter.grid(row=4 ,column=1)
    einalter.grid(row=4 ,column=3)

    labeltelnr.grid(row=5 ,column=1)
    eintelnr.grid(row=5 ,column=3)

    labelemail.grid(row=6 ,column=1)
    einemail.grid(row=6 ,column=3)

    labelpw1.grid(row=7 ,column=1)
    einpw1.grid(row=7 ,column=3)

    labelpw2.grid(row=8 ,column=1)
    einpw2.grid(row=8 ,column=3)
    registerbutton.grid(row=9,column=2)
    button2.grid(row =9, column=0)

global genderwahl
def choosegender():
    global frame
    global curgast
    frame.destroy()
    frame = tk.Frame(root)  # make a frame in the window root
    frame.pack()  # put it into the window
    #gender radiobuttons
    anrede = ['m','f', 'd']
    curgast.gender=tk.StringVar()
    curgast.gender.set('f')
    for wert in anrede:
        radiob =tk.Radiobutton(frame, text=wert, value=wert, variable=curgast.gender)
        radiob.pack()
    button3 = tk.Button(frame, text='Add the guest', command=addguest)
    button3.pack()
#program
registeruser()
#registeruser()
#open the window
root.mainloop()
listall()