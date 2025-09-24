#if True:
#    pass

"""
for dd in range(10):
    ad = input("Adınızı giriniz: ")
    if ad == "Berk":
        print("Berk bulundu.")
        break
    print(dd+1,". öğrenciye soruldu.")
"""

for dd in range(10):
    print(dd+1)
    ad = input("Adınızı giriniz: ")
    if ad == "Berk":
        print("bu kişi kayıtlı")
        continue
    soyad = input("Soyadınızı giriniz: ")
    print(ad, soyad, "Kursumuza hoşgeldiniz.")