#The Strings to test
toSan = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "

#toSan = ' <html> ist eine tolle Sprache</html> '

#toSan = "Hacker schleusen auch gerne Code ein! test()"

#toSan = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"

#toSan = "Oder am Ende von Eingaben "

#toSan = 'Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch)\n'

#toSan = "<dieser String ist nun sanitized>"
signs = '<>();\\"\'-{}[]'
for chars in signs: #für alle teile von signs, tu
    if(0!=toSan.count(chars)): #wenn die Zahl von chars in toSan nicht Null ist,
        print("Enthält \"", chars, "\" :", toSan.count(chars)) #Sag mir die Zahl
toSan = toSan.replace('<html>','')#destroy the tags vernichte html tags.
toSan = toSan.replace('</html>','')
print("Der Eingangsstring lautete: ", toSan) #Sag mir den Eingangsstring
for chars in signs: #für alle teile von signs, tu
    toSan = toSan.replace(chars,'') #ersetze die Zeichen mit dem leeren String
print('Der Sanitized String ist  : ', toSan) #sag mir was übrig bleibt
