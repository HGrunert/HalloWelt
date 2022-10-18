import random
#adject = []
#substant =[]

#def nice():#set nice pairs
#    global adject
#    global substant #just set them right now, because we need one of them anyway
adject = ['riesigste', 'großartigste', 'gewaltigste', 'immenseste', 'beste', 'liebste', 'schönste', 'größte']
substant =['Rechenkünstler', 'ABC-Schütze', 'Lerner', 'Experte', 'Mensch', 'Freund', 'Kumpel', 'Programmierer', 'Teilnehmer']


def naughty():
    global adject
    global substant
    if(random.randint(0,1)): #choose one pair and make it naughty
        adject = ['schwächste', 'dümmste','kleingeistigste', 'lernresistenteste','pfostigste','schleimigste']
    else:
        substant =['Vollidiot', 'Pfosten','Idiot','Braunnaser','Toillettenschlürfer','Leimschnüffler','HONK','Sonderschüler','Hundekicker']

a = random.randint(1,10) #generate 2 numbers
b = random.randint(1,10)
c = int(input('Was ist '+a.__str__() +' mal '+ b.__str__() +'?')) #ask for the product
if(a*b == c):   #check the answer
    print('Richtig.')
    #nice()
else:
    print('Falsch.')
    naughty()
#Fire the compliment/insult
print('Du bist der ' + random.choice(adject) +' ' + random.choice(substant)+'.')