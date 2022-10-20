
# -*- coding: utf-8 -*-

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



#################################################
# Hauptprogramm
greetings()
while True:
    usereingaben()
    check_if_end(string)
    show_answer(chat_ai(usereingabe()))



