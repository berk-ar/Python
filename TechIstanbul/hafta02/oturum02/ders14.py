okul = {
    "12A": [
        {"ad": "Berk", "numara": "07"},
        {"ad": "Tuğba", "numara": "30"}
    ],
    "12B": [
        {"ad": "Ricardo", "numara": "17"},
        {"ad": "Almeida", "numara": "09"}
    ]
}

# Sınıfları ve öğrencileri listele
for sinif, ogrenci_listesi in okul.items():
    print(f"\n {sinif} Sınıfı: ")
    for ogrenci in ogrenci_listesi:
        print(f" -  {ogrenci["ad"]} (No: {ogrenci["numara"]})")