fiyatlar = {"elma": 8, "muz": 12, "armut": 9}

toplam = 0

for fiyat in fiyatlar.values():
    toplam += fiyat

print("Toplam tutar", toplam)