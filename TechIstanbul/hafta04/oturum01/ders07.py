"""
1. Normal Örneklem (Instance) Method

Bunlar, sınıftan oluşturulan nesneye (instance'a) ait metotlardır.
İlk parametre self olmalıdır. Bu, nesnenin kendisini temsil eder.
"""

class Ogrenci:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    def bilgileriGoster(self):  # instance method
        print(f"Ad: {self.ad}, Soyad: {self.soyad}")

# Nesne oluşturma
ogr1 = Ogrenci("Berk","Ar")
ogr1.bilgileriGoster()  # Ad: Berk, Soyad: Ar

# __init__ bir constructor (yapıcı) metottur, nesne oluşturulurken otomatik çağrılır.

# bilgileriGoster normal bir metottur; self üzerinden nesne verilerine erişir.

print("-----------------------------------------------------")

"""
2. Class Method (@classmethod)

Bu metotlar sınıfın kendisine aittir, nesneye değil.
İlk parametre olarak cls alır (class'ı temsil eder).
@classmethod dekoratörü ile tanımlanır.

"""

class Okul:
    okulAdi = "Techİstanbul Akademi"

    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    @classmethod    # classmethod başına eklenir.
    def okulBilgisi(cls):  # parametre olarak cls alır ki bu sınıfı temsil eder.
        print(f"Bu öğrenciler {cls.okulAdi} okuluna gidiyor.")

# Sınıftan direkt çağrılabilir.
Okul.okulBilgisi()  # Bu öğrenciler Techİstanbul Akademi okuluna gidiyor.

# cls, sınıfın kendisini temsil eder.
# okulAdi gibi class değişkenlerine erişmek için kullanılır.
# nesne oluşturulmadan çağrılabilir.

print("-----------------------------------------------------")

"""
3. Statik Method (@staticmethod)

Bu metotlar ne sınıfa ne de nesneye bağlıdır -
bağımsız fonksiyonlar gibidir ama sınıf içinde tanımlanır.
@staticmethod dekoratörü kullanılır ve ne self ne cls parametresi alır.
"""

class Matematik:
    @staticmethod
    def topla(a, b):
        return a + b
    
    @staticmethod
    def carp(a, b):
        return a * b
    
print(Matematik.topla(5, 3))    # 8
print(Matematik.carp(4, 2)) # 8