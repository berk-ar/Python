"""
sayi = int(input("bir sayı giriniz: "))
ssayi = str(sayi)
toplam = 0
for rakam in ssayi:
    kup = int(rakam)**len(ssayi)
    toplam += kup
    print(rakam, kup, toplam)
if toplam == sayi:
    print(f"girilen {sayi} bir armstrong bir sayıdır.")
else:
    print(f"girilen {sayi} bir armstrong sayısı değildir {toplam}")
"""

for i in range(1,1000):
    sayi = i
    ssayi = str(sayi)
    toplam = 0
    for rakam in ssayi:
        kup = int(rakam)**len(ssayi)
        toplam += kup
       # print(rakam, kup, toplam)
    if toplam == sayi:
        print(f"girilen {sayi} bir armstrong bir sayıdır.")
    #else:
       # print(f"girilen {sayi} bir armstrong sayısı değildir {toplam}")