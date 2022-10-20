telnet = 23
erg = int(telnet ** 4 + telnet ** 3) / 2
print(15*"_/\\_")
print('|' + str((23**4+23**3)/2).center(58) + '|')
print(15*"\\__/")

def ausgabe(*mehrereParameter):
    for wert in mehrereParameter:
        print(wert)

def uebergeben(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key,value))

ausgabe()
uebergeben(name='alter',alter='20')
