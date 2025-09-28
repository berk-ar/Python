urunler = []

print("=== ÜRÜN STOK TAKİP ===")

"""
while True:
    urun = input("Ürün adını giriniz: ")
    fiyat = float(input("Fiyatını giriniz: "))
    stok = int(input("Stok miktarını giriniz: "))
    urunler.append({
        "urun": urun,
        "fiyat": fiyat,
        "stok": stok
    })
    print("Çıkmak için 'bitir' yazınız")
    exit = input("Çıkmak istiyor musunuz?: ")
    if exit.lower() == "bitir":
        break
print(urunler)
"""

while True:
    print("Çıkmak için 'bitir' yazınız")
    name = input("Ürün adını giriniz: ")
    if name.lower() == "bitir":
        break
    else:
        price = float(input("Ürün fiyatını giriniz: "))
        stock = int(input("Ürün stoğunu giriniz: "))
        urunler.append({
            "urun": name,
            "fiyat":price,
            "stok": stock
        })
print(urunler)