# yl4
# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud
# arvust miinimumi (ära kasuta min funktsiooni).
# (muutuja - variable, tingimus - condition, if-lause - if statement)

a = int(input('Esimene arv: '))
b = int(input('Teine arv: '))

if a < b:
    print('Arvutan miinimumi ...')
    print(a, 'on miinimum')
else:
    print(b, 'on miinimum')