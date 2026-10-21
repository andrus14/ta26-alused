# yl7
# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv
# on paarisarv või mitte. (paarisarvu mõiste - odd/even)

n = int(input('Sisesta täisarv: '))

if not n % 2 == 0:
    print(n, 'on paaritu arv')
else:
    print(n, 'on paarisarv')

