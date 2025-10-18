# Praktikaülesanded 1–14 (lihtne versioon)

import math
import random
from datetime import date

# 1. Juku
print("Ülesanne 1: Juku")
nimi = input("Sisesta nimi: ")
if nimi == "JUKU":
    print("Nimi on suurte tähtedega – lähme Jukuga kinno!")
else:
    print("Nimi ei sobi.")

vanus = input("Sisesta Juku vanus: ")
if vanus.isdigit():
    vanus = int(vanus)
    if vanus < 0 or vanus > 100:
        print("Viga andmetega!")
    elif vanus < 6:
        print("Tasuta")
    elif vanus <= 14:
        print("Lastepilet")
    elif vanus <= 65:
        print("Täispilet")
    else:
        print("Sooduspilet")
else:
    print("Palun sisesta täisarv!")

# 2. Pinginaabrid
print("\nÜlesanne 2: Pinginaabrid")
a = input("Sisesta esimese õpilase nimi: ")
b = input("Sisesta teise õpilase nimi: ")
if a.isalpha() and b.isalpha():
    if random.choice([True, False]):
        print(f"{a} ja {b} on täna pinginaabrid!")
    else:
        print(f"{a} ja {b} ei ole täna pinginaabrid.")
else:
    print("Nimed peavad koosnema ainult tähtedest!")

# 3. Remont
print("\nÜlesanne 3: Remont")
pikkus = float(input("Sisesta toa pikkus (m): "))
laius = float(input("Sisesta toa laius (m): "))
pindala = pikkus * laius
print("Põranda pindala:", pindala, "m2")
soov = input("Kas soovid remonti teha? (jah/ei): ")
if soov.lower() == "jah":
    hind = float(input("Kui palju maksab 1 m² materjal: "))
    summa = pindala * hind
    kes = input("Kas teed ise või professionaal? (ise/prof): ")
    if kes.lower() == "prof":
        too = float(input("Kui palju maksab töö 1 m² kohta: "))
        summa += too * pindala
    print("Remondi kogumaksumus:", summa, "€")
else:
    print("Remonti ei tehta.")

# 4. Allahindlus
print("\nÜlesanne 4: Allahindlus")
hind = float(input("Sisesta toote hind: "))
if hind > 700:
    print("30% soodushind:", hind * 0.7)
else:
    print("Soodustust ei saa.")

# 5. Temperatuur
print("\nÜlesanne 5: Temperatuur")
t = float(input("Sisesta temperatuur: "))
if t > 18:
    print("Soe ja sobiv temperatuur.")
else:
    print("Võib olla jahe.")

# 6. Pikkus
print("\nÜlesanne 6: Pikkus")
h = float(input("Sisesta pikkus (cm): "))
if h < 160:
    print("Lühike")
elif h <= 180:
    print("Keskmine")
else:
    print("Pikk")

# 7. Pikkus ja sugu
print("\nÜlesanne 7: Pikkus ja sugu")
h = float(input("Sisesta pikkus (cm): "))
sugu = input("Sisesta sugu (m/n): ")
if sugu == "m":
    if h < 170:
        print("Lühike mees")
    elif h <= 185:
        print("Keskmine mees")
    else:
        print("Pikk mees")
elif sugu == "n":
    if h < 160:
        print("Lühike naine")
    elif h <= 175:
        print("Keskmine naine")
    else:
        print("Pikk naine")
else:
    print("Sugu vale!")

# 8. Pood
print("\nÜlesanne 8: Pood")
kaubad = ["piim", "sai", "leib"]
hinnad = {k: round(random.uniform(1, 5), 2) for k in kaubad}
kokku = 0
for k in kaubad:
    print(f"{k} maksab {hinnad[k]} €")
    soov = input(f"Kas soovid osta {k}? (jah/ei): ")
    if soov.lower() == "jah":
        kogus = int(input("Mitu tükki: "))
        kokku += kogus * hinnad[k]
print("Kokku maksad:", kokku, "€")

# 9. Ruut
print("\nÜlesanne 9: Ruut")
a = float(input("Sisesta 1. külg: "))
b = float(input("Sisesta 2. külg: "))
c = float(input("Sisesta 3. külg: "))
d = float(input("Sisesta 4. külg: "))
if a == b == c == d and a > 0:
    print("See on ruut!")
else:
    print("See ei ole ruut.")

# 10. Matemaatika
print("\nÜlesanne 10: Matemaatika")
x = float(input("Sisesta esimene arv: "))
y = float(input("Sisesta teine arv: "))
op = input("Sisesta tehe (+ - * /): ")
if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    if y != 0:
        print(x / y)
    else:
        print("Viga: nulliga ei saa jagada!")
else:
    print("Tundmatu tehe!")

# 11. Juubel
print("\nÜlesanne 11: Juubel")
aasta = int(input("Sisesta sünniaasta: "))
praegu = date.today().year
vanus = praegu - aasta
if vanus % 5 == 0:
    print("See on juubel!")
else:
    print("Pole juubel.")

# 12. Müük
print("\nÜlesanne 12: Müük")
hind = float(input("Sisesta toote hind: "))
if hind <= 10:
    print("Soodushind 10%:", hind * 0.9)
else:
    print("Soodushind 20%:", hind * 0.8)

# 13. Jalgpallimeeskond
print("\nÜlesanne 13: Jalgpalli meeskond")
sugu = input("Sisesta sugu (m/n): ")
if sugu == "n":
    print("Naissoost kandidaate ei küsita vanust – ei sobi meeskonda.")
else:
    vanus = int(input("Sisesta vanus: "))
    if 16 <= vanus <= 18:
        print("Sobib meeskonda!")
    else:
        print("Ei sobi – vale vanus.")

# 14. Bussid
print("\nÜlesanne 14: Busside logistika")
inimesi = int(input("Sisesta inimeste arv: "))
kohad = int(input("Mitu kohta ühes bussis: "))
busse = math.ceil(inimesi / kohad)
viimases = inimesi % kohad if inimesed % kohad != 0 else kohad
print("Busse vaja:", busse)
print("Viimases bussis inimesi:", viimases)
