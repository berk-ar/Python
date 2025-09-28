ogrenciler = []

print("="*5, "Öğrenci Not Sistemi", "="*5)
print("Çıkmak için Çık yazınız")

while True:
    ad = input("Adınızı Giriniz: ")
    if ad.lower() == "çık":
        break
    puan = int(input("Notunuzu Giriniz: "))
    if puan < 0:
        break
    ogrenciler.append({
        "ad": ad,
        "puan": puan
    })

print(ogrenciler)
