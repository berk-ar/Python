# Metotlar (Methods)
# Sınıf içinde tanımlanan fonksiyonlardır.
# self parametresi zorunludur (otomatik aktarılır).

# self Anahtar kelimesi
# Her metot ilk parametre olarak self alır.
# Python, nesne.metot() çağrısında self otomatik eklenir.
# self yerine başka isim de kullanılabilir ama best practice değildir.

class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileriGoster(self):
        return f"{self.marka} - {self.model}"

araba1 = Araba("Volkswagen", "Golf")
print(araba1.bilgileriGoster()) # Volkswagen - Golf

class Ogrenci:
    bolum = "Mühendislik"
    bina = "Doğu Blok"
    def __init__(self, ad, soyad, tcno):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tcno

    def tamad(self):
        self.tamisim = self.ad + self.soyad
        return self.tamisim
    def __str__(self):
        return self.ad + self.soyad
    
ogr1 = Ogrenci("Berk","Ar","121212121212")
print(ogr1.tamad())
print(vars(ogr1))