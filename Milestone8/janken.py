#Schere Stein Papier spiel
import random
moves = ['Schere','Stein','Papier']
loss = 1
mine = input('Schere, Stein oder Papier?')
his = random.choice(moves)
print('Enemy: ' + his)
if(his == mine):
    print('Draw.')
elif(his=='Schere'):
    if(mine=='Stein'):
        print('WINNER!')
        loss=0
    else:
        print('LOOSER!')
elif(his=='Stein'):
    if(mine=='Papier'):
        print('WINNER!')
        loss=0
    else:
        print('LOOSER!')
elif(his=='Papier'):
    if(mine=='Schere'):
        print('WINNER!')
        loss=0
    else:
        print('LOOSER!')
adject = ['riesigste', 'großartigste', 'gewaltigste', 'immenseste', 'beste', 'liebste', 'schönste', 'größte']
substant =['Rechenkünstler', 'ABC-Schütze', 'Lerner', 'Experte', 'Mensch', 'Freund', 'Kumpel', 'Programmierer', 'Teilnehmer']
if(loss):
    if (random.randint(0, 1)):  # choose one pair and make it naughty
        adject = ['schwächste', 'dümmste', 'kleingeistigste', 'lernresistenteste', 'pfostigste', 'schleimigste']
    else:
        substant = ['Vollidiot', 'Pfosten', 'Idiot', 'Braunnaser', 'Toillettenschlürfer', 'Leimschnüffler', 'HONK',
                    'Sonderschüler', 'Hundekicker']
#Fire the compliment/insult
print('Du bist der ' + random.choice(adject) +' ' + random.choice(substant)+'.')