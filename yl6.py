# yl6
# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud
# arvust maksimumi (ära kasuta max funktsiooni).
# (loogikatehted - logic operators)

a = int(input('Sisesta a: '))
b = int(input('Sisesta b: '))
c = int(input('Sisesta c: '))

if a > b and a > c:
    print(a, 'on maksimum')
elif b > c:
    print(b, 'on maksimum')
else:
    print(c, 'on maksimum')


