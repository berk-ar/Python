class Hayvan:
    def __init__(self, ad):
        self.ad = ad

    def sesCikar(self):
        print("Bilinmeyen Ses")

class Kopek(Hayvan):
    def sesCikar(self):
        print("hav hav")

class Kus(Hayvan):
    def __init__(self, ad, kanatUzunlugu):
        Hayvan.__init__(self,ad)
        self.kanatUzunlugu = kanatUzunlugu

    def ucma(self):
        print("Kuş uçuyor")
        

kopek1 = Kopek("Mavi")
print(kopek1.ad)    # Mavi
kopek1.sesCikar()   # hav hav

print("--------------------------")

kus1 = Kus("Maviş", 2.5)
print(vars(kus1))