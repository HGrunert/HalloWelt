


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
gasteintrag = {}
gasteintrag['vname'] = "Ben"
gasteintrag['nname'] = "Ertel"
gasteintrag['telnr'] = "+4900000000000"
gasteintrag['mail'] = "Ertel@ben.deutschland"
gasteintrag['allergie'] = "keine"
gasteintrag['gender'] = "backfisch"
gaestebuch.append(gasteintrag)
#nochwat
gasteintrag = {}
gasteintrag['vname'] = "Benny"
gasteintrag['nname'] = "Ertelly"
gasteintrag['telnr'] = "+4900000000001"
gasteintrag['mail'] = "Ertelly@ben.deutschland"
gasteintrag['allergie'] = "keine"
gasteintrag['gender'] = "backfische"
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
    ge['mail'] = 'lol' #set mail to something
    while((ge['mail'].count('@') * ge['mail'].count('.'))== 0): #solange entweder
        ge['mail'] = input("EMail:".rjust(20)) #0@s oder 0 punkte drin sind
        if((ge['mail'].count('@') * ge['mail'].count('.'))== 0):
            print('ERROR:Not an email.') #und gib ne errormeldung an
    ge['allergie'] = input("Allergene:".rjust(20))
    ge['gender'] = input("Gender:".rjust(20))
    return(ge) #return the guest to append it outside

def findguest(): #finde einen Gast nach seinem Namen und returne ihn.
    aName = input('Name des Gastes:')
    n=0 #setz die outnummer auf 0
    for guest in gaestebuch:
        if(guest['vname'] == aName):#check firstname
            return([guest,n])
        if(guest['nname'] == aName):#lastname
            return([guest,n])
        if(guest['vname']+' '+guest['nname'] == aName): #bothnames
            return([guest,n])
        n+=1 #make the number larger before loading the next guest
    guest['allergie'] = 'error' #if there is no guest make one and give it the allergie error
    return([guest,-100000000000]) #return the guest and it's number. Negative 10billions is an error code.

def listall():
    n=0 #to print guest numbers
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
        hmeingabe = hmeingabe.lower()
        #bedingung prüfen inclusive bedingung "schleifenabbruch"
        if(hmeingabe=='quit'): #kill the programm
            break
        elif(hmeingabe=='addguest'): #add a guest
            gaestebuch.append(eingabe())
        elif(hmeingabe=='delguest'): #delete a guest
            gone = findguest()[1] #get nr from name
            if(gone == -100000000000): #error code
                print("Ich konnte diesen Gast nicht finden.")
            else:
                del(gaestebuch[gone])
                print('Gast', gone ,'entfernt.')
        elif:(hmeingabe=='checkguest'): #check a guests Allergies
            tmpguest = findguest()#call the findguest
            curguest = tmpguest[0] #put the found guest into curguest
            if(tmpguest[1] == -100000000000):#check for the error code
                print("Ich konnte diesen Gast nicht finden.")
            else:
                print('Gast' +str(tmpguest[1]) + ':' + curguest['vname'] + ' ' + curguest['nname'] + ' ist auf der Gästeliste.')
                if(curguest['allergie']=='keine' or curguest['allergie']== 'none'):
                    #check if there are allergies
                    print('Der Gast hat keine Allergien.')
                else: #if the field isn't filled with none, gimme the field
                    print(curguest['vname'] + ' ist gegen ' + curguest['allergie'] + ' allergisch.')
        elif(hmeingabe=='printall'): #dump the guestbook
            print(gaestebuch)
        elif(hmeingabe=='guests'): #list the guests with their number
            listall()
        elif(hmeingabe=='load'): #dummy
            if('Ja'==input('Altes Gaestebuch überschreiben? Ja/Nein?')):
                print('loaded')
                #pickle.load(gaesteliste,'GL.dat')
        elif(hmeingabe=='save'): #dummy
                if('Ja'==input('Altes Gaestebuch file überschreiben? Ja/Nein?')):
                    print('saved')
                    #pickle.dump(gaesteliste,'GL.dat')
        elif(hmeingabe=='guestnumber'): #dump a guest from it's number
            n= int(input('Nummer? '))
            if(n<len(gaestebuch)):
                print(gaestebuch[n])
            else: print('No Entry.')
        elif(hmeingabe=='clearall'): #delete everything.
            if('Ja'==input('Wirklich alles löschen? Ja/Nein?')):
                gaestebuch = []
                print('Your Funeral.')
                gaestebuch.append(gastn) #put an empty entry in, so stuff doesn't break


###################
hauptmenue()

