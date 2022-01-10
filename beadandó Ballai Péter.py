import math
print("üdv a geomatriai számoló programomban")

#elfogadott válaszok listája
valaszok = [1,2]

print("1 - Téglatest\n2 - Gömb")

#válasz bekérése
valasz = int(input("add meg a testhez tartozó számot a számításhoz: "))

#válasz bekérése, amíg nem jó
while valasz not in valaszok:
    valasz = int(input("légyszi érvényes számot adj meg! "))

#megnézi, hogy melyik testtel számoljon
if valasz == valaszok[0]:

    #oldalak bekérése
    a = float(input("add meg a téglatest a oldalát cm-ben: "))
    b = float(input("add meg a téglatest b oldalát cm-ben: "))
    c = float(input("add meg a téglatest c oldalát cm-ben: "))

    #ha egy kocka írja ki, hogy ez egy kocka
    if a == b == c:
        print("ez egy kocka!")

    #számítás száma bekérése
    print("1 - Térfogat\n2 - Felszín")
    teglavalasz = int(input("add meg a számítsához tartozó számot: "))
    while teglavalasz not in valaszok:
        teglavalasz = int(input("légyszi érvényes számot adj meg! "))

    #térfogat számítása
    if teglavalasz == valaszok[0]:
        teglaV = (a*b*c)
        print(teglaV, "cm^3", "\n",
        teglaV/1000, "dm^3", "\n",
        teglaV/1000000, "m^3")

    #felszín számítása
    if teglavalasz == valaszok[1]:
        teglaA = (2*(a*b + a*c + b*c))
        print(teglaA, "cm^2", "\n",
        teglaA/100, "dm^2", "\n",
        teglaA/10000, "m^2")

if valasz == valaszok[1]:

    #sugár bekérése
    r = float(input("add meg a gömb sugarát cm-ben: "))

    #számítás száma bekérése
    print("1 - Térfogat\n 2 - Felszín")
    gombvalasz = int(input("add meg a számítsához tartozó számot: "))
    while gombvalasz not in valaszok:
        gombvalasz = int(input("légyszi érvényes számot adj meg! "))

    #térfogat számítása
    if gombvalasz == valaszok[0]:
        gombV = (4*r**2*math.pi)/3
        print(gombV, "cm^3", "\n",
        gombV/1000, "dm^3", "\n",
        gombV/1000000, "m^3" )

    #felszín számítása
    if gombvalasz == valaszok[1]:
        gombA = (4*r**2*math.pi)
        print(gombA, "cm^2", "\n",
        gombA/100, "dm^2", "\n", 
        gombA/10000, "m^3")
    print("a gömb átmérője: ", r*2, "cm")
