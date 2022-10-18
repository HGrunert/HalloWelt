#Schere Stein Papier spiel
import random
moves = ['Schere','Stein','Papier']

mine = input('Schere, Stein oder Papier?')
his = random.choice(moves)
print('Enemy: ' + his)
if(his == mine):
    print('Draw.')
elif(his=='Schere'):
    if(mine=='Stein'):
        print('WINNER!')
    else:
        print('LOOSER!')
elif(his=='Stein'):
    if(mine=='Papier'):
        print('WINNER!')
    else:
        print('LOOSER!')
elif(his=='Papier'):
    if(mine=='Schere'):
        print('WINNER!')
    else:
        print('LOOSER!')