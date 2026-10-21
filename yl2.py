# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse
# ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

from math import pi

r = float(input("Sisesta raadius: "))

s = round(pi * r ** 2, 2)

p = round(2 * pi * r, 2)

print('Pindala on:', s)
print('Ümbermõõt on:', p)