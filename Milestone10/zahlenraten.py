import random

def zahlenraten():
    a = random.randint(1, 10)
    c = -1
    n=-1
    while(a != c):   #check the answer
        n+=1
        c = int(input('Was ist die Zahl?'))  # ask for the product
    print('Richtig. Du brauchtest', n, 'Versuche.')
zahlenraten()