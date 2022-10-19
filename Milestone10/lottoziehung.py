import random #random
winning =set() #winning
winlist = [] #liste in die wir das set packen können
while(len(winning)<6): #solange in winning weniger als 6 zahlen sind
    winning.add(random.randint(1,49).__str__().zfill(2)) #füge zahl hinzu und mach sie zum str für die Ausgabe
winlist.extend(winning) #extend um das set elementweise anzufügen
winlist = sorted(winlist) #sortieren zfill für 49 < 5
#winlist.sort() #sorted
print('Die Gewinnzahlen sind ' + ' '.join(winlist) + '.') #Ausgabe zahlen müssen str sein