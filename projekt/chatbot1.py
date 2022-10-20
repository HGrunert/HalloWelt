import random
import Milestone10.lottoziehung #hol aus Milestone10 das lottospiel
# -*- coding: utf-8 -*-


#'modelle'/Daten
##passende Antworten[]
def initialize(): #Erstelle die globalen Variablen und Daten.
    global passend #Für direkte genau richtige eingaben.
    passend ={}
    passend['Wie verbinde ich mich mit dem B2?'] = '''Führe den ssh Befehl mit dem -i Parameter aus.
    Dieser brauch den Pfad zur passenden Schlüsseldatei, die ihr selbst generiert habt und
    das Schloss dafür auf den B2 hochgeladen habt.
    Dann müsst ihr als Argument Benutzername@hostname angeben. Der Benutzername ist user und eine zahl,
    der hostname ist eine IP oder ein fqdn. Für den B2 ist das cctrainer.ddnss.de'''
    global bekannte_eingaben #erstelle 2 Listen, die direkt zueinander gehören.
    bekannte_eingaben=[] #mögliche schlüsselwörter
    global passendn #passend numbered
    passendn=[] #dazugehörige ausgaben
    bekannte_eingaben.append('help')
    passendn.append('Frage mich einfach nach möglichen Hilfethemen.')
    bekannte_eingaben.append('ssh')
    passendn.append('''Führe den ssh Befehl mit dem -i Parameter aus.
    Dieser brauch den Pfad zur passenden Schlüsseldatei, die ihr selbst generiert habt und
    das Schloss dafür auf den B2 hochgeladen habt.
    Dann müsst ihr als Argument Benutzername@hostname angeben. Der Benutzername ist user und eine zahl,
    der hostname ist eine IP oder ein fqdn. Für den B2 ist das cctrainer.ddnss.de''')
    bekannte_eingaben.append('scp')
    passendn.append('''Führe den scp Befehl mit dem -i Parameter aus.
    Dieser brauch den Pfad zur passenden Schlüsseldatei, die ihr selbst generiert habt und
    das Schloss dafür auf den B2 hochgeladen habt.
    Dann müsst ihr als Argumente zuerst die zu kopierende Datei, dann das Ziel angeben.
    Pfade auf remote Maschienen werden als Benutzername@hostname:pfad angeben. Der Benutzername
    ist z.B beim B2 user und eine zahl, der hostname ist eine IP oder ein fqdn.
    Für den B2 ist das cctrainer.ddnss.de''')
    bekannte_eingaben.append('b2')
    passendn.append('Willst du über ssh oder scp erfahren?')
    bekannte_eingaben.append('lol')
    passendn.append('Du bist nicht lustig.')
    bekannte_eingaben.append('lotto')
    passendn.append(Milestone10.lottoziehung.lottoziehung()) #Zahlen sind für jede ausführung jeweils stabil.
    ##Zufällige Antworten[]
    global zufaellig
    zufaellig =['Bitte deutlich schreiben.','Wenn du meinst...', 'Bist du da sicher?']

#views
##Anzeigen/Ausgaben
###greeting()
def greeting():
    print(15*"_/\\_")
    print('|' + 'Wilkommen! Ich bin ein scp und ssh Erklärer!'.center(58) + '|')
    print(15*"\\__/")
    print('Bot: Wie kann ich dir helfen?')
###show_answer()
def show_answer(answer,name='Bot'):
    print(name + ':', answer)
###Verabschieden()
def verabschieden():
    print(random.choice(['Dann geh doch zu Netto!','Du mich auch!','Tschüß',\
                         'Goodbye!', 'Farvel!']))


##Eingaben
###usereingaben()
def usereingaben(name='Ich'):
    global bekannte_eingaben
    inp=input(name + ': ')
#    bekannte_eingaben.append('Selber' + inp)
    return(inp)


#control
##Tools/Verarbeitung
###worte[] = zerlege eingabe(string)
def zerlege_eingabe(estring):
    worte = estring.split(' ')
    return worte
### int_index= check frage(string, bekannte eingabe)
def check_frage(eing,xlist):
    out=-1
    einzelworte = zerlege_eingabe(eing.lower())
    for wort in einzelworte:
        n=0
        for keyword in xlist:
            if(wort.strip('.!?')==keyword):out = n
            n+=1
    return out
### strings = get_antwort(int_index,passende_antworten[])
### string = get_random_answer()
# # Tools/Verarbeitung
# # # int_index = genrandom_answer(random_antworten)
# # # string = check_passende_antwort(bool)             # prüft den Index von check_eingaben und verzweigt ggf auf get_random_answer unter zuhilfenahme vom int_index aus genrandom_answer
# # # string = get_random_answer(int_index)

# # # bool=check_if_end(string)
def check_if_end(ins): #check for exit strings They need to be exact
    if {'quit','bye','exit','fuck you'}.__contains__(ins.lower()):return(True)
    if ins.lower().count(' bye '): return(True) #or there is a standalone bye in it
    return(False)
# string = chat_ai() #dies Verarbeitet unsere Tools und Daten
def chat_ai(eing):
    if eing=='': #Empty is just Wie Bitte?
        return('Wie bitte?')
#    if(type(passend[eing])=='string'):return(passend[eing])
    for check in passend.items(): #check the exact answers items gets us a list of tuples of
        if check[0]==eing: return(check[1]) # keys and values
    if(check_frage(eing,bekannte_eingaben)==-1): return(random.choice(zufaellig)) #if the final check fails
    #give us a random answer, but if it works
    else: return (passendn[check_frage(eing,bekannte_eingaben)]) #give the numbered passend

def mainprogram():
    while True: #start the loop
        in_string = usereingaben() #make a variable form a eingabe
        if check_if_end(in_string): #check for endcriterion
            break #and kill the loop
        show_answer(chat_ai(in_string))
#Programm:
def chatbot():
    initialize() #set global variables
    greeting() #greet the user
    mainprogram() #Run the bot
    verabschieden() #say goodbye
#tryout
chatbot()