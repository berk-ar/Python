import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaAdi = bulundugumDizin + "/" + "kurs.txt"

metin = "Techistanbul Python Bootcamp çok faydalı\n"
dosya = open(dosyaAdi, "w", encoding="utf-8")
dosya.write(metin)
dosya.close()

# Dosyayı açıp tekrar veri yazalım
with open(dosyaAdi, "a", encoding="utf-8") as dosya:
    dosya.write("bu kurs toplam 80 saat sürecek")

# İçerik okuma
with open(dosyaAdi, "r", encoding="utf-8") as dosya:
    print(dosya.read())