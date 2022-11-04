import paramiko

def ssh_command(ip,port,user,passwd='0',cmd='ls',file='none'):
    client =paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if(file=='none'):
        client.connect(ip, port=port, username=user, password=passwd)
        _ , stdout, stderr =client.exec_command(cmd)
        output = stdout.readlines() + stderr.readlines()
        for line in output:
            print(line.strip()) #if fehlermeldung, nächstes, else, safe the credentials and next IP


if __name__ == '__main__':
    import getpass
    #user=getpass.getuser()
    user=input('Username:')
    #password= getpass.getpass()
    password =input('Password:')
    ip= input('Enter server IP:') or '192.168.1.203'
    port = input('Enter port or <CR>:') or 2222
    cmd = input('Enter command:') or 'id'
    ssh_command(ip,port,user,password,cmd)


#bitte die E-Book PDF- Seiten (pdf-seite) 198-225 bearbeiten

#verwende paramiko und urllib um ein tool zu schreiben, das folgende aufgaben erfüllt

#erstelle für die cli und für die Gui folgende Views:

#ssh command-eingabe
#ssh rückgabe in dictionary-liste speichern (für spätere Analysen)
#ssh rückgaben auflisten

#advanced:
#frage per ssh z.B. die Bash_history aus und suche nach schlüsselworten in den ausgabezeilen