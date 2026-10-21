# yl8
# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv
# on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

year = int(input('Aasta: '))

# 1
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(year, 'on liigaasta')
else:
    print(year, 'on lihtaasta')

# 2
if year % 400 and (year % 4 or not year % 100):
    print(year, 'on lihtaasta')
else:
    print(year, 'on liigaasta')

# 3
if year % 400 == 0:
    print(year, 'on liigaasta')
elif year % 4 == 0 and year % 100 != 0:
    print(year, 'on liigaasta')
else:
    print(year, 'on lihtaasta')

