class Calisan:
    zamOrani = 1.05
    personelSayisi = 0

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad + "." + self.soyad + "@sirket.com"
        Calisan.personelSayisi += 1

    def tamad(self):
        return f"Adı: {self.ad} - Soyadı: {self.soyad}"
    
    def arttir(self):
        self.maas = (self.maas * self.zamOrani)

class Gelistirici(Calisan):
    def __init__(self, ad, soyad, maas, programlamaDili):
        super().__init__(ad, soyad, maas)
        self.programlamaDili = programlamaDili
        self.zamOrani = 1.2

class Yonetici(Calisan):
    def __init__(self, ad, soyad, maas, calisanlar = None):
        super().__init__(ad, soyad, maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar
    
    def elemanEkle(self, eleman):
        self.calisanlar.append(eleman)

    def elemanCikar(self, eleman):
        self.calisanlar.remove(eleman)

    def calisanListele(self):
        for eleman in self.calisanlar:
            print(eleman.tamad())

personel1 = Calisan("Alex","Kick",10000)
personel2 = Calisan("Sona", "Stick", 20000)

gel1 = Gelistirici("Tuğba", "Ar", 30000, "Python, Kotlin")

yonet1 = Yonetici("Berk", "Ar", 25000, [gel1, personel1])

yonet1.elemanEkle(personel2)
yonet1.calisanListele() # Adı: Tuğba - Soyadı: AR
print("---------------------------")
print(yonet1.tamad())   # Adı: Berk - Soyadı: Ar
print("---------------------------")
yonet1.elemanCikar(personel1)
yonet1.calisanListele()
print("---------------------------")
print(isinstance(personel1, Yonetici))  # False
print(isinstance(gel1, Gelistirici))    # True
print("---------------------------")
print()