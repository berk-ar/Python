# Özellikler yani Attributes
"""
Örnek (instance) özellikleri: self ile tanımlanır, her nesneye özeldir.
Sınıf (class) özellikleri: Sınıf seviyesinde, tüm nesneleri kapsar.
"""

class Araba:
    tekerlekSayisi = 4 # sınıf özelliği attribute

class Ogrenci:
    kurs = "Python 80 Saat Bootcamp"
    fakulte = ""

print(Araba.tekerlekSayisi) # 4
print(Ogrenci.kurs) # Python 80 Saat Bootcamp 

ogr1 = Ogrenci()
print(ogr1.kurs)    # Python 80 Saat Bootcamp 
ogr1.fakulte = "Mühendislik"
print(ogr1.fakulte) # Mühendislik
print(Ogrenci.fakulte)  # 