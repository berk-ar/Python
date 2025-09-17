import random

tutulan_sayi = random.randint(1,10)

tahmin = int(input("Bir sayı tahmininde bulununuz: "))

if tahmin == tutulan_sayi:
    print("Bildiniz, Tebrikler.")
else:
    print("Tutmadı, bir dahaki sefere.")
    print("Tutulan sayı: ",tutulan_sayi)