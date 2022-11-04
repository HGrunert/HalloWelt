

import webbrowser
import urllib
from urllib import request
#print(help(urllib))
url= 'https://www.google.com'
#webbrowser.open(url)
#webbrowser.open_new(url)
#webbrowser.open_new_tab(url + '/search?q=lol')
#webbrowser.get('firefox').open_new_tab(url + '/search?q=lol')
#webbrowser.get('safari').open_new_tab(url + '/search?q=owolly')
rueck = request.urlopen(url)
print(type(rueck))

#url aufruf und check der rückgabe ob der Server eine HTML-Seite zurückliefert
#url status der aufrufe in eine Liste speichern
#url statis in dicht/liste anzeigen lassen

#Auswahl ob dies über cli oder gui passieren soll.


