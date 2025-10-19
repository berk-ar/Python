# CSV (Comma Separated Values), veri depolamak icin yaygin kullanilan bir formattir.
# Excel, Google Sheats verileri genellikle .csv formatındadır.

import os
bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaAdi = bulundugumDizin + "/" + "ogrenciler.csv"

with open(dosyaAdi, "w", encoding="utf-8") as f:
    f.write("isim,yas,bolum\n")
    f.write("Berk,25,Yazılım\n")
    f.write("Tuğba,25,Muhasebe\n")
    f.write("Ronaldo,40,Besyo\n")

with open(dosyaAdi, "r", encoding="utf-8") as f:
    for satir in f:
        print(satir.strip())    # boşlukları siler
        print(satir.strip().split(","))