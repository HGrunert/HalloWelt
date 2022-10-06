teststring="abcdefghijklmnopqrstuvwxyz"
durchlauf=1
abbruch = len(teststring)
liste = []
toSan = "&fsadqwertzuio%sda$§sd\"fd§fdjkjkllhf§$oipmvs%dfbcxyxccxm<>><§$f\"ds§d$gf%f§"
while(durchlauf <= abbruch) :
    cnr = durchlauf-1
    chars = teststring[cnr]
    print("hallo " + durchlauf.__str__().zfill(2) + " " + chars)
    liste.append("Achtung! Der String enthält Normalzeichen \"" + chars + "\"  : " + \
          str(toSan.count(chars)).zfill(2))  # mach dat ding in die liste
    toSan = toSan.replace(chars, ' ')  # ersetze die Zeichen mit einem  String
    durchlauf += 1
print(toSan)
for i in range(len(liste)):
    print(liste[i])
print("or just use the nifty trick:")
print('\n'.join(liste))