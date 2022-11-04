#bitte die E-Book PDF- Seiten (pdf-seite) 198-225 bearbeiten
#verwende paramiko und urllib um ein tool zu schreiben, das folgende aufgaben erfüllt
#erstelle für die cli und für die Gui folgende Views:
#ssh command-eingabe
#ssh rückgabe in dictionary-liste speichern (für spätere Analysen)
#ssh rückgaben auflisten
#url aufruf und check der rückgabe ob der Server eine HTML-Seite zurückliefert
#url status der aufrufe in eine Liste speichern
#url statis in dicht/liste anzeigen lassen
#Auswahl ob dies über cli oder gui passieren soll.
#advanced:
#frage per ssh z.B. die Bash_history aus und suche nach schlüsselworten in den ausgabezeilen
#benötigte funktonen:
import os.path
import tkinter as tk
from urllib import request
class Sshinput:
    def __init__(self,user='',password='',ip='',port=22,cmd='ls -la',file='none'):
        import paramiko
        self.user=user
        self.password=password
        self.ip=ip
        self.port=port
        self.cmd=cmd
        self.file=file
        self.client= paramiko.SSHClient()
        self.output=None
    def setcommand(self,cmd):
        self.cmd=cmd
    def execute(self,cmd=True):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if(cmd):
            command=self.cmd
        else:
            command=cmd
        if (self.file.lower() == 'none'):
            self.client.connect(self.ip, port=self.port, username=self.user, password=self.password)
            _, stdout, stderr = self.client.exec_command(command)
            self.output = stdout.readlines() + stderr.readlines()
            for line in self.output:
                print(line.strip())  # if fehlermeldung, nächstes, else, safe the credentials and next IP
        else:
            self.client.connect(self.ip, port=self.port, username=self.user, key_filename=self.file)
            _, stdout, stderr = self.client.exec_command(command)
            self.output = stdout.readlines() + stderr.readlines()
            for line in self.output:
                print(line.strip())  # if fehlermeldung, nächstes, else, safe the credentials and next IP


        return self.output
#frame und co initialisieren Alex
##initGui Alex
def initgui():
    global root
    root = tk.Tk()
    global frame
    frame = tk.Frame(root)
#variablen, dics{}, lits() Ben
##initAll()
def initAll():
    saveSCRSdic = {}
    savePara = {}
    saveSCRSitems = {'Status', 'Command', 'Rückgabe', 'Status'}
#basis menü (cli oder gui) Ben

def rungui():
    return(False)

def runcli():
    while True:
        whatopen()
    return(False)

#hauptmenü für die auswahl von urllib oder paramiko
def whatopen():
    choiche=input('Urllib or Paramiko?')
    if(choiche.lower()=='urllib'):
        runurllibcli()
    elif(choiche.lower()=='paramiko'):
        runparamikocli()
    elif(choiche.lower()=='exit'):
        exit()
##chooseUserUrlPara()
def runurllibcli():
    from urllib import request
    url = input('URL?')
    rueckgabewert = request.urlopen(url)
    # print("Dateigröße in Bytes: ", rueckgabewert.length)
    inhalt = rueckgabewert.read()
    print(type(inhalt))
    inhalt_text = inhalt.decode("UTF-8")
    while True:
        choiche=input('type \n print \n exit')
        if choiche=='type': print(type(inhalt_text))
        elif choiche=='print': print(inhalt_text)
        elif choiche=='exit': break
    whatopen()

def runparamikocli():
    #user=getpass.getuser()
    user=input('Username:')
    #password= getpass.getpass()
    password =input('Password:')
    ip= input('Enter server IP:') or '192.168.1.203'
    port = input('Enter port or <CR>:') or 2222
    cmd = input('Enter command:') or 'id'
    ssh_command=Sshinput(user,password,ip,port,cmd)
#eingabemasken sowohl im cli und gui (einzelabfrage auf einen server)
#eingabemaske für paramiko (einzelabfrage auf einen server)
##CliInputForm()
##GuiInputForm()
#eingabemask für das erstellen einer serverliste
##CliServerInputForm()
##GuiServerInputForm()
#check auf den status der abfrage
##Check unabhängig von GUI/CLI
###CheckSshDict()
###savePara{}
#check ist das commando ausgeführt worden (ja/nein/errormsg)
##Check unabhängig von GUI/CLI
###CheckCmdDict()
#speicherfunktion in eine liste (server, commando, rückgabe, status) in ein dict {} speichern
##SaveSCRS()
###saveSCRSitems = {'Status', 'Command', 'Rückgabe', 'Status'}
#funktion zum anzeigen der liste(n)
##showlists()
#eingabemaske für urllibs (einzelabfrage auf einen server)
##aksUrl()
#eingabemask für das erstellen einer serverliste
##makeUrlList()
#check auf den status der abfrage
##checkStatus()


##userchooseGuiCli
if(input('Do you want a GUI? y/n')=='y'):
    rungui()
else:
    runcli()


def showWebsite():
    print("Anfang des Inhalts:", rueckgabewert.peek())
'''
urls =[]
urls.append('http://www.google.com/')
urls.append('http://www.example.com/')
urls.append('http://www.heise.com/')
urls.append('http://www.golem.de/')
urls.append('http://www.heise.de/')
for url in urls:
    rueckgabewert = request.urlopen(url)
    if rueckgabewert.code == 200:
        print("webseite konnte geladen werden")
        print(url)
        showWebsite()
    elif rueckgabewert.code == 400:
        print("fehlerhafte URL",url)
    elif rueckgabewert.code ==403:
        print("Zugriff nicht erlaubt",url)
    elif rueckgabewert == 404:
        print("URL konnte nicht gefunden werden",url)
    else:
        print("Unbekannter Fehler",url)
'''
#check ist das commando ausgeführt worden (ja/nein/errormsg)
##checkCmd()
#speicherfunktion in eine liste
##saveList()
#speicherfunktion in eine liste (url, rückgabe(webside), status) = in ein dict {}
##saveListUrl()
#funktion zum anzeigen der liste(n)
##showList()
#Hauptmenu
##hauptmenu()
#cli hauptprogramm
