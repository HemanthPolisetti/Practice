def is_leap(year):
    leap = False
    if year%400==0 and year%100==0 and year%4==0:
        leap=True
        return leap
    elif year==2100:
        leap=False
        return leap
    elif year%4==0:
        leap=True
        return leap
    else:
        return leap
year = int(input())
print(is_leap(year))