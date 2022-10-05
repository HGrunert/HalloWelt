kursName = '   Python lernen, große Klasse!    ' #einfache str Variable
#help(str.lower)
print(kursName) #variable unverändert
print(kursName.lstrip()) #unnötige Zeichen von links entfernen
print(kursName.lstrip() + "Heute noch Teilnehmen!") #aber rechts bleiben sie
wrongColon = "test:       Lern Python!"
print(wrongColon.lstrip(':set ')) #Wir können auch noch extrazeichen entfernen lassen.
wrongNewline = '\n:\n:Vergiss auch die extra Leerzeilen nicht!\n \n\n : \n \n :' #cursed
print(wrongNewline.lstrip(" \n\r:")) #decursed

