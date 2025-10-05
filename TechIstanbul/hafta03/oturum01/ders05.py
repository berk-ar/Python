meyveler = ["elma", "armut", "çilek", "muz", "portakal"]
print(f"Meyveler: {meyveler}")

try:
    indeks = int(input("Hangi meyveyi görmek istersiniz (0-4): "))

    secilenMeyve = meyveler[indeks]

    print(f"Seçilen Meyve: {secilenMeyve}")

except ValueError:
    print("HATA: Lütfen bir sayı girin! 0-1-2-3-4")
except IndexError:
    print(f"HATA: Geçersiz Numara! Sadece 0-{len(meyveler)-1} arası girebilirsiniz")
else:
    print(f"Afiyet olsun. {secilenMeyve}")
finally:
    print("İşlem Tamamlandı.")