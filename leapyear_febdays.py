def is_year_leap(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    list_31 = [1,3,5,7,8,10,12]
    list_30 = [4,6,9,11]
    if month in list_31 :
        return 31
    elif month in list_30 :
        return 30
    elif is_year_leap(year) and month == 2:
        return 29
    # elif is_year_leap(year) != True and month == 2:
    else:
        return 28


x = int(input('Enter any year: '))
y  = int(input('Enter a month: '))


l_p = is_year_leap(x)
month_in_lp = days_in_month(x,y)

print(l_p, month_in_lp)
