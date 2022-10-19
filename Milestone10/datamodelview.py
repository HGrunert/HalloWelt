# data      - variable eingabedaten
# model     - rechenarten
# view      - anzeige
test = "hallo"
len(test)
par3 = 256
"""eingabe in Funktionen"""
def addition(par1=1,par2=10):
    global par3
    #par1=1
    #par2=11
    #data
    print(par3)
    print(par1)
    print(par2)
    #model
    ergebnis= int(par1) + int(par2)
    #print("Versuche max "+ str(versuche))
    #zufall=random.randint(par1,par2)
    #print("Zufall " + str(zufall))
    #print(ergebnis)
    return ergebnis
def mk_data(zahl1,zahl2):
    out = []
    out.append(zahl1)
    out.append(zahl2)
    return out
def mk_mult(data):
    out = 0
    out = data[0] * data[1]
    return out
def view_erg(ergebnis):
    print(str(ergebnis))
#zahlenraten(2)
#print(par1)
#erg = addition(1,5,7)
erg=mk_mult(mk_data(21,2))
#view
view_erg(erg)