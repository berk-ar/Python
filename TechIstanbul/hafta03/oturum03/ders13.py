import json
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaJson = bulundugumDizin + "/" + "kullanici.json"

kullanici = {
    "ad": "Berk",
    "yas": 25,
    "sehir": "İstanbul",
    "hobiler": ["futbol","yazılım"],
}

# JSON string'e dönüştürme
print(type(kullanici))  # <class 'dict'>
jsonString = json.dumps(kullanici, ensure_ascii=False, indent=2)
print("JSON String: ")
print(jsonString)
print(type(jsonString)) # <class 'str'>

# JSON dosyasını yazma
with open(dosyaJson, "w", encoding="utf-8") as dosya:
    json.dump(kullanici, dosya, ensure_ascii=False, indent=2)

# JSON dosyasını okuma
with open(dosyaJson, "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)
    print("\nOkunan Veri: ")    # {'ad': 'Berk', 'yas': 25, 'sehir': 'İstanbul', 'hobiler': ['futbol', 'yazılım']}
    print(veri)

# JSON string'den Python verisine dönüştürme
jsonVerisi = '{"isim": "Berk", "yas": 25}'
pythonVerisi = json.loads(jsonVerisi)
print(f"\nPython verisi: {pythonVerisi}")   # Python verisi: {'isim': 'Berk', 'yas': 25}

print(help(json))