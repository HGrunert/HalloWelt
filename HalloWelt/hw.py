import keyboard  # keyboard is not installed on b2
import time

def function1(X):
    print(X)

def f1(X):
    print(X)

def f2(X):
    print("Jo ", X, "!")
    print(X, " I'm talking to you!")
    f1("Goddammit!")

print("hello world")  # nice comment, did your mom buy it for you
a = keyboard.read_key()  # read a keypress, wait until you've read something
print(a)  # lolz it prints it for a millisecond
longstring ="Lets be absolutely clear.\nYou don't own me.\nI own me, not you.\nOhmygawd Imma die, Imma die.\rYou have no power over me. None."
print(longstring)
print(len(longstring)) #len gibt uns die länge. Ist auch eine Method. Methods werden mit Punkten angewended.
print(longstring.format()) #geht das auch
sonder = "Größ, klein, Fräß müss sein." #srings haben methods kann man mit dir(str) oder dir(varname anzeigen)
print(sonder.lower(),sonder.upper())#werden so aufgerufen. So wie z.B. packet.function_from_that_packet().
# Zeichenumbrüche, backslash,waiting ,return_carriage
print(r"c:\lolz is a path and \n is a newline and \r is carriage return to write over stuff.")
print("print this long secret message \r and erase it                  ")
print("Don't forget to escape \" \\ \"  \" \' \" and \" \" \"")
print('Although "you" can use "single quotes" if you "want" lots of "quoted stuff".')

kursname = "ccpython"  # Variable
Teilnehmer = ["elke", "Uwe", "Kay"]  # List
mnr = (433, 2543, 5672)  # Tuple

# f1("Hi!")
# f1("I'm trying function calls")
# f2("Ben")
