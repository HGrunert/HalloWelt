#sanitizes the beginning and end of strings contains htmlstripper and stepstripper

def htmlstrip(htmlteststring): #strip htmltags from a string
    #Strip html in two layers. lstrip('<html\\\'') then lstrip('<> ')
    tailstringwb = htmlteststring.lstrip('<html/ \\\'\"')
    tailstring = tailstringwb.lstrip('<> ')
    stringwb = tailstring.rstrip('html> / \\\'\"')
    finstring = stringwb.rstrip('<> ')#then rstrip('>html\\\'') then rstrip(<>)
    return(finstring)


def countshit(toCount):
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
    return(0)



#def onestrip(toreduce):#string deleter if there is one special character
#    begnr = min(toreduce.find("\\n"),toreduce.find(";"),toreduce.find("<"),\
#                toreduce.find(">"),toreduce.find("'"),toreduce.find('"'))
#    #always give out -1 unless ALL special characters are in there
#    endnr = min(ecuderot.find("\\n"),ecuderot.find(";"),ecuderot.find("<"),\
#                ecuderot.find(">"),ecuderot.find("'"),ecuderot('"'))
#    #same thing again
#    return(toreduce[(int(begnr) + 1):(len(toreduce) - (int(endnr) + 1))]) #give out gibberish

def sanitize(toSan):
    print('Der Sanitized String ist  : ', sanitize2(toSan))
    return('')

def sanitize1(toSan): #the actual sanitizer version one
    countshit(toSan)
    print("Der Eingangsstring lautete: ", toSan)
    toSan = toSan.strip('§- \'(){}[]\";\\') #first strip the usual criminals except anglebrackets
    #old try to find html tags #if(len(teststring.strip())==len(teststring.strip('<> '))):
    if(toSan.find('<html>') != -1): #if there's a htmltag in there,
        toSan = htmlstrip(toSan)# strip it
    toSan = toSan.strip('§- \'(){}[]<>\";\\') #now strip everything including anglebrackets
    return(toSan)

def sanitize2(toSan):
    countshit(toSan)
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
    return(toSan.strip())

#now put the things through
print(sanitize(" - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "))

print(sanitize(' <html> ist eine tolle Sprache</html> '))

print(sanitize("Hacker schleusen auch gerne Code ein! test()"))

print(sanitize(" ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"))

print(sanitize("Oder am Ende von Eingaben "))

print(sanitize('Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch)\n'))

print(sanitize("<dieser String ist nun sanitized>"))
