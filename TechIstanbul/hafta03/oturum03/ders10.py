import csv
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaAdi = bulundugumDizin + "/" + "ogrenciler.csv"

# csv dosya yazma
with open(dosyaAdi, "w", newline="", encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["Ad","Soyad","Not"])   # başlık satırı
    yazici.writerow(["Berk","AR",95])
    yazici.writerow(["Tuğba","AR",100])

# csv formatında okuma
with open(dosyaAdi, "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        print(satir)

# sözlük formatında csv işlemleri
with open(dosyaAdi, "r", encoding="utf-8") as dosya:
    basliklar = dosya.readline().strip().split(",")
    print(basliklar)
    for satir in dosya:
        degerler = satir.strip().split(",")
        ogrenci = dict(zip(basliklar,degerler))
        print(ogrenci)