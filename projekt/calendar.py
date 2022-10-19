#import nothing
datamonths =[]
datamonths =[0,31,28,31,30,31,30,31,31,30,31,30,31]

def get_days(year,month): #show me how many days the month in that year has/had
    monthsd = [] #listen kopieren ist nicht trivial wie monthsd = datamonths da der dann einfach
    # nur den Speicherort weitergibt
    monthsd.extend(datamonths)# d.h. riesige SideEffects macht.
    if(year>1901):
        if(not(year%4)):
            monthsd[2] = 29
    return(monthsd[month])

def get_months(year): #get me a list of the months with their number of days for a year
    monthsm = [] #listen sind clunky, nicht pythonisch
    monthsm.extend(datamonths)
    monthsm[2] = get_days(year,2)
    return(monthsm)

def get_years(yeary): #Make a list of 100 years after year
    return(list(range(yeary,yeary+100)))


def get_data_from_user_view():  # view #  eingabe eines Datums und zerlegen in jahr, monat, tag
    day = int(input('Zahl für den Tag:'))
    month = int(input('Zahl für den Monat:'))
    year = int(input('Jahreszahl:'))
    datum ={'tag':day, 'monat':month,'jahr':year}
    return(datum)

def check_datum(datumc):  # model#  prüfen ob das Datum korrekt eingegeben wurde
    if(datumc['monat']>12):
        return(False)
    if (datumc['tag'] > get_days(datumc['jahr'],datumc['monat'])):
        return(False)
    return(True)

def check_schaltjahr(datums):  #
    if(year>1901):
        if(datums['jahr']%4):
            return (False)
        return(True)
    return(False)

def view_datum(datumv):  # view #  ausgabe ob datum korrekt ist
    if(check_datum(datumv)):
        print(datumv['jahr'],'/',datumv['monat'],'/',datumv['tag'])
    else:
        print('Error, Datum existiert nicht.')
    return(1)

def calendarprint(yearcal):
    monsc = [] #non pythonic lists
    monsc.extend(get_months(yearcal))
    for mon in monsc[1::]:
        print(' [ ]'+ ' [ ]'.join(str(x) for x in range(1,mon+1)))

#print(get_days(2000,2))
#print(get_years(1950))
#print(check_datum(get_data_from_user_view()))
for year in get_years(1945):
    print(year, ':')
    print(177*'=')
    calendarprint(year)