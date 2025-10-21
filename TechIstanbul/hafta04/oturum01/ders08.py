# class içerisinde tanımlanabilen tüm metotlar ile ilgili ortak örnek

class Calisan:
    zamOrani = 1.1  # class değişkeni

    def __init__(self, ad, maas):
        self.ad = ad
        self.maas = maas

    def maasGoster(self):   # instance metot
        print(f"{self.ad} maaşı: {self.maas}")

    @classmethod
    def zamYap(cls, oran):
        cls.zamOrani = oran
        print(f"Yeni zam oranı: {cls.zamOrani}")

    @staticmethod
    def bilgi():
        print("Bu sınıf çalışan maaşlarını yönetir.")

# Kullanım
c0 = Calisan("Berk", 10000)
Calisan.bilgi() # Bu sınıf çalışan maaşlarını yönetir.
Calisan.zamYap(1.5) # Yeni zam oranı: 1.5
c1 = Calisan("Tuğba", 15000)
c1.maasGoster() # Tuğba maaşı: 15000
print(c1.zamOrani)  # 1.5