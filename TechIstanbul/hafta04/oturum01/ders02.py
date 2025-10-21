# Class tanımlama: nesnelerin şablonudur, nesnelerin hangi özelliklere ve işlevlere sahip olabileceğini belirtir.

class Araba:
    pass

araba1 = Araba()
araba2 = Araba()

class Ogrenci:
    pass

ogrenci1 = Ogrenci()
ogrenci1.ad = "Berk"

print(type(ogrenci1))   # <class '__main__.Ogrenci'>
print(ogrenci1.ad) # Berk

ogrenci2 = Ogrenci()
print(type(ogrenci2))
