ausgabetext = "Der Preis für 2 Socken beträgt 5 DM und 5 Paar kosten 10 DM"
print(ausgabetext)
ausgabetext = ausgabetext.replace("DM", "Euro")#replace straightforward
print("Nach dem Austauschen über replace():")
print(ausgabetext)
#replace multiple things
ausgabetext = "1 1 2 2 3 3 4 4"
ausgabetext = ausgabetext.replace("1", "eins")
ausgabetext = ausgabetext.replace("2", "zwei")
ausgabetext = ausgabetext.replace("3", "drei")
print("Nach dem Austauschen über replace():")
print(ausgabetext)
#now the same thing cursed
ausgabetext = "1 1 2 2 3 3 4 4"
ausgabetext = \
ausgabetext.replace("1","eins").replace("2","zwei")\
.replace("3","drei")
print("Nach dem Austauschen über replace():")
print(ausgabetext)
inhalt = "Hier kommt ein String-Inhalt"
print ( inhalt.count("in") ) #how many times does "in" appear in inhalt
#you might need to count lower if you want both upper and lower
