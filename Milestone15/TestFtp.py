
#from urllib import request
url = 'https://www.example.com/'
'''
rueckgabewert = request.urlopen(url)
#print("Dateigröße in Bytes: ", rueckgabewert.length)
print("Anfang des Inhalts:", rueckgabewert.peek())
inhalt = rueckgabewert.read()
print(type(inhalt))
inhalt_text = inhalt.decode("UTF-8")
print(type(inhalt_text))
print(inhalt_text)
'''
####pip install requests
import requests
r= requests.get(url)
print(r.text)

rp = requests.get('https://www.python-lernen.de/bilder/biene-sprite-animiert-01.gif')
with open('biene.gif', 'wb') as f: #öffne eine neue Datei, benenne sie biene.gif
    #                        # und gib ihr die bezeichnung f
    f.write(rp.content) #schreib r.content in das file f
#read out header
r = requests.get(url)
print(r.status_code)
print(r.ok)
print(r.headers)

##You can also do get and post
payload = {'key1': 'value1', 'key2': 'value2'}
r=requests.post("https://httpbin.org/post", data=payload)
print(r.text)
print(r.status_code)
print(r.ok)

r = requests.get("http://httpbin.org/get", params=payload)
print (r.text)
