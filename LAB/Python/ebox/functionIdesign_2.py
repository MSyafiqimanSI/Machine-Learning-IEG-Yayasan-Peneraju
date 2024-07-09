def daysInYear(year,notleapyear=False):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return notleapyear
    elif year % 4 == 0:
        return True
    
year = int(input())
if daysInYear(year) == True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")