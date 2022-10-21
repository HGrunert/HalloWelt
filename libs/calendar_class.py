#import nothing
datamonths =[]
datamonths =[0,31,28,31,30,31,30,31,31,30,31,30,31]
class Datum_setgets:
    def __init__(self,jahr=1,monat=1,tag=1):
        self.year = jahr
        self.month =monat
        self.day = tag
    def get_year(self):
        return int(self.year)
    def set_year(self,inp):
        if inp: self.year= int(inp)
        else: print('no year 0')
    def get_month(self):
        return int(self.month)
    def set_month(self,inp):
        if inp < 13 and inp > 0:
            self.month= int(inp)
        else:print('invalid month')
    def get_day(self):
        return int(self.day)
    def set_day(self,inp):
        if inp<=self.get_days() and inp >0:
            self.day= inp
        else:print('invalid day')

class Datum(Datum_setgets):
    def __init__(self,jahr,monat,tag):
        self.year = jahr
        self.month =monat
        self.day = tag
    def get_days(self): #show me how many days the month in that year has/had
        monthsd = [] #listen kopieren ist nicht trivial wie monthsd = datamonths da der dann einfach
        # nur den Speicherort weitergibt
        monthsd.extend(datamonths)# d.h. riesige SideEffects macht.
        if(self.get_year() > 1901):
            if(not(self.get_year()%4)):
                monthsd[2] = 29
        return(monthsd[self.get_month()])
    def get_months(self): #get me a list of the months with their number of days for a year
        monthsm = [] #listen sind clunky, nicht pythonisch
        monthsm.extend(datamonths)
        monthsm[2] = get_days(date.get_year(),2)
        return(monthsm)
    def get_years(self): #Make a list of 100 years after year
        return(list(range(self.get_year(),self.get_year()+100)))
    def check_schaltjahr(self):  #
        if (self.get_year() > 1901):
            if (self.get_year() % 4):
                return (False)
            return (True)
        return (False)
    def check_datum(self):  # model#  prüfen ob das Datum korrekt eingegeben wurde
        if(not(self.get_year())):
            return (False)
        if (self.get_month() > 12 or self.get_month() < 1):  # Also check <0
            return (False)
        if ((self.get_day() > self.get_days()) or (1 > self.get_day())):
            return (False)
        return (True)
    def view(self):  # view #  ausgabe ob datum korrekt ist
        if (self.check_datum()):
            print(self.get_year(), '-', self.get_month().__str__().zfill(2), '-', self.get_day().__str__().zfill(2))
        else:
            print('Error, Datum existiert nicht.')


def get_data_from_user_view():  # view #  eingabe eines Datums und zerlegen in jahr, monat, tag
    while True:
        sday = input('Zahl für den Tag:') #if type == int or sanitizer mit 2 var
        smonth = input('Zahl für den Monat:')
        syear = input('Jahreszahl:')
        if(sday.isnumeric() and smonth.isnumeric() and syear.isnumeric()):
            return(Datum(syear,smonth,sday))
        print('Error, not a number.')

def calendarprint(yearcal):
    monsc = [] #non pythonic lists
    monsc.extend(Datum(yearcal).get_months())
    for mon in monsc[1::]:
        print(' [ ]'+ ' [ ]'.join(str(x) for x in range(1,mon+1)))

print(Datum(2000,2).get_days)
print(Datum(1950).get_years())
print(get_data_from_user_view().check_datum)
#for year in get_years(1945):
#    print(year, ':')
#    print(177*'=')
#    calendarprint(year)

date = get_data_from_user_view()
#print(date)
#print(check_schaltjahr(date))
date.view()