kursName = '   Python lernen, große Klasse!    ' #einfache str Variable
print(len(kursName)) #zeig mir die Länge an
print(kursName.__len__())
#Für Object oriented Programming Methods kann man das Objekt nehmen und
#die Methode mit einem Punkt dahinter schreiben
#objektname.aktion Diese kann man sich mit dir(objektname) oder dir(Klassenname) anzeigen lassen
#dir(str)
#dir(kursName)
#help(str) #geht auch
print(kursName.lower())
print(kursName.upper())
#help(str.lower)
print(kursName) #variable unverändert
print(kursName.lstrip()) #unnötige Zeichen von links entfernen
print(kursName.lstrip() + "Heute noch Teilnehmen!") #aber rechts bleiben sie
wrongColon = "test:       Lern Python!"
print(wrongColon.lstrip(':set ')) #Wir können auch noch extrazeichen entfernen lassen.
print(kursName.strip()) #volles rohr
wrongNewline = '\nVergiss auch die extra Leerzeilen nicht!\n \n\n : \n \n :' #cursed
print(wrongNewline.strip(" \n\r:")) #decursed

