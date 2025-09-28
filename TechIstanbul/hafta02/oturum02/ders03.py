ogrenci = ["Berk", 25, "Yazılım"]

# sozluk = { key : value, key1 : value1, ...}
ogrenci_sozluk = {
    "isim" : "Berk",
    "yas" : 25,
    "bolum" : "Yazılım"
}

print(type(ogrenci_sozluk)) # <class 'dict'>
print(ogrenci_sozluk["bolum"])  # Yazılım

ogrenci_sozluk["meslek"] = "Yazılımcı"  # input("Mesleğinizi giriniz: ")

print(ogrenci_sozluk)

print(ogrenci_sozluk.keys())    # dict_keys(['isim', 'yas', 'bolum', 'meslek'])
print(ogrenci_sozluk.values())  # dict_values(['Berk', 25, 'Yazılım', 'Yazılımcı'])

for dd in ogrenci_sozluk:
    print(dd, ogrenci_sozluk[dd])   # isim Berk ....

print("-----------------------------------------------")

for anahtar, deger in ogrenci_sozluk.items():
    print(anahtar, deger)