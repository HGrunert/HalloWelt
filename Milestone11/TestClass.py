class Tier:
    def __init__(self):
        self.tierart = "Biene"
        self.bewegung = 'fliegen'
        self.laut ='sum sum'
        self.name = "Maja"

    def set_species(self,species1):
        self.tierart = species1

    def get_species(self):
        return self.tierart

    def bewegen(self):
        return self.bewegung

    def laut_geben(self):
        return self.laut

    def set_name(self,name1):
        self.name = name1

    def get_name(self):
        return self.name

class Gast:
    def __init__(self,vname='NA',nname=' ',email='not@given.nowhere',\
                 allergie='unknown',telephone_Nr='000000',gender='Attack Helicopter',\
                 impfstatus=False,covid=False,status='invited'):
        self.vname= vname
        self.nname= nname
        self.email= email
        self.allergie= allergie
        self.telephone_Nr= telephone_Nr
        self.gender= gender
        self.impfstatus=impfstatus
        self.covid=covid
        self.status=status
    #region #getset
    def set_nname(self,name):
        self.nname =name

    def get_nname(self):
        return self.nname

    def set_vname(self,name):
        self.vname =name

    def get_vname(self):
        self.vname =name

    def set_email(self, inp):
        self.email = inp

    def get_email(self):
        return self.email

    def set_telephone_Nr(self, inp):
        self.telephone_Nr = inp

    def get_telephone_Nr(self):
        return self.telephone_Nr

    def set_allergie(self, inp):
        self.allergie = inp

    def get_allergie(self):
        return self.allergie

    def set_gender(self, inp):
        self.gender = inp

    def get_gender(self):
        return self.gender

    def set_status(self, inp):
        self.status = inp

    def get_status(self):
        return self.status

    def set_impfstatus(self, inp):
        self.impfstatus = inp

    def get_impfstatus(self):
        return self.impfstatus

    def set_covid(self, inp):
        self.covid = inp

    def get_covid(self):
        return self.covid
    #endregion
    ##functions
    def ask_values(self):
        self.set_vname(input("Vorname:".rjust(20)))
        self.set_nname(input("Nachname:".rjust(20)))
        self.set_telephone_Nr(input("Tel.:".rjust(20)))
        self.set_email('lol')  # set mail to something
        while ((self.email.count('@') * self.email.count('.')) == 0):  # solange entweder
            self.set_email(input("EMail:".rjust(20)))  # 0@s oder 0 punkte drin sind
            if ((self.email.count('@') * self.email.count('.')) == 0):
                print('ERROR:Not an email.')  # und gib ne errormeldung an
        self.set_allergie(input("Allergene:".rjust(20)))
        self.set_gender(input("Gender:".rjust(20)))
        if (input('rsvp? j/n'.rjust(20)) =='j'): self.set_status('confirmed')
        if (input('Geimpft? j/n'.rjust(20)) == 'j'): self.set_impfstatus(True)
        if not(input('CoViD Positiv? j/n'.rjust(20)) == 'n'):
            self.set_impfstatus(True)
            print('Interpreting vague answer as "Yes".')

ben=Gast('Ben', 'Ertel')
ben.ask_values()
