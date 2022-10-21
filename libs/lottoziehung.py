import random #random
class lottoziehung():
    def __init__(self):
        self.winlist=[]
        self.winlist=self.ziehung()
        self.ausgabe=self.ausgabe()
    def ziehung(self):
        winning =set() #winning
        winli = [] #liste in die wir das set packen können
        while(len(winning)<6): #solange in winning weniger als 6 zahlen sind
            winning.add(random.randint(1,49).__str__().zfill(2)) #füge zahl hinzu und mach sie zum str für die Ausgabe
        winli.extend(winning) #extend um das set elementweise anzufügen
        return(sorted(winli)) #sortieren zfill für 49 < 5
        #winlist.sort() #sorted
    def ausgabe(self):
        return('Die Gewinnzahlen sind ' + ' '.join(self.winlist) + '.') #Ausgabe zahlen müssen str sein
    def printnumb(self):
        print(self.ausgabe())
#print(lottoziehung().ausgabe())