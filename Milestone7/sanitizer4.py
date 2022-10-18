def ruler():
    print(9*"0"+10*"1"+10*"2"+10*"3"+10*"4"+10*"5"+"6")
    print(6*"1234567890")

def sanitize(toSan):
    signs = '<>(){}[];\\"\'-'
    toSan = toSan.strip()
    countoutp = []
    zaeler = []
    for chars in signs: #für alle teile von signs, do
        zaeler.append(toSan.count(chars))
        if(0!=toSan.count(chars)): #wenn die Zahl von chars in toSan nicht Null ist,
            countoutp.append("Achtung! Der String enthält Sonderzeichen \"" + chars + "\"  :"\
                         + str(toSan.count(chars)).zfill(2).rjust(5))
            #Hänge an countoutp : eine Einleitung mit dem Zeichen + die Zahl der zeichen in toSan
            # + zahl der Zeichen als str, zfilled zu 2 ziffern
            # und rechtsbündig mit 5 Zeichen nach dem ":".
    ######Ausgabe######
    ruler() #mach ein Lineal
    print("Der Eingangsstring lautete".ljust(49) + ':' + '\n' + toSan.ljust(60))
    # Sag mir den Eingangsstring
    toSan = toSan.replace('<html>','      ')#destroy the tags vernichte html tags.
    toSan = toSan.replace('</html>','       ')
    for chars in signs: #für alle teile von signs, tu
        toSan = toSan.replace(chars,' ') #ersetze die Zeichen mit einem leerzeichen
    toSan = toSan.lower() #speichern als kleinbuchstaben.
    print('Der Sanitized String ist'.ljust(49) + ':' + '\n' + toSan[0].upper() + toSan[1:len(toSan)].ljust(59)) #sag mir was übrig bleibt
    ruler()
    print('\n'.join(countoutp))
    return[toSan, countoutp , zaeler]

#The Strings to test
print(sum(sanitize(" - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' ")[2]))

for i in sanitize(' <html> ist eine tolle Sprache</html> ')[2]:
    print(i)

sanitize("Hacker schleusen auch gerne Code ein! test()")

sanitize(" ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!")

sanitize("Oder am Ende von Eingaben ")

sanitize('Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch)\n')

sanitize("<dieser String ist nun sanitized>")