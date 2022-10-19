#from getpass import getpass
import hashlib
name= input('Benutzername:')
print('Password:')
PW= hashlib.sha512((name + input() +'peppercornneumanndoorkleepause').encode()).hexdigest()
if(PW=='529c0ebbb3bb3e3615ec65e75fba01af523e613e76e1614d09d9a38037fa64b05ef997db544d560b886f317a731e5de746303692abaa2a9c202bf5c969caae50'):
    print('Geheimnis')