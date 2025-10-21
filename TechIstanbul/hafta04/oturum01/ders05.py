# __init__ Metodu - Kurucu (Constructor)
# Nesne oluşturulurken otomatik çağrılır.
# Başlangıç durumunu (özellikleri) tanımlar.

class Araba:
    tekerSayisi = 4
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

araba1 = Araba("Volkswagen", "Golf")
print(araba1.marka, araba1.model)   # Volkswagen Golf
print(vars(araba1)) # {'marka': 'Volkswagen', 'model': 'Golf'}
araba2 = Araba("Renault", "Megane 4")
print(araba2.marka, araba2.model)   # Renault Megane 4
print(vars(araba2)) # {'marka': 'Renault', 'model': 'Megane 4'}

class Ogrenci:
    bolum = "Mühendislik" # sınıf class attributes
    bina = "Doğu Blok"
    def __init__(self):
        self.ad = ""    # örnek instance attributes
        self.soyad = ""
        self.tcno = ""

ogr1 = Ogrenci()
print(ogr1.bolum)
ogr1.ad = "Berk"
print(ogr1.ad)
ogr2 = Ogrenci()
print(ogr2.ad)