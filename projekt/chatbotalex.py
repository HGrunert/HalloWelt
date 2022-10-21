#-*- coding: utf-8 -*-
# erlaubte dinge im Programm.
#
# Listen
# Dictionary
# while-Schleifen
# for-Schleifen
# die Abfrage „in“
#
# als import ist "random" erlaubt
# views
# # Anzeigen/Ausgaben
# # # greeting(string="Hallo")
# # # show_answer(string)
# # # show_end(string="bye bye")
# # Eingaben
# # # string = usereingaben()
# control
# string = chat_ai(string_usereingabe)                 # dies verarbeitet unsere tools und daten - gibt die Daten /Antworten in den Chat aus
# # Tools/Verarbeitung
# # # bool=check_benutzereingabe(string)
# # # bool=check_if_end(string)
# # # worte[] = zerlege_eingabe(string)
# # # int_index = check_frage(string,bekannte_eingaben)
# # # int_index = genrandom_answer(random_antworten)
# # # string = check_passende_antwort(bool)             # prüft den Index von check_eingaben und verzweigt ggf auf get_random_answer unter zuhilfenahme vom int_index aus genrandom_answer
# # # string = get_answer(int_index,passende_antworten[])
# # # string = get_random_answer(int_index)
# modelle / Daten
# #  passende_antworten[]
# #  bekannte_eingaben[]
# #  random_antworten[]
import random
##################################################################################################
def greetings():
    greeting_list = ['Willkommen bei Stan&Olly!', 'Willkommen bei BotChy!']
    hinweis_list = ['Worüber möchtest du Heute sprechen?', 'Wie kann ich dir behilflich sein?', 'Wie kann ich dir den Tag versauen?:D']
    print(random.choice(greeting_list))
    print(random.choice(hinweis_list))
    print("zum beenden bitte 'bye' eintippen!")
def usereingaben():
    out= input("Besucher  >")
    return out
#Gibt False falls es vorkommt, gibt True falls es nicht vorkommt!
#Kann zum Abbruch der Hauptprogrammschleife genommen werden.
def check_if_end(inputstr):
    inp = inputstr.lower()
    if inp.count("bye", 0, 4) == 1:
        return False
    else:
        return True
def show_answer(answer):
    print("bot  >"+ answer)
def chat_ai(eingabe):
    global bekannte_eingaben
    global passende_antworten
    global random_antworten
    out = " "
    out = eingabe + " Antwort"
    #xindex = -1
    xindex = check_frage(eingabe,bekannte_eingaben)
    if xindex != -1:
        out = get_answer(xindex,passende_antworten)
        #print("Antwort"+ out)
    else:
        yindex = get_random_answer(random_antworten)
        yindex = 1
        out = get_random_answer(yindex,random_antworten)
        #print("Antwort" + out)
    return out
def genrandom_answer(random_antworten_lst):
    xindex = -1
    return xindex
def get_random_answer(xindex,random_antworten_lst):
    out = ""
    return out
def check_benutzereingabe(eingabe):
    if len(eingabe) <= 1:
        x = False
    else:
        x = True
    return x
def show_end(winke="bye bye"):
    print(winke)
def check_frage(eingabe,xlist):
    out = -1
    einzeltorte = eingabe.split(" ")
    xindex = 0
    for element in xlist:
        for wort in einzeltorte:
            if wort == element:
                out=xindex
        xindex += 1
        #inx = xlist.len(wort.strip(".!?"))  # gegebenenfalls noch überprüfen
        #if inx =<
    #print(inx," ",wort)
    return out
def get_answer(xindex,anworten_lst):
    out = " "
    out = anworten_lst[xindex]
    return out
################################################
# Hier haben wir bekannte Eingaben!!
bekannte_eingaben = []
passende_antworten = []
bekannte_eingaben.append("help")
passende_antworten.append("hilf dir selber!! oder gib vertrag/witz/astro-tv/lotto-zahlen ein")
bekannte_eingaben.append("vertrag")
passende_antworten.append("Wie viel Geld willst du ausgeben???")
bekannte_eingaben.append("witz")
passende_antworten.append("drücke ALT+F4!!!")
bekannte_eingaben.append("astro-tv")
passende_antworten.append("es gibt Heute nichts Gutes für dich im HoRRoRskop !!!")
bekannte_eingaben.append("lotto-zahlen")
passende_antworten.append("1+2+3+4+5+6 pluuus SuperZahlen 69")
####################################################
random_antworten = []
random_antworten.append("Für Hilfe drücke F1 !!!")
random_antworten.append("Brudi!! Gib help ein !!")
random_antworten.append("Wenn ich dir nicht helfen kann, ALT+F4 drücken")
random_antworten.append("Ich sehe Geld in deinen Leben $$$$")
random_antworten.append("Sorry, ich wurde dafür nicht gut genug programmiert :D !!")
#################################################
# Hauptprogramm
greetings()
running = True
while running:
    eingabe = usereingaben()
    #eingabe = "help"
    if check_benutzereingabe(eingabe):
        running = check_if_end(eingabe)
        if running:
            show_answer(chat_ai(eingabe))
    else:
        x = False
show_end("Bis nächstes mal!!")