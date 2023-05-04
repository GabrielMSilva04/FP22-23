# isLeapYear(year) deve devolver True se year é um ano bissexto
# e False se é um ano comum.  Corrija-a.
# (See: https://en.wikipedia.org/wiki/Leap_year)
def isLeapYear(year):
    return ((year%4 == 0 and year%100 != 0) or year%400 == 0)


# monthDays deve devolver o número de dias de um dado mês num dado ano.
# Por exemplo, monthDays(2004, 2) deve devolver 29.
# Corrija-a.
def monthDays(year , month):
    if ((year%4 == 0 and year%100 != 0) or year%400 == 0):
        MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    else:
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = MONTHDAYS[month]
    
    return days


# nextDay deve devolver o dia a seguir a uma dada data.
# Por exemplo, nextDay(2017, 1, 31) deve devolver (2017, 2, 1)
def nextDay(year, month, day):
    day += 1
    
    days = monthDays(year , month)
    if day>days and month==12:
        year=year+1
        month=1
        day=1
    elif day>days:
        month=month+1
        day=1
    
    return year, month, day



# Defina uma função dateIsValid que deve
# devolver True se os seus argumentos formarem uma data válida
# e devolver False no caso contrário.
# Por exemplo, dateIsValid(1980, 2, 29) deve devolver True,
# dateIsValid(1980, 2, 30) deve devolver False.
def dateIsValid(year, month, day):
    days = monthDays(year , month)
    if day>days:
        valid=False
    elif month<0 or month>12:
        valid=False
    else:
        valid=True
    return valid



# Defina uma função previousDay que devolva o dia anterior a uma dada data.
# Por exemplo, previousDay(1980, 3, 1) deve devolver (1980, 2, 29)
def previousDay(year, month, day):
    if day==1 and month==1:
        year=year-1
        month=12
        day = monthDays(year , month)
    elif day==1:
        month=month-1
        day = monthDays(year , month)
    else:
        day -= 1
    
    return year, month, day

# No Codecheck, não chame nenhuma função: o sistema trata disso.