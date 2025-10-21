"""
KALITIM TEMEL KAVRAMLARI:
- Üst sınıf (Parent class): Temel sınıf
- Alt sınıf (Child class): Üst sınıftan türeyen sınıf
- super(): Üst sınıfın metotlarına erişim
"""

class Ogrenci:
    ogrenciDersler = ["edebiyat", "tarih"]
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
class BolumOgrenci(Ogrenci):
    bolumDersler = ["algoritma", "veri yapıları"]
    def __init__(self, ad, soyad, bolum):
        super().__init__(ad, soyad)
        self.bolum = bolum

class FakulteOgrenci(BolumOgrenci):
    fakulteDersler = ["mühendislik tarihi"]
    def __init__(self, ad, soyad, bolum, fakulte):
        super().__init__(ad, soyad, bolum)
        self.fakulte = fakulte

ogrenci1 = Ogrenci("Berk", "AR")
print(vars(ogrenci1), ogrenci1.ogrenciDersler)  # {'ad': 'Berk', 'soyad': 'AR'} ['edebiyat', 'tarih']

ogrenci2 = BolumOgrenci("Tuğba", "AR", "Bilgisayar Mühendisliği")
print(vars(ogrenci2), ogrenci2.bolumDersler)   # {'ad': 'Tuğba', 'soyad': 'AR', 'bolum': 'Bilgisayar Mühendisliği'} ['algoritma', 'veri yapıları']