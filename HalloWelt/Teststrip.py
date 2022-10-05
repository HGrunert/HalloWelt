kursName = '   Python lernen, große Klasse!    ' #einfache str Variable
print(kursName) #variable unverändert
print(kursName.lstrip()) #unnötige Zeichen von links entfernen
print(kursName.rstrip()) #unnötige Zeichen von rechts entfernen
print(kursName.lstrip() + "Heute noch Teilnehmen!") #aber rechts bleiben sie
wrongColon = "test:       Lern Python!"
print(wrongColon.lstrip(':set ')) #Wir können auch noch extrazeichen entfernen lassen.
print(kursName.strip()) #volles rohr
wrongNewline = '\nVergiss auch die extra Leerzeilen nicht!\n \n\n : \n \n :' #cursed
print(wrongNewline.strip(" \n\r:")) #decursed

