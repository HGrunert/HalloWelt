#The Strings to test
toSan = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "

#toSan = ' <html> ist eine tolle Sprache</html> '

#toSan = "Hacker schleusen auch gerne Code ein! test()"

#toSan = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"

#toSan = "Oder am Ende von Eingaben "

#toSan = 'Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch)\n'

#toSan = "<dieser String ist nun sanitized>"

toCount = toSan
if(0!=toCount.count('<')): #if toCount Enthält das Zeichen 
        print("Enthält \"<\" :", toCount.count('<')) #Zähl es und gib die Zahl aus
if(0!=toCount.count('>')):
        print("Enthält \">\" :", toCount.count('>'))
if(0!=toCount.count('(')):
        print("Enthält \"(\" :", toCount.count('('))
if(0!=toCount.count(')')):
        print("Enthält \")\" :", toCount.count(')'))
if(0!=toCount.count(';')):
        print("Enthält \";\" :", toCount.count(';'))
if(0!=toCount.count('"')):
        print("Enthält \"\"\" :", toCount.count('"'))
if(0!=toCount.count("'")):
        print("Enthält \"'\" :", toCount.count("'")) #switch quote
if(0!=toCount.count('-')):
        print("Enthält \"-\" :", toCount.count('-'))
if(0!=toCount.count('{')):
        print("Enthält \"{\" :", toCount.count('{'))
if(0!=toCount.count('}')):
        print("Enthält \"}\" :", toCount.count('}'))
if(0!=toCount.count('[')):
        print("Enthält \"[\" :", toCount.count('['))
if(0!=toCount.count(']')):
        print("Enthält \"]\" :", toCount.count(']'))
print("Der Eingangsstring lautete: ", toSan)
toSan = toSan.replace('<html>','')#destroy the tags
toSan = toSan.replace('</html>','')
toSan = toSan.replace('<','')#destroy the signs
toSan = toSan.replace('>','')
toSan = toSan.replace('(','')
toSan = toSan.replace(')','')
toSan = toSan.replace(';','')
toSan = toSan.replace('"','')
toSan = toSan.replace('\'','')
toSan = toSan.replace('-','')
toSan = toSan.replace('{','')
toSan = toSan.replace('}','')
toSan = toSan.replace('[','')
toSan = toSan.replace(']','')
print('Der Sanitized String ist  : ', toSan)
