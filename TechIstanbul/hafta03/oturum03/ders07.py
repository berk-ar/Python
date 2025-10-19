import os

print("---ALIŞVERİŞ LİSTESİ---")

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaAdi = bulundugumDizin + "/" + "alisverisListesi.txt"

with open(dosyaAdi, "a", encoding="utf-8") as dosya:
    while True:
        item = input("Lütfen ürün giriniz (Çıkmak için Q yazın): ")
        if item.lower() == "q":
            break
        else:
            dosya.write(item + "\n")