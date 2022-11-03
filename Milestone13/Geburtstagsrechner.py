import time
import datetime
import locale
import calendar



def findin(it,list):
    for i in list:
        if i==it:
            return(list.index(it),False)
    return(0,True)

def get_data_from_user_view():  # view #  eingabe eines Datums und zerlegen in jahr, monat, tag
    while True:
        sday = input('Zahl für den Tag:') #if type == int or sanitizer mit 2 var
        smonth = input('Zahl für den Monat:')
        syear = input('Jahreszahl:')
        if(sday.isnumeric() and smonth.isnumeric() and syear.isnumeric()):
            return(datetime.date(syear,smonth,sday))
        print('Error, not a number.')
def timezone():
    fin = True
    while fin:
        print('Choose Timezone:')
        timezones=['CEST','GMT','CVT','GST','WGT','ADT','EDT','CDT','MDT','MST','AKDT']
        print('\n'.join(timezones))
        tzinp = input('Timezone:')
        check=findin(tzinp,timezones)
        fin=check[1]
    return(check[0])

def calculate(day1,day2):
    if(int(day1.year) -int(day2.year)<0):
        ooy = 'Jahre älter'
        diff= int(day2.year) -int(day1.year)
    elif(day1.year == day2.year):
        if(int(day1.month) -int(day2.month)<0):
            ooy = 'Monate älter'
            diff= int(day2.month) -int(day1.month)
        elif(int(day1.month)==int(day2.month)):
            if(day1.day==day2.day):
                return('gleich alt',0)
            elif(int(day1.day)<int(day2.day)):
                ooy = 'Tage älter'
                diff= int(day2.day) -int(day1.day)
            else:
                ooy = 'Tage jünger'
                diff= int(day1.day) -int(day2.day)
        else:
            ooy = 'Monate jünger'
            diff = int(day1.month) - int(day2.month)
    else:
        ooy = 'Jahre jünger'
        diff = int(day1.year) - int(day2.year)
    return(ooy,diff)

print(timezone())
while True:
    b1 = True
    while b1:
        print('Dein Geburtstag:')
        bday1 = calendar_class.get_data_from_user_view()
        b1 = not bday1.check_datum()
    b2 = True
    while b2:
        print('Anderer Geburtstag:')
        bday2 = calendar_class.get_data_from_user_view()
        b2 = not bday2.check_datum()
    ans=calculate(bday1,bday2)
    if ans[1]:
        print('Der andere ist', ans[1],ans[0])
    else:
        print('Die beiden sind gleich alt.')
    if input('Type Exit to quit').lower() =='exit': break


def timedeltaToHours(delta):
    sec = delta.seconds
    daysToHours = delta.days * 24
    hours = sec // (60 * 60)
    minutes = (sec - (hours * 60 * 60)) // 60
    return str(hours + daysToHours) + ":" + str(minutes) + " h"
