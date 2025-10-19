import os
import random

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaAdi = "oyun.txt"
dosyaAdi = bulundugumDizin + "/" + dosyaAdi

if not(os.path.exists(dosyaAdi)):
    dosya = open(dosyaAdi, "x", encoding="utf-8")
    dosya.close()


while True:
    cevap = int(input("Oyunu oyna 1,\t İstatistikler için 2,\t Çıkış yapmak için 3: "))
    if cevap == 1:
        dosya = open(dosyaAdi, "a")
        rastgele = random.randrange(1,100)
        dosya.write(str(rastgele)+"+")
        tahminSayisi = 10
        taban = 0
        tavan = 100
        while tahminSayisi >= 1:
            tahmin = int(input(f"Bir sayı tahmini yapınız {taban} - {tavan}: "))
            dosya.write(str(tahmin)+",")
            if tahmin == rastgele:
                dosya.write(f"{tahmin} + kazandınız.\n")
                dosya.close()
                print("Tebrikler")
                break
            elif tahmin > rastgele:
                print("Daha küçük bir sayı giriniz...")
                tavan = tahmin
            elif tahmin < rastgele:
                print("Daha büyük bir sayı giriniz...")
                taban = tahmin
            tahminSayisi -= 1
            print("Kalan tahmin sayısı: ", tahminSayisi)

            if tahminSayisi == 0:
                dosya.write("+ kaybettiniz.\n")
    elif cevap == 2:
        with open(dosyaAdi, "r") as dosyaOku:
            print(dosyaOku.read())
    elif cevap == 3:
        print("Çıkış yapıldı...")
        break