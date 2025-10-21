# Nesne Yönelimli Programlama (OOP), gerçek dünyadaki varlıkları ve ilişkileri modellememizi sağlayan bir program
"""
Yapısal programlamadan farkı: Kodun tekrar kullanılabilirliği, modülerliği ve bakım kolaylığı.
Gerçek dünyadaki benzetimi: Nesneler -> Özellikler (attributes) + Davranışlar (methods).
Python'da her şey nesnedir: int, str, list gibi tipler bile birer sınıftır.
"""

"""
# OOP öncesi - Fonksiyonel Yaklaşım
def ogrenciOlustur(ad, yas, notOrtalamasi):
    return {"ad": ad, "yas": yas, "notOrtalamasi": notOrtalamasi}

def ogrenciBilgileri(ogrenci):
    return f"{ogrenci['ad']}, {ogrenci['yas']} yaşında, Not: {ogrenci['notOrtalamasi']}"

def ogrenciBilgileriGuncelle(ogrenci, **kwargs):
    for anahtar, deger in kwargs.items():
        if anahtar in ogrenci:
            ogrenci[anahtar]=deger
    return ogrenci
    
# Kullanım
ogrenci1 = ogrenciOlustur("Berk", 25, 100)
print(ogrenciBilgileri(ogrenci1))
ogrenciBilgileriGuncelle(ogrenci1,ad="Tuğba")
print(ogrenciBilgileri(ogrenci1))
"""

class Ogrenci:
    def __init__(self, ad, yas, notOrtalamasi):
        self.ad = ad
        self.yas = yas
        self.notOrtalamasi = notOrtalamasi

    def bilgileriGoster(self):
        return f"{self.ad}, {self.yas} yaşında ve ortalaması {self.notOrtalamasi}"
    
ogrenci1 = Ogrenci("Berk", 25, 95.5)
print(ogrenci1.bilgileriGoster())
ogrenci2 = Ogrenci("Tuğba", 25, 100)
print(ogrenci2.bilgileriGoster())