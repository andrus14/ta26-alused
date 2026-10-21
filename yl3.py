# yl3
# Kirjuta programm, mis küsib kasutajalt täisarvu
# n vahemikus 1-9. Arvuta n + nn + nnn väärtus ja
# väljasta see.
# (Näiteks kui kasutaja sisestab 2, siis on vaja
# väljastada tulemus 2 + 22 + 222 = 246).
# Ära kasuta korrutamistehet. Ülesanne on lahendatav
# ainult liitmise operaatorit kasutades.

n = input('Sisesta täisarv vahemikus 1-9: ')
nn = n + n
nnn = n + n + n
res = int(n) + int(nn) + int(nnn)
# res = n + nn + nnn

print(n + ' + ' + nn + ' + ' + nnn + ' = ' + str(res))

print(n + ' + ' + n + n + ' + ' + n + n + n + ' = ' + str(res))

print(n, '+', nn, '+', nnn, '=', res)

print(n, '+', n * 2, '+', n * 3, '=', res)

print('abc ' * 10)