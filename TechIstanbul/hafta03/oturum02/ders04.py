import math
print("----Geometrik Hesaplamalar----")
try:
    yaricap = float(input("Dairenin yarıçapını giriniz: "))
    if yaricap <= 0:
        raise ValueError("Yarıçap pozitif olmalıdır!")
    
    # Math modülü ile hesaplamalar
    daireCevre = 2 * math.pi * yaricap
    daireAlan = math.pi * math.pow(yaricap, 2)
    print(f"\n Daire Bilgileri: ")
    print(f"Yarıçap: {yaricap}")
    print(f"Çevre: {daireCevre:.3f}")
    print(f"Alan: {daireAlan:.2f}")

    # Karekök ve üs hesapları
    karekok = math.sqrt(yaricap)
    karesi = math.pow(yaricap, 2)
    kupu = math.pow(yaricap, 3)
    print(f"\nDiğer Hesaplar:")
    print(f"Karekök: {karekok:.3f}")
    print(f"Karesi: {karesi:.2f}")
    print(f"Küpü: {kupu:.2f}")

    # Trigonometrik hesaplamalar
    aci = float(input("\nBir açı değeri girin (derece): "))
    aciRadyan = math.radians(aci)
    print(f"\nTrigonometrik Değerler: ")
    print(f"Sinüs: {math.sin(aciRadyan):.3f}")
    print(f"Kosinüs: {math.cos(aciRadyan):.3f}")
    print(f"Tanjant: {math.tan(aciRadyan):.3f}")
    
except ValueError as e:
    print(f"HATA: {e}")
except Exception as e:
    print(f"Beklenmeyen Hata: {e}")
print("Hesaplamalar tamamlandı.")