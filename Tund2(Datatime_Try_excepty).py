from datetime import *
from math import*



# Üleasnne 1
tana=date.today()
tanaf=date.today().strftime("%m/%d/%y")

print(f"Täna on {tana}")
d=tana.day
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

print("Tere tulemast")

nimi=input("Mis on sinu nimi? "). capitalize() #lower()-aaa, upper()-AAA,capitalize()-Aaa
print("Tere tulemast! Tevitan sind ", nimi)
print("Tere tulemast! Tevitan sind "+ nimi)
try:
    vanus=int(input("Kui vana sa oled? "))
    print("Tere tulemast! Tervitan sind  "+nimi+"Sa oled",vanus,"aastat vana")
    print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana")
except:
    print("On vaja numbreid sisalda!")


# Üleasnne 2
vastus1=3 + 8 / (4 - 2) * 4
vastus2=3+ 8/ 4 - 2 * 4
vastus3=((3+8)/ (4 - 2) * 4)
vastus3=round((3+8)/(4-2)*4)
print(vastus1,"\n",vastus2,"\n",vastus3)


# Ülesanne 3
try:
    R=float(input("Sisesta R: "))
    Sk=pi*R**2
    Skv=(2*R)**2
    Lkv=2*R*4
    print(f"Ringi pindala on{Sk}\nRingi ümnbermõõt on {Lk}\nRuudu
    pindala on {Skv} \nRuudu Ümbermõõt on {Lkv}\n")
except:
    print("On vaja number!")
    
# Üleasnne 4
maa_raadius=6378
mundi_diameter=2
mundi_diameter_km = mundi_diameter / 1000

maa_umbermooud=2*math.pi*maa_raadius
muntide_arv = maa_umbermooud / mundi_diameter_km

print(f"Maa ümbermõõt ekvaatori kohal: {maa_umbermooud} km")
print(f"Mündid, mis on vajalikud, et teha ümbermõõt: {muntide_arv:.0f}")

# Üleasnne 5
s = 'kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll kill-koll'
print(s.title())

# Üleasnne 6
laul = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""

def print_laulusonad(laul):
    print(laul.upper())

print_laulusonad(laul)
