# Kullanıcının ismini, yaşını, hobilerini al, hem .txt, hem .json olarak kaydet.

import json
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaTxt = bulundugumDizin + "/" + "bilgi.txt"
dosyaJson = bulundugumDizin + "/" + "bilgi.json"

print("---KİŞİSEL BİLGİ KAYIT---")
isim = input("İsim: ")
yas = int(input("Yaş: "))
hobiler = input("Hobiler(virgülle ayır): ").split(",")

# Sözlük oluştur
kisi = {
    "isim" : isim,
    "yas": yas,
    "hobiler": [hobi.strip() for hobi in hobiler]
}

# TXT olarak kaydet
with open(dosyaTxt, "w", encoding="utf-8") as f:
    f.write(f"İsim: {isim}\n")
    f.write(f"Yaş: {isim}\n")
    f.write(f"Hobiler: {', '.join(hobiler)}\n")

# JSON olarak kaydet
with open(dosyaJson, "w", encoding="utf-8") as f:
    json.dump(kisi, f, indent=4)

print("Bilgiler kaydedildi: bilgi.txt ve bilgi.json")