trenner = " Bottles of Beer on the wall! One is drunk and now we have "
botl = list(str(i) for i in range(100))
bot = botl[-1:0:-1]
print(trenner.join((bot)) + " Bottle of Beer on the... WAAAAALLLLLL! Yeah!")
