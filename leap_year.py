years=[2000, 1800, 1900, 2400, 2100, 2200, 2300, 2500, 2023, 2024, 2020]

def is_leap(year):
    leap=False
    if year%4==0:
        if year%400==0:
            leap=True
        elif year%100==0:
            leap=False
        else:
            leap=True
    return leap

for i in years:
    print(i, ":", is_leap(i))