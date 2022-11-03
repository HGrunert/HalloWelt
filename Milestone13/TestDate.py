import time
import datetime

#print('\n'.join(dir(time)))
#print(time.time.__format__(#######))
print(datetime.date.today().day)
td = datetime.date(2004,2,29)
print(td.isocalendar())

str = input('datum (im Format "01.11.22"):')

dt = datetime.datetime.strptime(str, "%d.%m.%y").date()
print(dt)