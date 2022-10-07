


#################################################################
# basisdefinitionen

# vornamen
# nachnamen
# telefonnummer
# email
# allergie
# gender

###############################################
#
gasteintrag = {}
gastn = {}
global gaestebuch
gaestebuch = []


#Gastgeber
gasteintrag['vname'] = "Ben"
gasteintrag['nname'] = "Ertel"
gasteintrag['telnr'] = "+4900000000000"
gasteintrag['mail'] = "Ertel@ben.deutschland"
gasteintrag['allergie'] = "keine"
gasteintrag['gender'] = "backfisch"
gaestebuch.append(gasteintrag)
#leereintrag
gastn['vname'] = "NA"
gastn['nname'] = "NA"
gastn['telnr'] = "0"
gastn['mail'] = "NA@NA.NA"
gastn['allergie'] = "NA"
gastn['gender'] = "NA"
#######################################################
# Beispiele
# gast in gaestebuch schreiben
#gaestebuch[0] = gasteintrag

# gasteintrag aus gaestebuch laden
#gasteintrag = gaestebuch[0]

##################################################################################
def eingabe():
    ge = {}
    ge['vname'] = input("Vorname:".rjust(20))
    ge['nname'] = input("Nachname:".rjust(20))
    ge['telnr'] = input("Tel.:".rjust(20))
    ge['mail'] = 'lol'
    while((ge['mail'].count('@') * ge['mail'].count('.'))== 0):
        ge['mail'] = input("EMail:".rjust(20))
        if((ge['mail'].count('@') * ge['mail'].count('.'))== 0):
            print('ERROR:Not an email.')
    ge['allergie'] = input("Allergene:".rjust(20))
    ge['gender'] = input("Gender:".rjust(20))
    return(ge) #return the guest to append it outside

def findguest(): #finde einen Gast nach seinem Namen und returne ihn.
    aName = input('Name des Gastes:')
    n=0
    for guest in gaestebuch:
        if(guest['vname'] == aName):
            return([guest,n])
        if(guest['nname'] == aName):
            return([guest,n])
        if(guest['vname']+' '+guest['nname'] == aName):
            return([guest,n])
        n+=1
    guest['allergie'] = 'error'
    return([guest,-100000000000]) #return the guest and it's number. Negative 10billions is an error code.

def listall():
    n=0
    print(40*'-')#Format
    print('Nr:'.ljust(5) + 'Name:'.ljust(20) + 'Gender:')#Tabellenkopf
    for guest in gaestebuch:
        namee = guest['vname'] + ' ' +guest['nname']#space for the name
        print( str(n).ljust(5) , namee.center(20) + ":" + guest['gender'].rjust(13))
        n+=1
    print(40*'-')
    

# hier kommt unser programm

def hauptmenue():
    global gaestebuch #übernehme das gästebuch

# basisschleife aufbauen
    while True:
        # Hauptmenue ausgeben
        print("""
        Hauptmenu:
        guests
        addguest
        delguest
        load
        save
        checkguest
        guestnumber
        printall
        clearall
        quit""")
        # benutzereingabe abfragen
        hmeingabe = input("Bitte wähle eine Option des Hauptmenüs:")
        #bedingung prüfen inclusive bedingung "schleifenabbruch"
        if(hmeingabe=='quit'): #kill the programm
            break
        if(hmeingabe=='addguest'): #add a guest
            gaestebuch.append(eingabe())
        if(hmeingabe=='delguest'): #delete a guest
            gone = findguest()[1] #get nr from name
            if(gone == -100000000000): #error code
                print("Ich konnte diesen Gast nicht finden.")
            else:
                del(gaestebuch[gone])
                print('Gast', gone ,'entfernt.')
        if(hmeingabe=='checkguest'): #check a guests Allergies
            tmpguest = findguest()
            curguest = tmpguest[0]
            if(tmpguest[1] == -100000000000):
                print("Ich konnte diesen Gast nicht finden.")
            else:
                print('Gast' +str(tmpguest[1]) + ':' + curguest['vname'] + ' ' + curguest['nname'] + ' ist auf der Gästeliste.')
                if(curguest['allergie']=='keine' or curguest['allergie']== 'none'):
                    print('Der Gast hat keine Allergien.')
                else:
                    print(curguest['vname'] + ' ist gegen ' + curguest['allergie'] + ' allergisch.')
        if(hmeingabe=='printall'): #dump the guestbook
            print(gaestebuch)
        if(hmeingabe=='guests'): #list the guests with their number
            listall()
        if(hmeingabe=='load'): #dummy
            if('Ja'==input('Altes Gaestebuch überschreiben? Ja/Nein?')):
                print('loaded')
                #pickle.load(gaesteliste,'GL.dat')
        if(hmeingabe=='save'): #dummy
                if('Ja'==input('Altes Gaestebuch file überschreiben? Ja/Nein?')):
                    print('saved')
                    #pickle.dump(gaesteliste,'GL.dat')
        if(hmeingabe=='guestnumber'): #dump a guest from it's number
            n= int(input('Nummer? '))
            if(n<len(gaestebuch)):
                print(gaestebuch[n])
            else: print('No Entry.')
        if(hmeingabe=='clearall'): #delete everything.
            if('Ja'==input('Wirklich alles löschen? Ja/Nein?')):
                gaestebuch = []
                print('Your Funeral.')
                gaestebuch.append(gastn) #put an empty entry in, so stuff doesn't break


###################
hauptmenue()

