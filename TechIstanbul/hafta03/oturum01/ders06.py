sayilar = [10, 20, 30, 40, 50]
print(f"Mevut liste: {sayilar}")

try:
    indeks = int(input("Listeden kullanmak istediğiniz indeksi giriniz (0-4): "))
    bolen = int(input("Bu sayıyı kaça böleceksiniz: "))
    secilenSayi = sayilar[indeks]
    sonuc = secilenSayi / bolen
    print(f"Sonuc: {secilenSayi} / {bolen} = {sonuc}")

except (ValueError, ZeroDivisionError, IndexError) as hata:
    print(f"HATA oluştu: {type(hata).__name__}")
    if isinstance(hata, ValueError):
        print("Lütfen geçerli bir tam sayı girin!")
    elif isinstance(hata, ZeroDivisionError):
        print("0'a bölünemez")
    elif isinstance(hata, IndexError):
        print("Geçersiz liste indeks girişi. 0-4 arası bir sayı girin.")