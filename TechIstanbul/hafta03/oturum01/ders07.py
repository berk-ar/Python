try:
    yas = int(input("Yaşınızı Giriniz: "))

    if yas < 0:
        raise ValueError("Yaş negatif olamaz!")
    elif yas <18:
        raise Exception("18 yaşında küçükler bu işlemi yapamaz!")
    elif yas > 120:
        raise Exception("Geçerli bir yaş girin!")
    
    print("İşleme devam ediliyor...")

except ValueError as ve:
    print(f"Sayı hatası: {ve}")
except Exception as e:
    print(f"Hata: {e}")

print("Kontrol Tamamlandı")