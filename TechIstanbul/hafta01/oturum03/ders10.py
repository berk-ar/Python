carpim = 1
adet = 0
girilen_sayilar = ""

while True:
    sayi = int(input("Bir sayı giriniz: "))
    if sayi == 0:
        continue
    carpim *= sayi
    adet += 1
    girilen_sayilar += str(sayi) + " - "

    if adet == 10:
        print("10 adet 0'dan farklı sayı girdiniz.")
        print("Girilen sayıların çarpımı: ", carpim)
        print("Girilen sayılar", girilen_sayilar)
        break