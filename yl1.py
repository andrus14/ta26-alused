# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab
# ümardatud tulemuse. (round)

# küsime kasutajalt summa kroonides
# teeme tehte, mis teisendab kroonid eurodeks
# ümardame tulemuse
# väljastame

eek = input("Sisesta kroonid: ")

eur = float(eek) / 15.6466
eur = round(eur, 2)

usd = float(eek) / 13.9999
usd = round(usd, 2)

print("Eurod:", eur)
print("Dollarid:", usd)

# print()

# print("Eurod: " + str(round(float(input("Sisesta kroonid: ")) / 15.6466, 2)))