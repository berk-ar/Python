# parametresiz ve geriye değer döndüren methodlar
def selamla():
    isim = input("İsminizi giriniz: ")
    print("hoşgeldiniz", isim)
    return isim

print(selamla())

ad = selamla()
print(ad, type(ad))

def kat_kontrol(sayi, kat):
    if sayi % kat == 0:
        return sayi // kat

print(kat_kontrol(10,5))    # 2
print(kat_kontrol(10,3))    # None